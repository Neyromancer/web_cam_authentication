#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from client.recipient import Recipient

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

    def __add_user( self, user, password: str ) -> None:
        try:
            subprocess.run( ['useradd','-m' , user, '-p', password], stdin= subprocess.DEVNULL,
                            stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT, check=True )
        except subprocess.CalledProcessError as exp:
            print( "Error {0} occured on trying to create user {1} ".format( exp.returncode, user ) )

    def __del_user( self, user: str ) -> None:
        try:
            subprocess.run( ['userdel','-r', '-f' , user], stdin= subprocess.DEVNULL,
                            stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT, check=True )
        except subprocess.CalledProcessError as exp:
            print( "Error {0} occured on trying to delete user {1} ".format( exp.returncode, user ) )

    def is_user_exist( self, user: str ) -> bool:
        try:
            pwd.getpwnam( user )
        except KeyError:
            return False
        return True

    def create_user( self, user: str, password: str ) -> None:
        if self.is_user_exist( user ):
            print( "User {0} already exists".format( user ) )
            return

        self.__add_user(user, password)

    def delete_user( self, user: str ) -> None:
        if not self.is_user_exist( user ):
            print( "User {0} does not exists".format( user ) )
            return

        self.__del_user( user )

    def get_user_password( self, user: str ) -> str:
        if not self.is_user_exist( user ):
            print( "User does {0} not exist!".format( user ) )
            return ""
        pw = pwd.getpwnam( user )
        return pw.pw_passwd
