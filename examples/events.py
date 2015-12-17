# -*- coding: utf-8 -*-
import os.path
from onvif import ONVIFCamera
__author__ = 'vahid'


this_dir = os.path.abspath(os.path.dirname(__file__))
wsdl_dir = os.path.abspath(os.path.join(this_dir, '../wsdl'))

def get_event_srv():
    mycam = ONVIFCamera('10.0.0.38', 80, 'admin', 'admin') #, no_cache=True)
    print mycam.devicemgmt.GetServices()
    event_service = mycam.create_events_service()
    return event_service


if __name__ == '__main__':

    mycam = ONVIFCamera('10.0.0.38', 80, 'admin', 'admin') #, no_cache=True)
    print mycam.devicemgmt.GetServices()
    e_service = mycam.create_events_service()


    pp = e_service.GetEventProperties()
    
    print pp

#    params = e_service.create_type('CreatePullPointSubscription')
#    params.InitialTerminationTime = "PT600S"
#    p1 = e_service.CreatePullPointSubscription(params)
#    print p1



    p_service = mycam.create_eventspullpoint_service()
    params2 = e_service.create_type('PullMessages')
    params2.Timeout = "PT1M"
    params2.MessageLimit = 1024
    while (1 == 1):
        p2 = p_service.PullMessages(params2)
#        print p2
        if (p2.NotificationMessage[0].Message.Message.Data.SimpleItem._Name == "IsMotion"):
        	print p2.NotificationMessage[0].Message.Message.Data.SimpleItem._Value

    
