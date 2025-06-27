import React from 'react'

const Ex05ConditionalRendering = () => {

    const students = [
        {id: 1, name: "Riya", score: 85},
        {id: 2, name: "Amit", score: 60},
        {id: 3, name: "Neha", score: 95},
        {id: 4, name: "Kumal", score: 40}
    ];

    const result = students.find((student) => student.score > 100);
    console.log(`Result : ${result}`);
  return (
    <>
    {result ? <Comp1/> : <Comp2/>}
    <hr />
    </>
  )
};

const Comp1 = () => {
    return (
        <>
        <p>Students Present</p>
        </>
    )
}

const Comp2 = () => {
    return (
        <>
        <p>Students Absent</p>
        </>
    )
}

export default Ex05ConditionalRendering