import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Homepage } from './Homepage'
import { Input_Form } from './input_form'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Homepage/>
      <Input_Form/>
    </>
  )
}

export default App
