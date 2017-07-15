# -*- coding: utf-8 -*-
#client 
from twisted.internet import reactor,protocol
class KonckClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write
        
    def dataReceived(self,data):
        if data.startswith("who's there"):
            response = "Disappearing client"
        else:
            self.transport.loseConnection()
            reactor.stop()
            
class KonckFactory(protocol.Protocol):
    protocol = KonckClient
    
def main():
    f =KonckFactory()
    reactor.connectTCP("locahost",8000,f)
    reactor.run()
    if __name__ =="__main__":
        main()
        