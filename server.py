import zmq

# Establish server connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

# Start game time at 12:00 PM (noon)
game_hour = 12

# Loop to receive requests
while True:
    try:
        message = socket.recv_json()

        # Error: Empty message
        if not message:
            reply = {'Error': 'Request must include action'}

        # Shut down server
        elif message.get('request') == 'Q':
            reply = {'Status': 'Shutting down'}
            socket.send_json(reply)
            break

        # Get current game time
        elif message.get('request') == 'get_time':
            reply = {'Game Time': f'{game_hour}:00'}

        # Shift game time
        elif message.get('request') == 'shift_time':
            hours = message.get('hours')
            if isinstance(hours, int) and hours >= 0:
                game_hour = (game_hour + hours) % 24
                reply = {'NewTime': f'{game_hour}:00'}
            else:
                reply = {'Error': 'Invalid hours value'}

        else:
            reply = {'Error': 'Unknown request'}

    except Exception as e:
        reply = {'Error': str(e)}

    socket.send_json(reply)
