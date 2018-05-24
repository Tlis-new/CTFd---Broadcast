from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):
   	def handleMessage(self):
     	 	for client in clients:
        	 	if client != self:
            			client.sendMessage(self.data)
		print self.data

   	def handleConnected(self):
		clients.append(self)

   	def handleClose(self):
		clients.remove(self)

server =SimpleWebSocketServer('127.0.0.1', 8881, SimpleChat)
server.serveforever()

