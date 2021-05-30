"""
Create multiple routes with functions that require an input via the URL to return an output.

Flask Project. Created by Malia D'Mello, May 2021.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/temperature/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return "Your input value ({:.1f} celsius) is equivalent to {:.2f} fahrenheit.".format(float(celsius), fahrenheit)


if __name__ == '__main__':
    app.run()
