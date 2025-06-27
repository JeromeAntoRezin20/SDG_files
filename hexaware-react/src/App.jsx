import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Ex01FirstComponent from "./components/Ex01FirstComponent"
import Ex03ThirdComponent from './assignments/AS01ThirdComponent'
import Ex03JsxDemo from './components/Ex03JsxDemo'
import { AS02DeveloperInfo } from './assignments/AS02DeveloperInfo'
import { AS03TableInfo } from './assignments/AS03TableInfo'
import Ex04ArraysDemo from './components/Ex04ArraysDemo'
import Assignment01 from './components/assignments/day2/Assignment01'
import Ex05ConditionalRendering from './components/Ex05ConditionalRendering'
import StudentIdComponent, { StudentNameComponent, StudentScoreComponent } from './components/Ex06ImportExport'
import ProductInfoComponent, { ProductPriceComponent, ProductStockComponent } from './components/assignments/day2/Assignment03'
import Ex07StylingDemo from './components/Ex07StylingDemo'
import styles from "./styles/Ex07StylingDemo.module.css"
import Ex08BootstrapDemo from './components/Ex08BootstrapDemo'
import Ex09Images from './components/Ex09Images'
import PropsDemo from './components/PropsDemo/PropsDemo'
import StudentProfile from './components/PropsExample/StudentProfile'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>

{/* <h2 className='external-class'> Styled with External style sheet 
  In app jsx Styled with External Style sheet
  </h2>

  <h3 className={styles.moduleStyle}> Styled with css module </h3> */}

<hr/>
    {/* <Ex01FirstComponent/> 
    <Ex03ThirdComponent/> */}
    {/* <Ex03JsxDemo/> */}
    {/* <AS02DeveloperInfo/> */}
    {/* <AS03TableInfo/> */}
    {/* <Ex04ArraysDemo/>
    <Assignment01/> */}
    {/* <Ex05ConditionalRendering/> */}
    {/* <StudentIdComponent />
    <StudentNameComponent />
    <StudentScoreComponent /> */}

    {/* <ProductInfoComponent/>
    <ProductPriceComponent/>
    <ProductStockComponent/> */}

    {/* <Ex07StylingDemo/> */}
    {/* <Ex08BootstrapDemo/>
    <Ex09Images/> */}

    {/* <PropsDemo/> */}

    <StudentProfile/>
    
    </>
  )
}

export default App
