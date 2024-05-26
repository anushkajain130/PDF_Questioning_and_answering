from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import crud, models, database, nlp
from app.database import SessionLocal, engine
from pydantic import BaseModel
import os
import logging

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
models.Base.metadata.create_all(bind=engine)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuestionRequest(BaseModel):
    filename: str
    question: str

# Define routes 

#Upload PDF file
@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    print("hello")
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")

    contents = await file.read()
    file_path = f"./uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    text = nlp.extract_text_from_pdf(file_path)
    if(text):
        print("Text extracted from pdf")
    document = crud.create_document(db, file.filename, file_path)
    if(document):
     print("Document created in database")
    return {"filename": file.filename, "text": text}

@app.post("/ask_question/")
async def ask_question(request: QuestionRequest, db: Session = Depends(database.get_db)):
    
    filename = request.filename
    question = request.question
    if(filename):
        print("Received question for file {filename}")

    logger.info(f"Received question for file {filename}")

    try:
        document = crud.get_document_by_filename(db, filename)
        if not document:
            logger.error("Document not found")
            raise HTTPException(status_code=404, detail="Document not found")

        text = nlp.extract_text_from_pdf(document.file_path)
        if(text):
            print("Text extracted from pdf")
        answer = nlp.process_question_with_nlp(text, question)
        if(answer):
            print("Answered the question")
        logger.info(f"Question processed with answer: {answer}")

        return {"answer": answer}
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
