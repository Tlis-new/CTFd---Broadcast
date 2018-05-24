import websocket
from CTFd.models import *
def broadcast(noti):
	notifi = Notification()
	notifi.content = noti
	db.session.add(notifi)
	db.session.commit()
	ws = websocket.WebSocket()
	ws.connect("ws://127.0.0.1:8881")
	ws.send(noti)
