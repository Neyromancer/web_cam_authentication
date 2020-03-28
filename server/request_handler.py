#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import socket
import threading
import socketserver

class RequestHandler( socketserver.DatagramRequestHandler ):
    def __init__( self ):
        self.data = ""
        print( "Request handler instantiated" )

    def get_data( self ):
        if self.data:
            return self.data

    def handle( self ):
        self.data = str( self.request.recv( 1024 ), 'ascii' )
