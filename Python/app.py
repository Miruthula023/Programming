from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username')
    return render_template('display.html', name=name)

if __name__ == '__main__':
    app.run()
