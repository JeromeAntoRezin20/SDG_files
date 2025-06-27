import React from 'react'

const Ex04ArraysDemo = () => {
    const students = [
        {id: 1, name: "Riya", score: 85},
        {id: 2, name: "Amit", score: 60},
        {id: 3, name: "Neha", score: 95},
        {id: 4, name: "Kumal", score: 40}
    ];

     {/*  filter demo */}

    // console.log("students : ", students);
    // const passedStudents = students.filter((student) => student.score >= 50 && student.score <=85);  
    // console.log("Passed students : ",passedStudents)

    const student = students.find((student) => student.score > 90);
    console.log(`1st student with marks > 90 : ${student.name}`);

    const totalMarks = students.reduce((sum, student) => {
        return sum + student.score;
    }, 0);
    console.log(`Total Score : ${totalMarks}`);

    const average = totalMarks / students.length;
    console.log(`Average : ${average}`);

    const scores = students.map((student) => student.score);
    console.log(`Scores: ${scores}`);

    const maxScore = Math.max(...scores);
    console.log(`Max Score : ${maxScore}`);

    const topper = students.filter((s) => s.score == maxScore);
    console.log(`Toppers : ${topper[0].name}`);

  return <>  

  {/* map() demo */}

  {
    students.map((student) => 
        (
            <p key = {student.id}>
                {student.id}. {student.name} - {student.score}
            </p>
        ))}
    <hr />
    {/* filter demo */}

    <ol>
        {students.filter((student) => student.score >= 50 && student.score <=85).map((p) => (
            <li>
                {p.name} - {p.score}
            </li>
        ))}
    </ol>

  </>
}

export default Ex04ArraysDemo