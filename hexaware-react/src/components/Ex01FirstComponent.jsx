import React from 'react'
import Ex02NestedComponent from './Ex02NestedComponent'

//Shortcut => rafc

const Ex01FirstComponent = () => {
  return (
    <React.Fragment>
        <h1>Ex01FirstComponent</h1>
        <h1>Heading 1</h1>
        <h2>
            Heading 2
        </h2>
        <Ex02NestedComponent />
        </React.Fragment>
  )
}

export default Ex01FirstComponent