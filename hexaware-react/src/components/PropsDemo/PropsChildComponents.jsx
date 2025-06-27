import React from 'react'

const SimpleValuesProps = (props) => {
    console.log (props)

    // Destructuring Object

    const {character, heroName, Production} = props;
  return (
    <div>
        <p>
            Character : {character}, Hero Name : {heroName}, ProductionHouse : {Production}
        </p>
    </div>
  );
};

export default SimpleValuesProps



export const ArrayValueProps = ({names}) => {
//   console.log(props)
//   console.log(props.names)
  return (
    <div>

        {names.map((name, index) =>
            <p key = {index}>{name}</p> )}

    </div>
  )
}

export const ObjectValueProps=(props) => {
return (
    <>
    <p>
        Id : {props.student.id}, Name : {props.student.name}, Score :  {props.student.score}
    </p>
    </>
)
}

export const ArrayOfObjectsValueProps=({studentObjects}) => {
  // const {studentObjects} = props;
return (
  <>
  {
    studentObjects.map((student, index) => <p key = {student.id}> {student.id}. {student.name} - {student.score}</p>)
  }
  </>
)
}


