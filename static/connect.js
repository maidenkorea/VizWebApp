console.log("attempting socket connection to server...");

var socket = io();

socket.on("connect", () => {
  console.log("connected!");
});

socket.on("disconnect", () => {
  console.log("disconnected!");
});
