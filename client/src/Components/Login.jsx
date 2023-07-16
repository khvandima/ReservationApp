import React, {useState} from 'react';

function Login() {

const [username, setUsername] = useState("")
const onChange = (e) => {
    setUsername(e.target.value);
  };
  return (
    <div className="App">
        <label>username</label>
        <input onChange={onChange} value={username}/>
    </div>
  );
}

export default Login;
