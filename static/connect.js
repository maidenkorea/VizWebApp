console.log("attempting socket connection to server...");

var socketio = io();
var video = document.querySelector("#videoElement");
const constraints = {
  audio: false,
  video: {
    width: 640,
    height: 480,
    frameRate: { ideal: 10, max: 15 },
    facingmode: "environment",
  },
};

socketio.on("connect", () => {
  console.log("connected!");

  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function (stream) {
        video.srcObject = stream;
      })
      .catch(function (e) {
        console.log("error capturing video.");
      });
  } else {
    console.log("error detecting camera.");
  }
});

socketio.on("disconnect", () => {
  console.log("disconnected!");
});
