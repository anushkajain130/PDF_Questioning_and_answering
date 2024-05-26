import React, { useState } from 'react';
import axios from 'axios';

const QuestionComponent = () => {
    const [filename, setFilename] = useState("");
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleQuestionSubmit = async () => {
        try {
            const response = await axios.post("http://localhost:8000/ask_question/", { filename, question });
            setAnswer(response.data.answer);
        } catch (error) {
            setAnswer(`Error: ${error.response.data.detail}`);
        }
    };

    return (
        <div>
            <h2>Ask a Question</h2>
            <input type="text" placeholder="Filename" value={filename} onChange={(e) => setFilename(e.target.value)} />
            <input type="text" placeholder="Question" value={question} onChange={(e) => setQuestion(e.target.value)} />
            <button onClick={handleQuestionSubmit}>Submit</button>
            <p>{answer}</p>
        </div>
    );
};

export default QuestionComponent;
