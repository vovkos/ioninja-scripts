# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	SerialMonLog.jnc
	SerialMonSession.jnc
	)

source_group (
	src
	FILES
	${PLG_JNC_LIST}
	)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#
# res folder
#

set (
	PLG_PRJ_LIST
	SerialMon.njplg
	)

source_group (
	prj
	FILES
	${PLG_PRJ_LIST}
	)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#
# img folder
#

set (
	PLG_IMG_LIST
	images/capture.png
	images/pause.png
	images/serialmon.png
	)

source_group (
	img
	FILES
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
