from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):
   	def handleMessage(self):
     	 	for client in clients:
        	 	if client != self:
            			client.sendMessage("Hello")
		print self.data

   	def handleConnected(self):
		print(self.address,'connected')
		for client in clients:
			client.sendMessage("Hello")
     		clients.append(self)

   	def handleClose(self):
      		clients.remove(self)
      		print (self.address, 'closed')
      		for client in clients:
         		client.sendMessage(self.address[0] + u' - disconnected')

server =SimpleWebSocketServer('', 8881, SimpleChat)
server.serveforever()

