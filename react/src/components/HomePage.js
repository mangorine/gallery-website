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
                        <img className="img-team" src="/static/assets/img/027_group.jpg"/>
                    </Col>
                    <Col xs="12" sm="6" md="4" lg="4">
                        <div className="team-desc">
                            <h2>L'équipe</h2>
                            <p>Président: Malak Hossainy</p>
                            <p>V-Prez Photo: Maxime Tran</p>
                            <p>V-Prez Vidéo: Alexandre Echevin</p>
                            <p>Trez: Flavie Hy</p>
                            <p>Respo Matos: Clement Lin</p>
                            <p>Respo Galeries: Clement Lin</p>
                            <p>Vidéastes: Paulo Wiplier, Camille Laurichesse, Omar Toufelaz, Elsa Pilz</p>
                            <p>Photographes: Arthur Claveau, Saer Basse, Marick Jolivot, Clement Desbois, Faustine Delorme</p>
                        </div>
                    </Col>
                </Row>

            </Container>
        </>
    )
}

