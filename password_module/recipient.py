#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from validator import Validator 
import argparse

class Recipient:
  """
     Retrieve password.
     as a test case -  retrieves data from cmd.
     as a final solution - retrieves data from video cam.
  """
  def __init__( self ):
    self.validator = Validator()
    self.password = ""
    self.user = ""

  def set_password( self, password ):
    if self.validator.is_valid( password ):
      self.password = password

  def get_password( self ):
    return self.password

  def get_user( self ):
    return self.user

  def set_user( self, user ):
    if self.validator.is_user_valid( user ):
      self.user = user

  def cmd_password_reciever( self ):
    parser = argparse.ArgumentParser()
    parser.add_argument( "password", help="passed password" )
    args = parser.parse_args()

    self.set_password( args.password )
