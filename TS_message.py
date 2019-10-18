#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        TS_message.py
#
#  Project :     TS_message
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      sergey.v.babenkov$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["TS_message", "TS_messageClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
import tkinter
from tkinter import messagebox
import time
import threading
# Add additional import
#----- PROTECTED REGION ID(TS_message.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	TS_message.additionnal_import

# Device States Description
# No states for this device


class TS_message (PyTango.Device_4Impl):
    """TS_message"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(TS_message.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	TS_message.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        TS_message.init_device(self)
        #----- PROTECTED REGION ID(TS_message.__init__) ENABLED START -----#
        self.check_retract=False        
        
        if not 'pingthread' in dir(self):
            self.pingthread = threading.Thread(target=self.Retract)
            self.pingthread.setDaemon(True)
            self.pingthread.start()
        #----- PROTECTED REGION END -----#	//	TS_message.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(TS_message.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TS_message.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        #----- PROTECTED REGION ID(TS_message.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TS_message.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(TS_message.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TS_message.always_executed_hook

    # -------------------------------------------------------------------------
    #    TS_message read/write attribute methods
    # -------------------------------------------------------------------------
    
    def write_Message(self, attr):
        self.debug_stream("In write_Message()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(TS_message.Message_write) ENABLED START -----#
        if self.check_retract==False:
            self.check_retract=True
        #----- PROTECTED REGION END -----#	//	TS_message.Message_write
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(TS_message.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TS_message.read_attr_hardware


    # -------------------------------------------------------------------------
    #    TS_message command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(TS_message.programmer_methods) ENABLED START -----#
    def Retract(self):
        while True:
            if self.check_retract==True:
                root = tkinter.Tk()
                root.withdraw()
                result = messagebox.askyesno("Python","Would you like to save the data?")
                print result                
                self.check_retract=False
            time.sleep(0.1)
    #----- PROTECTED REGION END -----#	//	TS_message.programmer_methods

class TS_messageClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(TS_message.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	TS_message.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'Message':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.WRITE]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(TS_messageClass, TS_message, 'TS_message')
        #----- PROTECTED REGION ID(TS_message.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	TS_message.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
