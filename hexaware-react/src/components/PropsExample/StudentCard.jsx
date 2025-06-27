import React from 'react'
import styles from "./StudentCard.module.css";

const StudentCard = ({ student }) => {
    const { roll_no, full_name, course, email, finalScore, imageUrl} = student;
  return (
    <div className={styles.card}> 
    <img src={imageUrl} alt={full_name} className={styles.image}/>
    <h3> {full_name} </h3>
    <p> Roll No: {roll_no} </p>
    <p> Course: {course} </p>
    <p> Email: {email} </p>
    <p className = {finalScore < 40 ? styles.fail : styles.pass} >
        Final Score: {finalScore}
    </p>
    
    </div>
  )
}

export default StudentCard