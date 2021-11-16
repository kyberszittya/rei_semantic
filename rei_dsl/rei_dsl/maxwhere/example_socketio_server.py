import socketio

def main():
    # create a Socket.IO server
    sio = socketio.Server()

    # wrap with ASGI application
    app = socketio.ASGIApp(sio)
    sio.emit('hello', {'data': 'foobar'})


if __name__=="__main__":
    main()