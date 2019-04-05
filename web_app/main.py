from flask import Flask
from flask import render_template
from flask import ( request )

app = Flask(__name__)

@app.route('/')
def read():
    return render_template('poem.html')

@app.route('/interp')
def interpret():
    return render_template('interpretation.html')

if __name__ == "__main__":
    app.run(debug=True)