import React from 'react'
// Shortcut ==> rafce

const Ex03JsxDemo = () => {
    const companyName = "Hexaware";
    const numberOfTeams = 10;
    const isLoggedIn = true;
    const cities = ["Chennai","Bangalore","Mumbai","Delhi","Hyderabad"]
    const profile = { name: "Abhishek", age: 25, isPresent: true }

    const students = [
        { name: "Abhishek", age: 25, isPresent: true },
        { name: "Jerome", age: 22, isPresent: false },
        { name: "Anto", age: 29, isPresent: true },
        { name: "Rezin", age: 24, isPresent: false },
        { name: "Nila", age: 21, isPresent: true }
    ];

    return(
        <>
        <h1>Company Name: {companyName}</h1> 
        <p>No of Teams: {numberOfTeams}</p>
        <p>{isLoggedIn ? "Welcome user" : "Log in"}</p>  
        <ul>
            <li>{cities[0]}</li>
            <li>{cities[1]}</li>
            <li>{cities[2]}</li>
        </ul>
        <hr />
        <ol>
            {
                cities.map((city, index) =>{
                    return <li key={index}>{city}</li>;
                })
            }
        </ol>
        <p>Name : {profile.name}</p>
        <p>Age : {profile.age}</p>
        <p>Is Present : {profile.isPresent ? "Yes" : "No" }</p>

        {students.map((student, index) => {
            return (
                <p key={index}>
                Name : {student.name}, Age : {student.age}, Attendance : {student.isPresent ? "Present" : "Absent"}
                </p>
            );
            })
        }
    </>
    )
}

export default Ex03JsxDemo