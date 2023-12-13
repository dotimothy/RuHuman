/* UI.js: RuHuman User Interface */
/* Author: Timothy Do */

// UI Variables
var recordOption = document.getElementById('recordAudio');
var uploadOption = document.getElementById('uploadAudio');
var audSrc = document.getElementById("audiosource");
var filename = document.getElementById("filename");
var preview = document.getElementById("preview");
var startRecord = document.getElementById("record");
var stopRecord = document.getElementById("stop");
var audioUpload = document.getElementById("audioupload");
var verifyAudio = document.getElementById("verifyAudio");

//Recorder Variables
var recorder;
window.onload = function() {
	navigator.mediaDevices.getUserMedia({
		audio: true
	})
	.then(function (stream) {
		recorder = new MediaRecorder(stream);
		recorder.addEventListener('dataavailable', pushRecordToPreview);
	});
}

//function for loading audio file for playback preview
function loadFile(event) {
	filename.value = event.target.files[0]["name"];
	preview.style.width = '25%';
	preview.src = URL.createObjectURL(event.target.files[0]);
	preview.hidden = false;
	audSrc.hidden = false;
	recordOption.hidden = true;
}

// Reset Audio Upload Preview
function resetPreview() {
	stopRecording();
	preview.hidden = true;
	audSrc.hidden = true;
	preview.src = '';
	filename.value = '';
	audioUpload.value = '';
	recordOption.hidden = false;
	uploadOption.hidden = false;
	startRecord.hidden = false;
	verifyAudio.hidden = false;
}

//Start Recording
function startRecording() {
	uploadOption.hidden = true;
	startRecord.hidden = true;
	stopRecord.hidden = false;
	verifyAudio.hidden = true;
  	recorder.start();
}

function startDelayRecording(delay) {
	setTimeout(startRecording,delay);
}

//Stops Records and Saves File to the Form to Upload
function stopRecording() {
	stopRecord.hidden = true;
	verifyAudio.hidden = false;
	recorder.stop();
}

function pushRecordToPreview(e) {
	const date = new Date(Date.now());
	filename.value = `${date.getFullYear()}${date.getMonth()}${date.getDay()}_${date.getHours()}${date.getMinutes()}${date.getSeconds()}.weba`;
	preview.style.width = '25%';
	preview.src = URL.createObjectURL(e.data);
	preview.hidden = false;
	audSrc.hidden = false;
	var file = new File([e.data],filename.value,{type:"audio/weba",lastModified:new Date().getTime()});
	var container = new DataTransfer();
	container.items.add(file)
	audioUpload.files = container.files;

}