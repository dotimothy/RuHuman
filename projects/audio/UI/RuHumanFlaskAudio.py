# RuHuman Audio Verification UI Implemented in Python Flask

# Libraries 
from flask import Flask, redirect, url_for, render_template, request, send_file
import os


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
		if not audio or not name:
			return render_template('noaudio.html')
		if(not os.path.exists(os.getcwd() + '\\results')):
			os.makedirs(os.getcwd() + '\\results')
		name = name.replace(' ','_')
		path = f'./results/{name}'
		audio.save(path)
		nl = '\n'
		html = f"<h1 style='font-family:Courier'>Your Uploaded Audio ({name})</h1>{nl}<br>{nl}" 
		html = html + f"<a href={path}><audio controls title={name}/><source src={path}></audio></a>"
		html = html + f"<h1 style='font-family:Courier'><a href='/'>Return to Homepage</a></h1>{nl}"
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
	app.run(debug=True,host='0.0.0.0',port=8080)
