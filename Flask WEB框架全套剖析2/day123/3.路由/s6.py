from flask import Flask,render_template,redirect
app = Flask(__name__)
app.config['SERVER_NAME'] = 'oldboy.com:5000'


@app.route("/dynamic", subdomain="<username>")
def xxxxxxx(username):
    print(username)
    return 'xxxxx'

if __name__ == '__main__':
    app.run()