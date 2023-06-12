import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';
import CustomNavbar from './components/Navbar';
import Gallery from './components/Gallery';
import GalleryLink from './components/GalleryLink';

function App() {
  return (
    <div className="App">
      <CustomNavbar />

      <Row className='g-0'>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        <GalleryLink link='test1' sticker='test1.jpg' title='Test'/>
        </Row>
        <Gallery/>

      </div>
  );
}

export default App;
