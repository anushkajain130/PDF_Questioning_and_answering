from sqlalchemy.orm import Session
from app import models

def create_document(db: Session, filename: str, file_path: str):
    db_document = models.Document(filename=filename, file_path=file_path)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document_by_filename(db: Session, filename: str):
    return db.query(models.Document).filter(models.Document.filename == filename).first()