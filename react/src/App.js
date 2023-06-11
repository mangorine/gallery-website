import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import CustomNavbar from './components/Navbar';
import Gallery from './components/Gallery';

function App() {
  return (
    <div className="App">
      <CustomNavbar />

      <Row className='g-0'>
        <Col xs="12" sm="6" md="4" lg="3">
        <div className='img-foreground'>
            <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
          </div>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
          <div className='img-foreground'>
            <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
          </div>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        <Col xs="12" sm="6" md="4" lg="3">
        <a href="/galerie/10">
              <img src="/test1.jpg" width="100%"/>
            </a>
        </Col>
        </Row>
        <Gallery/>

      </div>
  );
}

export default App;
