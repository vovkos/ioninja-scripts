# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_lap_Echo)

#..............................................................................
#
# src folder
#

set (
	LAP_JNC_LIST
	nj_lap_EchoLayer.jnc
	)

source_virtual_folder (
	src
	${LAP_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	LAP_RES_LIST
	nj_lap_Echo.njlap
	echo.png
	)

source_virtual_folder (
	res
	${LAP_RES_LIST}
	)

#..............................................................................
#
# nj_lap_Echo script library
#

add_library (
	nj_lap_Echo
	EXCLUDE_FROM_ALL
	${LAP_JNC_LIST}
	${LAP_RES_LIST}
	)

set_target_properties (
	nj_lap_Echo
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
