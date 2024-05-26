import React, { useState } from 'react';
import axios from 'axios';

const UploadComponent = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    }; 

    const handleUpload = async () => {
        if (!file) {
            setMessage("Please select a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post("http://localhost:8000/upload_pdf/", formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            });
            setMessage(`File uploaded: ${response.data.filename}`);
        } catch (error) {
            console.error(error);
            if (error.response) {
                setMessage(`Error: ${error.response.data.detail}`);
            } else {
                setMessage("An unexpected error occurred.");
            }
        }
    };

    return (
        <div>
            <h2>Upload PDF</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            <p>{message}</p>
        </div>
    );
};

export default UploadComponent;
