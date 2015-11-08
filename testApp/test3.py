from bottle import route, run, template
import bottle
bottle.debug(True)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=4080, reloader=True)
