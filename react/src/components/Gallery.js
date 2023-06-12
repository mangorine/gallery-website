import {React, useState} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import DownloadIcon from '@mui/icons-material/Download';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import GallerySticker from './GallerySticker'

const Gallery = (props) => {

    //Modal open state
    const [state, setState] = useState(false);
    //Current loaded picture in modal
    const [current, setCurrent] = useState(null);
    //List of picture in the gallery
    const pics = ['test1.jpg', 'test2.jpg', 'test3.jpg'];

    //Open image in full screen when vignette is clicked
    const toggleModal = (e, img) => {
      setCurrent(img)
      setState(true)
    };

    //Close image modal
    const closeModal = () => {
      setState(false)
    };

    //Goto next picture in modal
    const nextPicture = () => {
      let nextId = pics.indexOf(current)+1;
      if(nextId == pics.length) nextId = 0 
      setCurrent(pics[nextId]);
    };

    //Goto previous picture in modal
    const previousPicture = () => {
      let nextId = pics.indexOf(current)-1;
      if(nextId == -1) nextId = pics.length-1
      setCurrent(pics[nextId]);
    };

    return (
      <div>
        <Row className='g-0'>
          <Col xs="12" sm="6" md="4" lg="2">
            <GallerySticker img='test1.jpg' modal_func={toggleModal}/>
          </Col>
          <Col xs="12" sm="6" md="4" lg="2">
          <GallerySticker img='test2.jpg' modal_func={toggleModal}/>
          </Col>
          <Col xs="12" sm="6" md="4" lg="2">
          <GallerySticker img='test3.jpg' modal_func={toggleModal}/>
          </Col>
        </Row>
        {state && (
          <div className='pic-modal'>
            <ArrowBackIcon onClick={previousPicture} className='arrow left-arrow'/>
            <ArrowForwardIcon onClick={nextPicture} className='arrow right-arrow'/>
            <div class="pic-modal-nav">
              <span className='close' onClick={closeModal}>&times;</span>
              <span><DownloadIcon className="download"/></span>
            </div>
            <div className='pic-modal-content'>
              <div class="img-browser">
                <img src={current} width="100%"/>
              </div>
            </div>
          </div>
          )
        }
      </div>
      
      
      );
    }
export default Gallery;