import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Get current game time
socket.send_json({'request': 'get_time'})
message = socket.recv_json()
print(f'Current Game Time: {message}')

# Shift game time by 5 hours
socket.send_json({'request': 'shift_time', 'hours': 5})
message = socket.recv_json()
print(f'New Game Time: {message}')

# Shut down server
socket.send_json({'request': 'Q'})
message = socket.recv_json()
