#!/usr/bin/python3

import sys,  getopt
from views.DeviceView import DeviceView
from view_models.DeviceViewModel import DeviceViewModel

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"i",["init"])
    except:
        print ('spotty [--init|-i]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i",  "--init"):
            view_model = DeviceViewModel()
            device_view = DeviceView(view_model) 
            device_view.show_device_table()
            sys.exit()

if  __name__ ==  "__main__":
    main(sys.argv[1:])

