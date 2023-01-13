import { Link } from 'react-router-dom';
import { BrowserRouter,Route,Routes } from 'react-router-dom';
import AddUi from './add';
import Add_attnUi from './add_attn';
import HomeUi from './home';
import LoginUi from './login';
import RegisterUi from './register';
import SeeUi from './see';
// const cors=require('cors')
// App.use(cors())
function App() {
  return (
  <BrowserRouter>
  <Routes>  
  <Route path="/" element={<HomeUi/>}/>
          <Route path="login" element={<LoginUi/>}/>
          <Route path="add_attn" element={<Add_attnUi/>}/>
          <Route path="register" element={<RegisterUi/>}/>
          <Route path="add" element={<AddUi/>}/>
          <Route path="see" element={<SeeUi/>}/>
        </Routes>

    </BrowserRouter>
  );
}

export default App;