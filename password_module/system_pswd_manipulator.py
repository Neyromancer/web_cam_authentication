#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from recipient import Recipient

import subprocess
import pwd

class SystemPswdManipulator:
    """
        Retrieve and store user password into and from the system.
    """

    def __init__( self ):
        self.recipient = Recipient()
        self.password = ""
        self.user = ""

    def add_user( self, user, password ):
        subprocess.run(['useradd','-m' , user, '-p', password]  )
        print( "Do something" )

    def is_user_exist( self, user ):
        try:
            pwd.getpwnam( user )
        except KeyError:
            return False
        return True

    def create_user( self, user, password ):
        self.add_user( user, password )

    def get_user_password( self, user ):
        if not self.is_user_exist( user ):
            print( "User does {0} not exist!".format( user ) )
            return ""
        pw = pwd.getpwnam( user )
        return pw.pw_passwd
