import React, {useState} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';
import Cookies from 'js-cookie';

export default function Login() {

    const cookie = Cookies.get('csrftoken')

    return (
        <>
            <Container>
                <Row className="justify-content-center">
                    <Col lg="5" sm="12" md="8">
                        <div className="login-container">
                            <img className="login-logo" src="/static/assets/img/logo-ponthe.png"/>
                            <form className="login-form" method="post" action="/login/">
                                <input type="hidden" name="csrfmiddlewaretoken" value={cookie} />
                                <input type="email" className="login-input" placeholder="prenom.nom@eleves.enpc.fr" name="username"required/>
                                <input type="password" className="login-input" placeholder="Mot de passe" name="password" required/>
                                {error && <p className="login-error">Mauvais identifiants</p>}
                                <button type="submit" className="login-button">Se connecter</button>
                            </form>
                            <a href="/accounts/login" className="login-link">Connexion SSO</a>
                        </div>
                    </Col>
                </Row>
            </Container>
        </>
    )

}