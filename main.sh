#!/bin/bash

while getopts "i(init)-:p" options
do
	case "${options}"
	in
		-)
			case "${OPTARG}"
			in
				init)
				echo check	
				;;
			esac
			;;
		p)
			echo play
			;;
	esac
done