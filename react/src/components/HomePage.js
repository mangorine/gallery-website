import React from 'react'
import CustomNavbar from './Navbar'
import KeyboardDoubleArrowDownIcon from '@mui/icons-material/KeyboardDoubleArrowDown';

export default function HomePage (){



    return (
        <>
            <CustomNavbar/>
            <div className="main-intro-div">
                <a className="big-button" href="/galleries">Accéder aux galeries</a>
                <span className="team-down"><KeyboardDoubleArrowDownIcon/>Ponthé 025<KeyboardDoubleArrowDownIcon/></span>
            </div>
            <img className="img-team" src="/static/assets/img/025_group.jpg"/>
        </>
    )
}