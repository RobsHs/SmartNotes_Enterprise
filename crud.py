from sqlalchemy.orm import Session
from models import Note

def create_note(db: Session, note):
    db_note = Note(
        title=note.title,
        content=note.content,
        tags=",".join(note.tags)
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session):
    return db.query(Note).all()

def delete_note(db: Session, note_id: str):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
        return True
    return False
