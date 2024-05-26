import fitz  # PyMuPDF
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

# Initialize Hugging Face's transformers pipeline with a suitable model
model_name = "deepset/roberta-base-squad2"  # You can replace this with any suitable QA model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file located at file_path.
    """
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text

def process_question_with_nlp(text: str, question: str) -> str:
    """
    Processes the question using the text extracted from the PDF with a local language model.
    """
    try:
        result = qa_pipeline({
            'context': text,
            'question': question
        })
        return result['answer']
    except Exception as e:
        print(f"Error processing question with NLP: {e}")
        return "Could not process the question."

