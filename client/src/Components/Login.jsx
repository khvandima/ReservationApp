import React, {useState} from 'react';

const DivWrapper = styled.div`
    display: flex;
    justify-content: space-between;
    background-color: #1E1F21;
    color: #DCDDDD;
    padding: 16px;
`;

function Login() {

const [username, setUsername] = useState("")
const onChange = (e) => {
    setUsername(e.target.value);
  };
  return (
    <DivWrapper>
        <label>username</label>
        <input onChange={onChange} value={username}/>
        <input />
        <button>Login</button>
    </DivWrapper>
  );
}

export default Login;
