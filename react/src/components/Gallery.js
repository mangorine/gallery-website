import React, {useState, useEffect} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import DownloadIcon from '@mui/icons-material/Download';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import GallerySticker from './GallerySticker'
import Cookies from 'js-cookie';

export default function Gallery({props}){

    //Modal open state
    const [state, setState] = useState(false);
    //Current loaded picture in modal
    const [current, setCurrent] = useState(null);
    const [picsList, setPicsList] = useState([]);
    const [pics, setPics] = useState([]);
    //List of picture in the gallery

    const requestOptions = {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken') },
      body: JSON.stringify({ id: gallery_id })
    };

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
      console.log(pics)
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

    useEffect(() => {
      let picsDiv = []
      let picsTemp = []
      fetch('/api/gallery/pics/', requestOptions)
            .then(res => res.json())
            .then(
              (result) => {
                for(const pic in result){
                  picsTemp.push(result[pic].link)
                }
                picsTemp.forEach((pic, index) =>{
                  picsDiv.push(<Col key={pic} xs="12" sm="6" md="4" lg="2">
                  <GallerySticker img={pic} modal_func={toggleModal}/>
                </Col>)
                })
                setPicsList(picsDiv)
                setPics(picsTemp)
                console.log(pics)
              },
              (error) => {
                console.log(error)
              }
            );
        
    }, [])
    
    return (
      <>
        <Row className='g-0'>
          {picsList}
        </Row>

        {state && (
          <div className='pic-modal'>
            <ArrowBackIcon onClick={previousPicture} className='arrow left-arrow'/>
            <ArrowForwardIcon onClick={nextPicture} className='arrow right-arrow'/>
            <div className="pic-modal-nav">
              <span className='close' onClick={closeModal}>&times;</span>
              <span><DownloadIcon className="download"/></span>
            </div>
            <div className='pic-modal-content'>
              <div className="img-browser">
                <img src={current} width="100%"/>
              </div>
            </div>
          </div>
          )
        }
      </>
      
      
      );
    }
