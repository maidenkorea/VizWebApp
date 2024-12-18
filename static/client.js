console.log("attempting socket connection to server...");

const socket = io();

const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const constraints = {
  audio: false,
  video: {
    width: 640,
    height: 480,
    frameRate: { ideal: 10, max: 15 },
    facingmode: "environment",
  },
};

socket.on("connect", () => {
  console.log("connected!");
  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function (stream) {
        video.srcObject = stream;
        setInterval(function () {
          ctx.drawImage(video, 0, 0, 640, 480);
          const frame = canvas.toDataURL("image/jpeg", 1);
          socket.emit("frame", frame);
        }, 3000);
      })
      .catch(function (e) {
        console.log("error capturing video: ", e);
      });
  } else {
    console.log("error detecting camera.");
  }
});

socket.on("disconnect", () => {
  console.log("disconnected!");
});

socket.on("result", () => {
  var container = document.getElementById("img");
  var content = container.innerHTML;
  container.innerHTML = content;
});
