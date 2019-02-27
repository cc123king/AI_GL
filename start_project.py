from app import app
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

if __name__=='__main__':
    try:
        http_server = WSGIServer(('0.0.0.0',8080),app)
        print('server at:http://0.0.0.0:8080/,use ctrl+c end server.')
        http_server.serve_forever()
        
    except KeyboardInterrupt as e:
        http_server.stop()
        print('close server.')
