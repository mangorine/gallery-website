import React, {useState} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Col from 'react-bootstrap/Col';

const GalleryLink = (props) => {
    return(
        <>
          <Col xs="12" sm="6" md="4" lg="3">
          <div className='img-foreground'>
              <a href={props.link}>
                <img src={props.sticker} width="100%"/>
              </a>
            </div>
          </Col>
        </>
    );
};

export default GalleryLink;