from . import main


@main.route('/hello', methods=['GET', 'POST'])
def hello_page():
    return 'Hello World'
