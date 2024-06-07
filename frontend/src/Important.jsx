
import { useState } from "react"
import axios from 'axios'

function Important() {
  const [data, setData] = useState(null);
  const [input, setInput] = useState('')
  const [systemRole, setSystemRole] = useState('')
  const [loading, setLoading] = useState(false)
  function clickHandler(e) {

    e.preventDefault()
    if (input.trim() === "" && systemRole.trim() === "") {
      return;
    }
    setLoading(true)
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
        console.log("This is Error", e);

        setLoading(false)

      })
  }


  return (
    <div className='App'>
      <h1>Data from Django API:</h1>
      {loading ? <h3>Loading...</h3> : <pre>{data && data._output}</pre>}


      {!data &&
        (<>  <input type='text' value={input} onChange={(e) => setInput(e.target.value)} name='_input' />,
          <br />
          <input type='text' value={systemRole} onChange={(e) => setSystemRole(e.target.value)} name='system_role' />
          <button type='submit' onClick={clickHandler}>Send</button>
        </>)
      }
    </div>
  );
}

const Test = () => {
  return (<h2>test Component</h2>)
}
export { Important };

export default Test;
