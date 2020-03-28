#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from password_module.system_pswd_manipulator import SystemPswdManipulator

import unittest
import getpass

class TestSystemPswdManipulator( unittest.TestCase ):
    def __init__( self ):
        self.sys_manip = SystemPswdManipulator()
        self.test_user = "TestUser"
        self.test_passwd = "1234"
        self.current_user = getpass.getuser()

    def tearDown(self) -> None:
        self.sys_manip.delete_user( self.test_user )

    def test_is_user_exist( self ) -> None:
        self.assertTrue( self.sys_manip.is_user_exist( self.current_user ),
                         "Fail to identify user's existance" )
        self.assertFalse( self.sys_manip.is_user_exist( self.test_user ),
                          "Fail to identify user's existance")
        
    def test_add_user( self ) -> None:
        self.assertFalse( self.sys_manip.is_user_exist( self.test_user ) )
        self.sys_manip.add_user( self.test_user, self.test_passwd )
        self.assertTrue( self.sys_manip.is_user_exist( self.test_user ) )

    def test_get_user_password( self ) -> None:
        self.sys_manip.add_user( self.test_user, self.test_passwd )
        self.assertEqual( self.test_passwd, self.sys_manip.get_user_password( self.test_user ) )

if __name__ == '__main__':
    unittest.main()
