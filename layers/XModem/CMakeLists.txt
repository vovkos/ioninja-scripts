# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_plg_XModem)

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	XModem.jnc
	XModemLayer.jnc
	XModemTransmitter.jnc
	XModemReceiver.jnc
	)

source_virtual_folder (
	src
	${PLG_JNC_LIST}
	)

#..............................................................................
#
# prj folder
#

set (
	PLG_PRJ_LIST
	XModem.njplg
	)

source_virtual_folder (
	prj
	${PLG_PRJ_LIST}
	)

#..............................................................................
#
# img folder
#

set (
	PLG_IMG_LIST
	images/xmodem.png
	)

source_virtual_folder (
	img
	${PLG_IMG_LIST}
	)

#..............................................................................
#
# nj_PLG_XModem script library
#

add_library (
	nj_plg_XModem
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_XModem
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
