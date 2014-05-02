# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_plg_SerialMon)

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	SerialMonLog.jnc
	SerialMonSession.jnc
	)

source_virtual_folder (
	src
	${PLG_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	PLG_PRJ_LIST
	SerialMon.njssp
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
	images/capture.png
	images/pause.png
	images/serialmon.png
	)

source_virtual_folder (
	img
	${PLG_IMG_LIST}
	)


#..............................................................................
#
# nj_plg_SerialMon script library
#

add_library (
	nj_plg_SerialMon
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_SerialMon
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
