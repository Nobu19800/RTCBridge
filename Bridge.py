#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file Bridge.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


class DataListener(OpenRTM_aist.ConnectorDataListenerT):
  def __init__(self, outport):
    self._outport = outport
    
  def __del__(self):
    pass

  def __call__(self, info, cdrdata):
    cons = self._outport.connectors()
    for con in cons:
		print dir(con)
		con._publisher.write(cdrdata, 0, 0)
	

    return OpenRTM_aist.ConnectorListenerStatus.NO_CHANGE


class ConnListener(OpenRTM_aist.ConnectorListener):
  def __init__(self, thebuffer):
    self._thebuffer = thebuffer

  def __del__(self):
    pass

  def __call__(self, info):
    prop = OpenRTM_aist.Properties()
    prop.setProperty("write.full_policy", "do_nothing")
    prop.setProperty("read.empty_policy", "do_nothing")
    self._thebuffer.init(prop)
    

    return OpenRTM_aist.ConnectorListenerStatus.NO_CHANGE

    


# This module's spesification
# <rtc-template block="module_spec">
bridge_spec = ["implementation_id", "Bridge", 
		 "type_name",         "Bridge", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.port_num", "1",

		 "conf.__widget__.port_num", "text",

         "conf.__type__.port_num", "int",

		 ""]
# </rtc-template>

##
# @class Bridge
# @brief ModuleDescription
# 
# 
class Bridge(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
		self._port_list = []



		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		ポートの数(InPort、OutPortでセット)
		 - Name: port_num port_num
		 - DefaultValue: 1
		"""
		self._port_num = [1]
		
		# </rtc-template>

	def addExtPort(self):
		ports = {}
		num = len(self._port_list)

		inname = "in"+str(num)
		ports["inport"] = OpenRTM_aist.InPortBase(inname, "any")
		self.addInPort(inname,ports["inport"])

		outname = "out"+str(num)
		ports["outport"] = OpenRTM_aist.OutPortBase(outname, "any")
		self.addOutPort(outname,ports["outport"])

		self.sendDataListener = DataListener(ports["outport"])
		ports["inport"].addConnectorDataListener(OpenRTM_aist.ConnectorDataListenerType.ON_RECEIVED,self.sendDataListener)

		self.sendConListener = ConnListener(ports["inport"]._thebuffer)
		ports["inport"].addConnectorListener(OpenRTM_aist.ConnectorListenerType.ON_CONNECT, self.sendConListener)

		self._port_list.append(ports)

		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("port_num", self._port_num, "1")
		
		# Set InPort buffers
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		for i in range(self._port_num[0]):
			self.addExtPort()
		
		return RTC.RTC_OK
	
	###
	## 
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	## 
	## @return RTC::ReturnCode_t
	#
	## 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	## 
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The activated action (Active state entry action)
	## former rtc_active_entry()
	##
	## @param ec_id target ExecutionContext Id
	## 
	## @return RTC::ReturnCode_t
	##
	##
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The deactivated action (Active state exit action)
	## former rtc_active_exit()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The execution action that is invoked periodically
	## former rtc_active_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onExecute(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def BridgeInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=bridge_spec)
    manager.registerFactory(profile,
                            Bridge,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    BridgeInit(manager)

    # Create a component
    comp = manager.createComponent("Bridge")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

