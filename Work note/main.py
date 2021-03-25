from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, url_for, request, render_template, redirect
import datetime

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


    
@app.route('/')
@app.route('/index')
def journal():
    jobs = []
    session = db_session.create_session()
    for i in session.query(Jobs).all():
        jobs.append((i.job,
                     name(session, i.team_leader),
                     surname(session, i.team_leader),
                     i.work_size,
                     i.collaborators,
                     i.is_finished))
    session.close()
    params = {}
    print(jobs)
    params["title"] = "Журнал работ"
    #params["static_css"] = url_for('static', filename="css/")
    params["static_img"] = url_for('static', filename="img/")
    params["jobs"] = jobs
    return render_template("journal.html", **params)


def name(session, idd):
    for i in session.query(User).filter(User.id == idd):
        return i.name
    
def surname(session, idd):
    for i in session.query(User).filter(User.id == idd):
        return i.surname

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')