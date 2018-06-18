from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
clients = []
class SimpleChat(WebSocket):
   	def handleMessage(self):
		data = self.data
		data = json.loads(data)
		print data
		if data['action']=='5hKhnlBxkPQkuGAqN6k1ksR3yfgNtQTHA2LwtykKZcGAfe5a0EhXh79hgRGb62fWcEBwfj8E5infOb5M5QtuE' and data['token']=='5YQfIYMy3UwbYPwqF13r3QqBWLmoOXiFsMBRvQl13x73iuwlgXheuvP8KxfguZUrWhGpiIDo2yLNuWm0TPSQbrhktZX0Z3gP17NSh4R8l3Eu5hI7CwG0GF':
     	 		for client in clients:
        	 		if client != self:
            				client.sendMessage(data['noti'])

   	def handleConnected(self):
		clients.append(self)

   	def handleClose(self):
		clients.remove(self)

server =SimpleWebSocketServer('127.0.0.1', 8881, SimpleChat)
server.serveforever()

