import {React, useState} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Col from 'react-bootstrap/Col';

const GallerySticker = (props) => {
    return(
        <div className='gallery-sticker'>
            <div className="gallery-sticker" onClick={(event) => props.modal_func(event, props.img)}>
                <img src={props.img} width="100%"/>
            </div>
        </div>
    );
};

export default GallerySticker;