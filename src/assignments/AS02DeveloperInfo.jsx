import React from 'react'

export const AS02DeveloperInfo = () => {
    const developerName = "Jerome Anto"
    const experience = 2
    const isAvailable = true
  return (
    <>
    <h2>Developer Name : {developerName}</h2>
    <p>Experience : {experience} years</p>
    <p>{isAvailable ? "Available" : "Not Available"}</p>
    </>
  )
}
