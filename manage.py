from flask_script import Manager, Server
from app import create_app


app = create_app()
manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=9888))

if __name__ == '__main__':
    manager.run()
