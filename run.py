from waitress import serve
from pemweb import main
from pyramid.paster import get_app

if __name__ == '__main__':
    app = get_app('development.ini', 'main')
    serve(app, host='127.0.0.1', port=6543)
