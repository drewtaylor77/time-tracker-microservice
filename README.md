# Game Time Tracker

A Python-based microservice capable of receiving requests to retrieve and advance in game time through TCP connections set up via ZeroMQ after the user performs an action.

### How It Works

The microservice runs as a server using ZeroMQ REP socket.

   * It listens for incoming time requests via a TCP server connection.
   * It maintains the current game time in an hourly format (e.g. `3:00`, `18:00`).
   * It can shift the time forward by a specified number of hours.

### Request formats
All requests must be in valid JSON format.

| Request  | Return/Action                      |
|----------|------------------------------------|
| `{'request': 'Q'}` | Break communication and shut down the server |
| `{'request': 'get_time'}` | Returns the current game time |
| `{'request': 'shift_time', 'hours': 'int value'}` | Shifts game time and returns confirmation |

### Making a Request

1. Establish a ZeroMQ context object
2. Create a socket w/ the context & establish connection on the host and port with 'socket = context.socket(zmq.REQ)'
   * connection is currently set to target "tcp://localhost:5555"
3. Create a valid JSON object in a format listed in the table above.
4. Send the request via 'socket.send_json()'

#### Example Request
```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Get current game time
socket.send_json({'request': 'get_time'})

# Shift game time by 5 hours
socket.send_json({'request': 'shift_time', 'hours': 5})
```

### Receiving a Response

After having received the request, assign a variable equal to 'socket.recv()'; it will generate a quote and send it back to the client.

#### Example of Receiving
```python
# Get current game time
message = socket.recv_json()
print(f'Current Game Time: {message}')

# Shift game time by 5 hours
message = socket.recv_json()
print(f'New Game Time: {message}')
```

The response is formatted as follows:

```python
# Get current game time
{'Game Time': '15:00'}

# Shift game time
{'New Time': '20:00'}

# Errors
{'Error': 'Invalid hours value'}
```

## Tech Stack

Python 3.13

ZeroMQ (pyzmq) — Microservice communication

### Author

Andrew Taylor
