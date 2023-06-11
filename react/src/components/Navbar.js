import React from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


const CustomNavbar = () => {
    return (
        <Navbar collapseOnSelect expand="lg" className='' variant='dark' bg='dark'>
          <Container>
            <Navbar.Brand href="/">
                <img src="logo-ponthe.png" height="40px"/>
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="#features">Galeries</Nav.Link>
                <Nav.Link href="#pricing">Équipe</Nav.Link>
                <Nav.Link href="#pricing">Matériel</Nav.Link>
              </Nav>
              <Nav>
                <Nav.Link href="#deets">Connexion</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      );
    }
export default CustomNavbar;