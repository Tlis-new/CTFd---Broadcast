import websocket
from CTFd.models import *
def broadcast(noti):
	notifi = Notification()
	notifi.content = noti
	db.session.add(notifi)
	db.session.commit()
	ws = websocket.WebSocket()
	ws.connect("ws://45.63.122.81:8881")
	data = {'noti':noti,'action':'5hKhnlBxkPQkuGAqN6k1ksR3yfgNtQTHA2LwtykKZcGAfe5a0EhXh79hgRGb62fWcEBwfj8E5infOb5M5QtuE','token':'5YQfIYMy3UwbYPwqF13r3QqBWLmoOXiFsMBRvQl13x73iuwlgXheuvP8KxfguZUrWhGpiIDo2yLNuWm0TPSQbrhktZX0Z3gP17NSh4R8l3Eu5hI7CwG0GF'}
	data = json.dumps(data)
	ws.send(data)
