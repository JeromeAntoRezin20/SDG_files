import React from 'react'

const student = {id : 1, name : "Satish", score : 80};

const StudentIdComponent = () => {
  return <div>Student id: {student.id}</div>;
};

const StudentNameComponent = () => {
    return <div>Student name: {student.name}</div>;
  };

const StudentScoreComponent = () => {
    return <div>Student Score: {student.score}</div>;
};

export default StudentIdComponent
export  {StudentNameComponent, StudentScoreComponent}