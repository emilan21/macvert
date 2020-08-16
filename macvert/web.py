# web.py - Flash ui

import os
import requests
from flask import Flask, render_template, request
from macvert.logic import convert_mac

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	errors = []
	results = {}
	conmacs = []
	macs = []
	if request.method == "POST":
		# Get Mac Addresses
		try:
			macs.append(request.form['macs'])
			input_type = request.form['input_type']
			output_type = request.form['output_type']
			conmacs.append(convert_mac(macs, input_type, output_type))
		except:
			errors.append(
				"Unable to get mac addresses. Please try again.")
		
	return render_template('index.html', errors=errors, results=results, conmacs=conmacs)
