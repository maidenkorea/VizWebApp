'use strict';
console.log('start video capture script.')

const constraints = { 
    audio: false,
    video: { 
        width: 640,
        height: 480,
        frameRate: { ideal: 10, max: 15 },
        facingmode: "environment"
    },
}