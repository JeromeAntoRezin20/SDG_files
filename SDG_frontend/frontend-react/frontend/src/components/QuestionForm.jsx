import React, { useState } from 'react';
 
function QuestionFetcher() {
  const [employeeId, setEmployeeId] = useState('');
  const [questions, setQuestions] = useState([]);
  const [field, setField] = useState('');
  const [error, setError] = useState('');
 
  const fetchQuestions = async () => {
    try {
const response = await fetch(`http://localhost:8086/get_questions/${employeeId}`, {
        method: 'GET',
      });
 
      if (!response.ok) {
        throw new Error('Employee not found or server error');
      }
 
      const data = await response.json();
      setField(data.field);
      setQuestions(data.questions);
      setError('');
    } catch (err) {
      console.error('Error fetching questions:', err);
      setError('Employee not found. Please check the Employee ID.');
      setQuestions([]);
      setField('');
    }
  };
 
  return (
    <div className="question-fetcher">
      <h2>Get Questions for Employee</h2>
      <input
        type="text"
        placeholder="Enter Employee ID"
        value={employeeId}
onChange={(e) => setEmployeeId(e.target.value)}
      />
      <button onClick={fetchQuestions}>Fetch Questions</button>
 
      {error && <p style={{ color: 'red' }}>{error}</p>}
 
      {field && questions.length > 0 && (
        <div>
          <h3>Field: {field}</h3>
          <ul>
{questions.map((q, index) => (
              <li key={index}>{q}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
 
export default QuestionFetcher;




// function QuestionForm({ questions, answers, setAnswers }) {
//     return (
//       <div>
//   {questions.map((q, i) => (
//           <div key={i}>
//             <p><strong>❓ {q.question}</strong></p>
//             <input
//               value={answers[q.field] || ""}
//               onChange={(e) =>
//   setAnswers({ ...answers, [q.field]: e.target.value })
//               }
//               placeholder="Your answer"
//             />
//           </div>
//         ))}
//       </div>
//     );
//   }
   
//   export default QuestionForm;