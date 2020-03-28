#!/usri/bin/env python3
# -*- coding: utf-8 -*-

class Validator:
  """
    Validate password
    Determine if password have correct representation (symbols)
    and right image in case of image processing.
  """
  def is_password_valid( self, password ):
    if len( password ) < 8 or len( password ) >= 20:
      return False
    return True

  def is_user_valid( self, user ):
    return False
