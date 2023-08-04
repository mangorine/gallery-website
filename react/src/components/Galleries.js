import React, {useState, useEffect} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Row, Container, Col } from 'react-bootstrap';
import Cookies from 'js-cookie';
import GalleryLink from './GalleryLink';
import CustomNavbar from './Navbar'
import {Select, MenuItem} from '@mui/material';

export default function Gallery() {
  const [galleriesComp, setGalleriesComp] = useState([]);
  const [menuComponents, setMenuComponents] = useState([]);
  const [year, setYear] = useState('');
  const [result, setResult] = useState([]);

  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': Cookies.get('csrftoken')
    },
  };
  useEffect(() => {
    fetch('/api/galleries', requestOptions)
      .then(res => res.json())
      .then(
        (result) => {
          setResult(result)
        },
        (error) => {
          console.log(error)
        }
      );
      fetch('/api/years', requestOptions)
      .then(res => res.json())
      .then(
        (result) => {
          let menuCompTemp = []
          for (const year in result) {
            menuCompTemp.push(<MenuItem value={result[year].name}>{result[year].name}</MenuItem>)
          }
          setMenuComponents(menuCompTemp)
          setYear(result[0].name)
        },
        (error) => {
          console.log(error)
        }
      );
  }, [])

  useEffect(() => {
    let galleriesTemp = []
    let compTemp = []
    for (const pic in result) {
      if(result[pic].year == year) 
        galleriesTemp.push(result[pic])
    }
    galleriesTemp.forEach((gal, index) => {
      compTemp.push(<GalleryLink key={gal.slug} link={'/gallery/' + gal.slug} sticker={gal.sticker_url} title={gal.name} />)
    })
    setGalleriesComp(compTemp)

  }, [year])


  return (
      <>
        <CustomNavbar/>
        <Container>
          <Row>
          <Col xs="12" sm="6" md="4" lg="2">
          <Select style={{marginTop: '100px', marginBottom: '40px', width: '100%', padding:0, height: "40px"}} value={year} onChange={e => 
                {
                    setYear(e.target.value)
                }} label="Visiblité">
                    {menuComponents}
        </Select>
        </Col>
          </Row>
        </Container>
        
        <Container fluid>
          <Row>
          
          </Row>
          <Row className="g-1">
          
              {galleriesComp}
          </Row>
        </Container>
      </>
    )
}
