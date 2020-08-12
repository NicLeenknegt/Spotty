#!/usr/bin/python3

import sys,  getopt
from views.DeviceView import DeviceView
from view_models.DeviceViewModel import DeviceViewModel
from resources.options.Option import Option

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"i",["init"])
    except:
        print ('spotty [--init|-i]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i",  "--init"):
            option = Option('select', True)
            print(option.get_long_option())
            print(option.get_short_option())
            sys.exit()

if  __name__ ==  "__main__":
    main(sys.argv[1:])

