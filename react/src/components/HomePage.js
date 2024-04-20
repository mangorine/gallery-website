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
                <a className="big-button ytb-btn" href="https://www.youtube.com/@ponthe-ecoledesponts7542">Voir notre chaine Youtube</a>
                <a name="team"></a>
                <span className="team-down"><KeyboardDoubleArrowDownIcon/>Ponthé 026<KeyboardDoubleArrowDownIcon/></span>
            </div>
            <Container fluid>
                <Row>
                    <Col xs="12" sm="6" md="8" lg="8">
                        <img className="img-team" src="/static/assets/img/026_group.jpg"/>
                    </Col>
                    <Col xs="12" sm="6" md="4" lg="4">
                        <div className="team-desc">
                            <h2>L'équipe</h2>
                            <p>Président: Paul Tritz-Heid</p>
                            <p>V-Prez Photo: Aglaé Ténèze</p>
                            <p>V-Prez Vidéo: Paulin Courbon</p>
                            <p>Trez: Paul Saurin</p>
                            <p>Respo Matos: Jonathan Remy</p>
                            <p>Respo Galeries: Kenji Chikhaoui</p>
                            <p>Vidéastes: Martin Barrault, Damien Galbrun, Léo Wang</p>
                            <p>Photographes: Bastien Colleau, Albin Soleille, Gabriel Rogan, Hind Tanouti, Léa Woillez</p>
                        </div>
                    </Col>
                </Row>

            </Container>
        </>
    )
}
