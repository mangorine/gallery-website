import React, {useState, useEffect} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Row, Container, Col } from 'react-bootstrap';
import Cookies from 'js-cookie';
import CustomNavbar from './Navbar'
import {Select, MenuItem} from '@mui/material';
import GalleryMosaic from './GalleryMosaic';

export default function Gallery(props) {
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
  console.log(props.view)
  useEffect(() => {
    fetch('/api/get_view?view=' + props.view, requestOptions)
      .then(res => res.json())
      .then(
        (result) => {
          setResult(result)
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
        },
        (error) => {
          console.log(error)
        }
      );
  }, [])

  return (
      <>
        <CustomNavbar/>
        <Container>
          <Row>
          <Col xs="12" sm="6" md="4" lg="2">
          <Select style={{marginTop: '100px', marginBottom: '40px', width: '100%', padding:0, height: "40px"}} value={year} onChange={e =>
                {
                    setYear(e.target.value)
                }} label="Année">
                    {menuComponents}
        </Select>
        </Col>
          </Row>
        </Container>
        <GalleryMosaic result={result} year={year}/>
      </>
    )
}
