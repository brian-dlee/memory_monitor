import tempfile

from flask import Flask, request, render_template, send_file
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
    start = None
    end = None

    if request.args.has_key('start'):
        start = int(request.args.get('start'))

    if request.args.has_key('end'):
        end = request.args.get('end')

    output = tempfile.NamedTemporaryFile('w', suffix=".png")
    generate_plot(request.args.get('pid'), output.name, start=start, end=end)

    return send_file(output.name, mimetype='image/png')


@app.route("/")
def get_viewer():
    return render_template('viewer.html')
