
## Setup Instructions

### Backend

1. Navigate to the `backend` directory:

    ```sh
    cd backend
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv env1
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Start the FastAPI server:

    ```sh
    uvicorn app.main:app --reload
    ```

### Frontend

1. Navigate to the `frontend` directory:

    ```sh
    cd frontend
    ```

2. Install the dependencies:

    ```sh
    npm install
    ```

3. Start the React development server:

    ```sh
    npm start
    ```

### Usage

1. Open your browser and navigate to `http://localhost:3000`.

2. Use the interface to upload PDF files and ask questions about their content.

## API Endpoints

### Upload PDF

- **URL:** `/upload_pdf/`
- **Method:** `POST`
- **Parameters:** `file` (form-data, required)
- **Response:** JSON object with filename and extracted text.

### Ask Question

- **URL:** `/ask_question/`
- **Method:** `POST`
- **Parameters:** `filename` (string, required), `question` (string, required)
- **Response:** JSON object with the answer to the question.

## Additional Information

This application uses FastAPI for the backend, React for the frontend, and Hugging Face Transformers for natural language processing. The PDF documents are stored locally, and the metadata is stored in a SQLite database.
