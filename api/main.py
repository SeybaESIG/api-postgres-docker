from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import db

app = FastAPI(title="API avec PostgreSQL et Docker")


class UserCreate(BaseModel):
    name: str


@app.on_event("startup")
def on_startup():
    """Initialise la base de données au démarrage."""
    db.init_db()


@app.get("/health", summary="Health check")
def health_check():
    """Retourne le statut de l'API."""
    return {"status": "ok"}


@app.get("/users", summary="Liste des utilisateurs")
def list_users():
    """Récupère la liste des utilisateurs depuis la base PostgreSQL."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM users ORDER BY id;")
            rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/users", status_code=201, summary="Créer un utilisateur")
def create_user(user: UserCreate):
    """Ajoute un nouvel utilisateur dans la base."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name) VALUES (%s) RETURNING id, name;",
                (user.name,),
            )
            new_user = cur.fetchone()
        conn.commit()
        conn.close()
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
