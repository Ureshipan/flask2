from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    
    user = User()
    user.name = "Ridley"
    user.surname = "Scott"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    
    user = User()
    user.name = "Ureshipan"
    user.surname = "Albedo"
    user.age = 17
    user.position = "officer"
    user.speciality = "engineer"
    user.address = "module_3"
    user.email = "albed.ureshi@genshin.com"
    db_sess = db_session.create_session()
    db_sess.add(user)
    
    user = User()
    user.name = "Gladrax"
    user.surname = "Kotran"
    user.age = 16
    user.position = "officer"
    user.speciality = "gay"
    user.address = "module_3"
    user.email = "gladkat@ya.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    
    db_sess.commit()    
    #app.run()


if __name__ == '__main__':
    main()