import React from 'react'
import SimpleValuesProps, { ArrayOfObjectsValueProps, ArrayValueProps, ObjectValueProps } from './PropsChildComponents';

const PropsDemo = () => {

    const namesArray = ["Ashish","praveen","rahul","ram"];

    const studentObject = {id: 1, name: "jerome", score: "85"};

    const studentArrayOfObjects = [
      {id: 1, name: "Suyash", score: "85"},
      {id: 2, name: "Jay", score: "80"},
      {id: 3, name: "Yash", score: "55"},
      
    ]
  return (
    <div>
        <ArrayOfObjectsValueProps studentObjects={studentArrayOfObjects} />
    </div>
    // <div>
    
    //     <ArrayValueProps names = {namesArray} />
    //     <ObjectValueProps student = {studentObject}/>
    
    // <SimpleValuesProps character="Tony Stark" heroName = "IronMan" Production="Marvel"/>
    // <SimpleValuesProps character="Steve Rogers" heroName = "Captian America" Production="Marvel Cinemas"/>
    // <SimpleValuesProps character="Bruce Banner" heroName = "Hulk" Production="MCU"/>
    
    // </div>
  );
};

export default PropsDemo