#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from password_module.validator import Validator
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

  def set_password( self, password: str ) -> None:
    if not self.validator.is_valid( password ):
        print( "Invalid password passed" )
        return
    self.password = password

  def get_password( self ) -> str:
    return self.password

  def get_user( self ) -> str:
    return self.user

  def set_user( self, user: str ) -> str:
    if self.validator.is_user_valid( user ):
      self.user = user

  def get_pswd_from_cmd( self ) -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument( "password", help="passed password" )
    args = parser.parse_args()

    self.set_password( args.password )
