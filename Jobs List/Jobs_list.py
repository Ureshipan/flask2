from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>')
def list_prof(list):
    jobs_list = ['Dungeon Master', 'Boss of the gym', 'Slave']
    return render_template('jobs.html', list=list, jobs=jobs_list)
 
            


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')