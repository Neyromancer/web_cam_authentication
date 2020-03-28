#!/usr/bin/env python3
# -*- condgin: utf-8 -*-

import socketserver

from .daemonizer import Daemonizer
from .request_handler import RequestHandler

class Server( socketserver.ThreadingUDPServer ):
    """
    1. thread for recieving data from client and writing to queue
    2. thread for hashing recieved data.
    """
    def __init__( self ):
      print( "Server instance created!" )
      self.daemon =  Daemonizer()
      self.host = "127.0.0.1"
      self.port = 65432
      self.request_queue_size = 10 # needed for queueing datagrams
      self( ( self.host, self.port ), RequestHandler )

    def daemonize( self ):
        self.daemon.daemonize( self )
