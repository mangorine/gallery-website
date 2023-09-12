import React, {useState, useEffect, useRef} from 'react';
import './../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Cookies from 'js-cookie';
import CustomNavbar from './Navbar';
import PictureMosaic from './PictureMosaic';

export default function Gallery({props}){

  const [touchStart, setTouchStart] = useState(null)
  const [touchEnd, setTouchEnd] = useState(null)

  // the required distance between touchStart and touchEnd to be detected as a swipe
  const minSwipeDistance = 50

  const onTouchStart = (e) => {
    setTouchEnd(null) // otherwise the swipe is fired even with usual touch events
    setTouchStart(e.targetTouches[0].clientX)
  }

  const onTouchMove = (e) => setTouchEnd(e.targetTouches[0].clientX)

  const onTouchEnd = () => {
    if (!touchStart || !touchEnd) return
    const distance = touchStart - touchEnd
    const isLeftSwipe = distance > minSwipeDistance
    const isRightSwipe = distance < -minSwipeDistance
    if (isLeftSwipe){
      nextPicture()
    } else if (isRightSwipe){
      previousPicture()
    }
  }

    //Modal open state
    const [state, setState] = useState(false);
    //Current loaded picture in modal
    const [current, setCurrent] = useState(null);
    const [picsList, setPicsList] = useState([]);
    const [pics, setPics] = useState([]);
    const [name, setName] = useState('');
    const [result, setResult] = useState([]);
    //List of picture in the gallery

    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken') },
      body: JSON.stringify({ slug: gallery_slug })
    };

    //Open image in full screen when vignette is clicked
    const toggleModal = (e, img) => {
      setCurrent(img)
      setState(true)
    };

    //Close image modal
    const closeModal = () => {
      setState(false)
    };

    //Goto next picture in modal
    const nextPicture = () => {
      console.log(pics)
      let nextId = pics.indexOf(current)+1;
      if(nextId == pics.length) nextId = 0
      setCurrent(pics[nextId]);
    };

    //Goto previous picture in modal
    const previousPicture = () => {
      let nextId = pics.indexOf(current)-1;
      if(nextId == -1) nextId = pics.length-1
      setCurrent(pics[nextId]);
    };

    useEffect(() => {
      let picsDiv = []
      let picsTemp = []
      fetch('/api/gallery/pics/', requestOptions)
            .then(res => res.json())
            .then(
              (result) => {
                setResult(result)
              },
              (error) => {
                console.log(error)
              }
            );
          fetch('/api/gallery/', requestOptions)
            .then(res => res.json())
            .then(
              (result) => {
                setName(result.name)
              },
              (error) => {
                console.log(error)
              }
            );
    }, [])

    const ref = useRef(null);
    const ref2 = useRef(null);
    const ref3 = useRef(null)
    const ref4 = useRef(null)

    useEffect(() => {
            const handleClickOutside = (event) => {
              if (ref.current && !ref.current.contains(event.target)
                && ref2.current && !ref2.current.contains(event.target)
                && ref3.current && !ref3.current.contains(event.target)
                && ref4.current && !ref4.current.contains(event.target)) {
                closeModal()
              }
            };
            document.addEventListener('click', handleClickOutside, true);
            return () => {
              document.removeEventListener('click', handleClickOutside, true);
            };
          },[]);

    return (
      <>
      <CustomNavbar/>
        <div className="introductive-content">
          <h2 className="gallery-title">{name}</h2>
        </div>
        <PictureMosaic result={result}/>
      </>


      );
    }
