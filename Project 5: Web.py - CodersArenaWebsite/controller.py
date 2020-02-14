"""
This is Our Controller. Basically this is the heart of the project because it holds all the models and view together.
All the routes and classes are defined in here.
"""

import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

# All the routes for our websites are defined here
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/logout', 'Logout',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity'
)

# Start the instance of our web app
app = web.application(urls, globals())

# Creating a session for an emtpy user at start, once the user logs in sssion obejct will be updated

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})
session_data = session._initializer

render = web.template.render('Views/Templates', base='MainLayout', globals={'session': session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        data = type('obj', (object,), {'username': 'Frankiii', 'password': 'sanket'})
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)
        if isCorrect:
            session_data['user'] = isCorrect
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class CheckLogin:
    def POST(self):
        # To take the input from html form
        data = web.input()

        # Here we will make a call to out model LoginModel.py inside that we will call LoginModel class
        login = LoginModel.LoginModel()

        # we will compare the entered password with the password which is stored inside th database
        isCorrect = login.check_user(data)

        # if password is correct then establish a login session and return it
        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect

        # otherwise return error
        return 'error'


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return 'success'


class PostRegistration:
    def POST(self):
        data = web.input()

        # Here we will make a call to out model RegisterModel.py inside that we will call RegisterModel class
        reg_model = RegisterModel.RegisterModel()

        # Using insert user we will create a new entry to the data base for this user who registers
        reg_model.insert_user(data)
        return data.username


class PostActivity:
    def POST(self):
        data = web.input()

        # We need to store posts with every user's name to tell who posted what
        data.username = session_data['user']['username']

        # Here we will make a call to out model Posts.py inside that we will call Posts class
        post_model = Posts.Posts()
        post_model._insert_post(data)
        return 'success'


if __name__ == '__main__':
    app.run()
