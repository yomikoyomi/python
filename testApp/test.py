# -*- coding: utf-8 -*-

# インポート
from bottle import route, run, template

# ルーティング
@route('/hello')
def hello():
    return template('Hello {{string}}',
                    string='World')

@route('/greeting/<name>')
def greeting(name):
    return template('Hello {{name}}.',
                    name=name)

@route('/article/<id:int>')
def article(id):
    return template('id={{id}}',
                    id=id)

@route('/article/<no:float>')
def article(no):
    return template('no={{no}}',
                    no=no)

@route('/article/<image_path:path>')
def article(image_path):
    return template('image_path={{image_path}}',
                    image_path=image_path)

@route('/search/<keyword:re:[a-z]+>')
def search(keyword):
    return template('keyword={{keyword}}',
                    keyword=keyword)

# サーバ起動
if __name__ == '__main__':
    run(host='localhost', port=4080,
        debug=True, reloader=True)
