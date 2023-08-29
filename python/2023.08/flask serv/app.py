from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask in Virtual Environment!'

@app.route('/commit')
def commit():
    return render_template('commit.html')

if __name__ == '__main__':
    app.run()

