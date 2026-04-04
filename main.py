from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartNotes API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notes", response_model=schemas.NoteResponse)
def create(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

@app.get("/notes")
def read(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.delete("/notes/{note_id}")
def delete(note_id: str, db: Session = Depends(get_db)):
    return {"deleted": crud.delete_note(db, note_id)}
