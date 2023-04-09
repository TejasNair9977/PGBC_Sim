import React from 'react'
import classes from "./animateAndTitle.module.css"
import ParticlesContainer from '../UI/Particles'
import lottie from "../../animation/lottie.json"
import Lottie from 'react-lottie'

const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: lottie,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice"
    }
  }




const AnimateAndTitle = () => {
    return(<>
        <ParticlesContainer></ParticlesContainer>
        <div className={classes.animate}>
            <Lottie
                options={defaultOptions}
                height={500}
                width={700}
            /><div>My Health Tracker</div>

        </div>
    </>)
}


export default AnimateAndTitle;