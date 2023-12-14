# RuHuman Audio Verification UI Implemented in Python Flask

# Libraries 
from flask import Flask, redirect, url_for, render_template, request, send_file
import daps
import os
import time


# Creating the app 
app = Flask(__name__)

# Landing Page
@app.route("/")
def home():
	return render_template('index.html')

@app.route("/upload",methods=["POST","GET"])
def upload():
	if request.method == "POST": 
		audio = request.files['upload']
		name = request.form['filename']
		detector = request.form['detectors']
		if not audio or not name:
			return render_template('noaudio.html')
		if(not os.path.exists(os.getcwd() + '\\results')):
			os.makedirs(os.getcwd() + '\\results')
		name = name.replace(' ','_')
		path = f'./results/{name}'
		audio.save(path)
		wavPath = daps.inputToWav(path)
		wavName = os.path.basename(wavPath)
		start = time.time()
		probAI = daps.sendToDetector(wavPath,detector)
		duration = time.time() - start
		melPlotPath = daps.plotMelSpectrogram(wavPath)
		nl = '\n'
		html = f"<link rel=\"stylesheet\" href=\"../static/style.css\"/><h1 style='font-family:Courier'>Your Uploaded Audio Sample: ({wavName})</h1>{nl}<br>{nl}" 
		html = html + f"<a href={wavPath}><audio controls title={wavName}><source src={wavPath}></audio></a>"
		html = html + f"<h2>Features:</h2><img width='50%' src='{melPlotPath}'' />"
		html = html + f"<h2>Detector Model: {detector} (Detected in {duration:.2f} seconds)"
		html = html + f"<h2>Probablity of Being Spoofed by Generative AI via {detector} Model: {probAI:.2f}%"
		html = html + f"<h1><a href='/'>Return to Homepage</a></h1>{nl}"
		html = html + f"<img id='favicon' src='../static/favicon.png'>"
		return html
	else:
		return redirect(url_for('home'))

@app.route("/clear")
def clear():
	try:
		for file in os.listdir('./results'):
			os.remove(os.path.join('./results',file))
		nl = '\n'
		return f'<script>{nl}alert("Cleared Results");{nl}window.location.href="/";{nl}</script>'
	except FileNotFoundError:
		return 'No Results'
		
@app.route("/results/<name>")
def results(name):
	path = f'./results/{name}' 
	return send_file(path,mimetype='audio')

# Debug if the same file as run
if __name__ == "__main__":
	clear()
	if(os.path.exists('cert.pem') and os.path.exists('key.pem')): # Run as https
		app.run(debug=True,host='0.0.0.0',port=8080,ssl_context=('cert.pem', 'key.pem'))
	else: 
		print("RuHuman Flask Server missing cert.pem and key.pem files. Please generate them in OpenSSL for full functionality.")
		app.run(debug=True,host='0.0.0.0',port=8080)