import React, {useState, useEffect} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Cookies from 'js-cookie';
import GalleryLink from './GalleryLink';

export default function Gallery(){
    const [galleriesComp, setGalleriesComp] = useState([]);
    const requestOptions = {
        method: 'GET',
        headers: { 
          'Content-Type': 'application/json',
          'X-CSRFToken': Cookies.get('csrftoken') },
      };
    useEffect(() => {
        let galleriesTemp = []
        let compTemp = []
        fetch('/api/galleries', requestOptions)
              .then(res => res.json())
              .then(
                (result) => {
                  for(const pic in result){
                    galleriesTemp.push(result[pic])
                  }
                  galleriesTemp.forEach((gal, index) =>{
                    compTemp.push(<GalleryLink key={gal.id} link={'/gallery/' + gal.id} sticker={gal.sticker_url} title={gal.name}/>)
                  })
                  setGalleriesComp(compTemp)
                },
                (error) => {
                  console.log(error)
                }
              );
          
      }, [])
      

    return(
        <Row className='g-0'>
            {galleriesComp}
        </Row>
    )
}
