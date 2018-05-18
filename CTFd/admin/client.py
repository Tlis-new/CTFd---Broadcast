import websocket
def broadcast():
	ws = websocket.WebSocket()
	ws.connect("ws://127.0.0.1:8881")
	ws.send("Hello World")
