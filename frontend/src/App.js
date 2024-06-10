// import React, { useState } from 'react'
// import axios from 'axios'
import React from 'react';
import  { Important } from './Important';
import { Home } from './Home';

function App() {
  const [isHomePage, setisHomepage] = React.useState(true)

  return (
    <>

      {isHomePage ? (<>
        <Home />
        <button onClick={(e) => setisHomepage(!isHomePage)}>Call Api</button>
      </>) : <Important />}


    </>
  );


}

export default App;