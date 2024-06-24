# web.py - Flash ui

import os
import requests
from flask import Flask, render_template, request
from logic import convert_mac

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    conmacs = []
    if request.method == "POST":
        # Get Mac Addresses
        try:
            mac_list = list(request.form['macs'].split("\r\n"))
            input_type = request.form['input_type']
            output_type = request.form['output_type']
            conmacs.append(
                convert_mac(mac_list, input_type, output_type))
        except:
            errors.append("Unable to get mac addresses. Please try again.")

    return render_template('index.html',
                           errors=errors,
                           results=results,
                           conmacs=conmacs[0])
