import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [data, setData] = useState(null);
  const [input, setInput] = useState('')
  const [systemRole, setSystemRole] = useState('')
  const [loading, setLoading] = useState(false)


  function clickHandler(e) {
    setLoading(true)
    e.preventDefault()
    axios({
      method: 'post',
      data: {
        _input: input,
        system_role: systemRole
      },
      url: 'http://localhost:8000/api/'
    })
      .then(data => {
        setData(data.data);

        setLoading(false)

      })
      .catch((e) => {
        console.log("THis is Error", e);

        setLoading(false)

      })
  }


  return (
    <div className='App'>
      <h1>Data from Django API:</h1>
      {loading ? <h3>Loading...</h3> : <pre>{data && data._output}</pre>}
      <input type='text' value={input} onChange={(e) => setInput(e.target.value)} name='_input' />,
      <br />
      <input type='text' value={systemRole} onChange={(e) => setSystemRole(e.target.value)} name='system_role' />
      <button type='submit' onClick={clickHandler}>Send</button>
    </div>
  );
}

export default App;