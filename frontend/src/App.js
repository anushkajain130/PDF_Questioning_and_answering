import React from 'react';
import UploadComponent from './components/UploadComponents';
import QuestionComponent from './components/QuestionComponents';

const App = () => {
    return (
        <div>
            <h1>PDF Q&A Application</h1>
            <UploadComponent />
            <QuestionComponent />
        </div>
    );
};

export default App;
