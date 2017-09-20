from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def first():
    return "This is the first page!"

@my_app.route('/second')
def second():
    return "This is the second page!"

@my_app.route('/third')
def third():
    return "This is the third page!"

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

    
