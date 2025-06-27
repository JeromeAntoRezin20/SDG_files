import React from 'react'
import reactLogo from 'react';
const Ex09Images = () => {
  return (
    <div>
        {/* Importing image from public folder */}
        <p>
            <img src = "./images/vite.svg" />
        </p>

        {/* Importing image from assests folder */}
        <p>
            <img src = {reactLogo} />
        </p>
    </div>
  )
}

export default Ex09Images