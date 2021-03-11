from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title_web>')
def index(title_web):
    return render_template('/static/html/index.html', title=title_web)
 
            


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')