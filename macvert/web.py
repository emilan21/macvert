"""Optional local Flask interface."""

from flask import Flask, render_template, request

from macvert.logic import convert_mac
from macvert.mac_operations import FORMATS

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    converted = []
    if request.method == "POST":
        try:
            input_type = request.form["input_type"]
            output_type = request.form["output_type"]
            if input_type not in FORMATS or output_type not in FORMATS:
                raise ValueError("Unknown MAC address format")
            addresses = request.form["macs"].splitlines()
            converted = convert_mac(addresses, input_type, output_type)
        except (KeyError, ValueError) as error:
            errors.append(str(error))
    return render_template("index.html", errors=errors, results={}, conmacs=converted)
