from s8day130_pro import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


app = create_app()
manager = Manager(app)



Migrate(app, db)
"""
# 数据库迁移命名
    python manage.py db init
    python manage.py db migrate # makemigrations
    python manage.py db upgrade # migrate
"""
manager.add_command('db', MigrateCommand)




@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)


@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令
    执行： python manage.py  cmd -n wupeiqi -u http://www.oldboyedu.com
    执行： python manage.py  cmd --name wupeiqi --url http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


if __name__ == '__main__':
    # app.run()
    manager.run()