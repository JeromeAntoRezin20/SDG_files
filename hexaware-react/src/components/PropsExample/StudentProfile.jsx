import React from 'react';
import students from "../../api/studentsJson.json";
import StudentCard from './StudentCard';
import styles from "./StudentProfile.module.css";

const StudentProfile = () => {
  return (
    <div>
        <h2 className={styles.heading}>Student Profiles</h2>
        <div className={styles.grid}>
            {students.map((student) => (
                <StudentCard key={student.roll_no} student={student} />
            ))}
        </div>
    </div>
  )
}

export default StudentProfile