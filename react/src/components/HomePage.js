import React from 'react'
import CustomNavbar from './Navbar'
import KeyboardDoubleArrowDownIcon from '@mui/icons-material/KeyboardDoubleArrowDown';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './../App.css';

export default function HomePage (){



    return (
        <>
            <CustomNavbar/>
            <div className="main-intro-div">
                <a className="big-button" href="/galleries">Accéder aux galeries</a>
                <span className="team-down"><KeyboardDoubleArrowDownIcon/>Ponthé 025<KeyboardDoubleArrowDownIcon/></span>
            </div>
            <Container fluid>
                <Row>
                    <Col xs="12" sm="6" md="8" lg="8">
                        <img className="img-team" src="/static/assets/img/025_group.jpg"/>
                    </Col>
                    <Col xs="12" sm="6" md="4" lg="4">
                        <div className="team-desc">
                            <h2>L'équipe</h2>
                            <p>Président: Cyril Possard</p>
                            <p>V-Prez Photo: Benjamin Pic</p>
                            <p>V-Prez Vidéo: Loys Duponchel</p>
                            <p>Respo Comm: Antoine De Solages</p>
                            <p>Respo Matos: Quentin Laugier</p>
                            <p>Respo Galeries: Alexandre Ducorroy</p>
                            <p>Relations externes: Damien Galbrun</p>
                            <p>Reltions internes/Trez: Paul Rosener</p>
                            <p>Vidéastes: Guillaume Bieth, Erwann Estève, Raphael Moreaux, Gabriel Tang, Gautier Michel, Jean-Marie Sleiman</p>
                            <p>Photographes: Bastien Lemée, Sixtine Nodet, Hugo Guastalla, Vincent Gefflaut, Mohammed Yacine Babi, Timothée Rigagneau, Barbara Quint</p>
                        </div>
                    </Col>
                </Row>
               
            </Container>
        </>
    )
}