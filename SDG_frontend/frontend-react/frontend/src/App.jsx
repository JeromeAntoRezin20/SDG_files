import { useState } from "react";
import QuestionForm from "./components/QuestionForm";
import axios from "axios";
 
function App() {
  const [employeeId, setEmployeeId] = useState("");
  const [questions, setQuestions] = useState([]);
  const [employeeName, setEmployeeName] = useState("");
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);
 
  const handleFetch = async () => {
    try {
const res = await axios.post("http://localhost:8086/get-questions/", {
        employee_id: employeeId,
      });
setQuestions(res.data.questions);
setEmployeeName(res.data.employee_name);
      setResult(null);
    } catch (err) {
      alert("Employee not found");
    }
  };
 
  const handleSubmit = async () => {
const formattedAnswers = questions.map(q => ({
      field: q.field,
      template: q.template,
      answer: answers[q.field] || ""
    }));
const res = await axios.post("http://localhost:8086/submit-answers/", {
      employee_id: employeeId,
      answers: formattedAnswers
    });
setResult(res.data.success ? "✅ Access Granted" : "❌ Access Denied");
  };
 
  return (
    <div style={{ padding: "20px" }}>
      <h1>Employee Verification</h1>
      <input
        placeholder="Enter Employee ID"
        value={employeeId}
onChange={(e) => setEmployeeId(e.target.value)}
      />
      <button onClick={handleFetch}>Fetch Questions</button>
 
      {employeeName && (
        <div>
          <h2>Welcome, {employeeName}</h2>
          <QuestionForm
            questions={questions}
            answers={answers}
            setAnswers={setAnswers}
          />
          <button onClick={handleSubmit}>Submit Answers</button>
        </div>
      )}
 
      {result && <h3>{result}</h3>}
    </div>
  );
}
 
export default App;