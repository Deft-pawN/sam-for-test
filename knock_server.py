# -*- coding: utf-8 -*-
# for server
from twisted.internet import protocol,reactor
class Knock(protocol.Protocol):
    def dataReceived(self,data):
        print 'Client',data
        if data.startswith("Konck knock"):
            response = "Who is there "
        else:
            response = data +"who?"
        print "Server",response
        self.transport.write(response)
        
class KnockFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Knock()
        