import React, { useEffect, useState, useRef} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import GallerySticker from './GallerySticker'
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import DownloadIcon from '@mui/icons-material/Download';

const PictureMosaic = (props) => {

    const [picsList, setPicsList] = useState([]);
    const [state, setState] = useState(false);
    //Current loaded picture in modal
    const [current, setCurrent] = useState(null);
    const [pics, setPics] = useState([]);

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
        let nextId = pics.indexOf(current) + 1;
        if (nextId == pics.length) nextId = 0
        setCurrent(pics[nextId]);
    };

    //Goto previous picture in modal
    const previousPicture = () => {
        let nextId = pics.indexOf(current) - 1;
        if (nextId == -1) nextId = pics.length - 1
        setCurrent(pics[nextId]);
    };

    useEffect(() => {
        const picsTemp = []
        const picsDiv = []
        for (const pic in props.result) {
            picsTemp.push(props.result[pic].link + '/uploads/' + props.result[pic].file_full_name)
            picsDiv.push(
                <Col key={pic} xs="12" sm="6" md="4" lg="2">
                    <GallerySticker img={props.result[pic].link + '/uploads/' + props.result[pic].file_full_name}
                        thumb={props.result[pic].link + '/thumbnails/' + props.result[pic].file_full_name}
                        modal_func={toggleModal} />
                </Col>
            )
        }
        setPicsList(picsDiv)
        setPics(picsTemp)
    }, [props.result]);

    useEffect(() => {
        const handleClickOutside = (event) => {
          if (ref.current && !ref.current.contains(event.target)
            && ref2.current && !ref2.current.contains(event.target)
            && ref3.current && !ref3.current.contains(event.target)
            && ref4.current && !ref4.current.contains(event.target)) {
            closeModal()
          }
        };
        document.addEventListener('click', handleClickOutside, true);
        return () => {
          document.removeEventListener('click', handleClickOutside, true);
        };
      },[]);
    const ref = useRef(null);
    const ref2 = useRef(null);
    const ref3 = useRef(null)
    const ref4 = useRef(null)

    return (
        <>
            <Container fluid>
                <Row className='g-1'>
                    {picsList}
                </Row>
            </Container>
            {state && (
                <div className='pic-modal'>
                    <ArrowBackIcon ref={ref2} onClick={previousPicture} className='arrow left-arrow' />
                    <ArrowForwardIcon ref={ref3} onClick={nextPicture} className='arrow right-arrow' />
                    <div className="pic-modal-nav">
                        <span className='close' onClick={closeModal}>&times;</span>
                        <a href={current} download={current}><span ref={ref4}><DownloadIcon className="download" /></span></a>
                    </div>
                    <div className='pic-modal-content'>
                        <div ref={ref} className="img-browser">
                            <img src={current} className='img-modal' />
                        </div>
                    </div>
                </div>
            )
            }
        </>
    );
};

export default PictureMosaic;