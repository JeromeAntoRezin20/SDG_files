import React from 'react'

export const AS03TableInfo = () => {

    const students = [
        { name: "Abhishek", age: 25, isPresent: true },
        { name: "Jerome", age: 22, isPresent: false },
        { name: "Anto", age: 29, isPresent: true },
        { name: "Rezin", age: 24, isPresent: false },
        { name: "Nila", age: 21, isPresent: true }
    ]
    return (
        <>
        <table border={1}>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Presence</th>
                </tr>

                {students.map((student,index) =>{
                    return(
                        <tr>
                            <td>{student.name}</td>
                            <td>{student.age}</td>
                            <td>{student.isPresent ? "Present" : "Absent"}</td>
                        </tr>
                    )
                })}
            </thead>
        </table>
        </>
    )
}
