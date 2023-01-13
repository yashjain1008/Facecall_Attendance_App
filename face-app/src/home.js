import './home.css';
import { Link } from 'react-router-dom';

function HomeUi() {
  return (
    <div className="main">
     <div className="sub-main">
       <div>
         <div>
           <h1>Facecall</h1>  
          <div className="login-button">
          <button><Link className="li" to="/login">Signin</Link></button>
          </div>
          <div className="register-button">
          <button><Link className="li" to="/register">Register</Link></button>
          </div>          
        </div>
       </div>
     </div>
    </div>
  );
}

export default HomeUi;