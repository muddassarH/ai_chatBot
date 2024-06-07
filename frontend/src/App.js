// import React, { useState } from 'react'
// import axios from 'axios'
import React from 'react';
import Test1, { Important } from './Important';
import { Home } from './Home';

function App() {
  const [isHomePage, setisHomepage] = React.useState(true)

  return (
    <>

      {isHomePage ? <Home /> : <Important />}


      <button onClick={(e) => setisHomepage(!isHomePage)}>Call Api</button>
    </>
  );


}

export default App;