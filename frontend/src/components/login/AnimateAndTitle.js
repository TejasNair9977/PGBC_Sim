import React from 'react';
import classes from './animateAndTitle.module.css';
import ParticlesContainer from '../UI/Particles';
import lottie from '../../animation/lottie.json';
import { Player } from '@lottiefiles/react-lottie-player';

const AnimateAndTitle = () => {
  return (
    <>
      <ParticlesContainer />
      <div className={classes.animate}>
        <Player
          autoplay
          loop
          src={lottie}
          style={{ height: '500px', width: '700px' }}
        />
        <div>PGBC</div>
      </div>
    </>
  );
};

export default AnimateAndTitle;