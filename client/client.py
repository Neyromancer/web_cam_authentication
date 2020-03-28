#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import socket

from client.recipient import Recipient

class Client:
  """
  Class for establishing UDP connection with server side
    Should repetitivly send each datagram 3 times
  """
  def __init__( self ):
    self.recipient = Recipient()
    self.host = "127.0.0.1"
    self.port = 65432
 
  def send( self, password: str ) -> None:
    with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s:
      s.connect( ( self.host, self.port ) )
      s.sendall( password.encode() )

  def start( self ) -> None:
    self.recipient.get_pswd_from_cmd()
    password = self.recipient.get_password()
    if not password:
      print( "Fail to retrieve password from cmd" )

    self.send( password )

if __name__ == "__main__":
  client = Client()
  client.start()
