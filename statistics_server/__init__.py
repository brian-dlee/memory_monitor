import os
import tempfile

from flask import Flask, request, render_template, send_file, jsonify
from flask_assets import Environment, Bundle

from plotter import generate_plot
from statistics_server import paths

app = Flask(__name__)
assets = Environment(app)

js = Bundle('js/main.js', filters="jsmin", output="bundle.js")
css = Bundle('css/main.css', filters="cssmin", output="bundle.css")
assets.register('javascript', js)
assets.register('stylesheets', css)
assets.url_expire = True
assets.debug = app.debug


@app.route("/get_plot")
def get_plot():
    pids = []
    start = None
    end = None

    if request.args.has_key('pid'):
        rawpid = request.args.get('pid')

        if rawpid.find(','):
            pids = rawpid.split(',')
        else:
            pids = [rawpid]

    if request.args.has_key('pids'):
        pids = request.args.has_key('pids')

    if len(pids) == 0:
        return "No PIDS or PID provided.", 400

    if request.args.has_key('start'):
        start = int(request.args.get('start'))

    if request.args.has_key('end'):
        end = int(request.args.get('end'))

    output = tempfile.NamedTemporaryFile('w', suffix=".png")
    generate_plot(pids, output.name, start=start, end=end)

    return send_file(output.name, mimetype='image/png')


@app.route("/pids")
def get_pids():
    return jsonify({
        "pids": [f.split('.')[0] for f in os.listdir(paths.DATA_DIR) if f.endswith('.txt')]
    })


@app.route("/")
def get_viewer():
    return render_template('viewer.html')
