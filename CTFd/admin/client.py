import websocket
def broadcast(noti):
	ws = websocket.WebSocket()
	ws.connect("ws://127.0.0.1:8881")
	ws.send(noti)
