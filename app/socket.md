# About Sockets

## Flask-Socket-IO

### error handling

```py
socketio = SocketIO(logger=True, engineio_logger=True)
```

### `send()` vs `emit()`

```py
@socketio.on('message')
def handle_message(message):
    send(message, namespace='/chat')
```

```py
@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, namespace='/chat')

broadcast=True # comes from the backend
```

### Rooms
# ! difference between namespace and room?
```py
from flask_socketio import join_room, leave_room

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)
```


### Errorhandling
```py
@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass

@socketio.on_error('/chat') # handles the '/chat' namespace
def error_handler_chat(e):
    pass

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    pass
	```