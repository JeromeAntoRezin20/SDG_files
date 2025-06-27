import React from 'react'
import '../styles/styles.css'
import styles from "../styles/Ex07StylingDemo.module.css"

const Ex07StylingDemo = () => {
    const headingStyle={
        border : "1px solid black",
        backgroundColor : "green",
        color : "blue",
    };
  return (
    <div>
        <h1 style = {{ backgroundColor: "yellow", color: "green"}}>
            Styled with Inline Style Object 
        </h1>


        <h1 style = {headingStyle}> Styled with Internal Style Object</h1>
        <p style = {headingStyle}> Styled with Internal Style Object</p>

        <hr />
        <h3 className={styles.moduleStyle}> Styled with css module </h3>

    </div>
  );
};

export default Ex07StylingDemo