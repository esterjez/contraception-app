import pandas as pd
from flask import Flask, render_template
print("✅ pandas and flask are working!")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adolescents')
def adolescents():
    return render_template('subpage1.html')

@app.route('/regions')
def regions():
    return render_template('subpage2.html')

if __name__ == '__main__':
    app.run(debug=True)
