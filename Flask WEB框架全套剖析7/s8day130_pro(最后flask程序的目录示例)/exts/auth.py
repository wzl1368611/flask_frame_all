from flask import request,session,redirect

class Auth(object):

    def __init__(self,app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self,app):
        app.auth_manager = self

        self.app = app
        app.before_request(self.check_login)
        app.context_processor(self.context_processor)

    def check_login(self):
        """
        检查用户是否已经登录
        :return:
        """
        if request.path == '/login':
            return

        user = session.get('user')
        if not user:
            return redirect('/login')

    def context_processor(self):
        user = session.get('user')
        return dict(current_user=user)

    def login(self,data):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        session['user'] = data

    def logout(self):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        del session['user']
