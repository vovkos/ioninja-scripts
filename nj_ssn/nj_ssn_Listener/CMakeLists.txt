# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_Listener)

#..............................................................................
#
# src folder
#

set (
	LISTENER_JNC_LIST
	nj_ssn_ListenerLog.jnc
	nj_ssn_ListenerSession.jnc
	)

source_virtual_folder (
	src
	${LISTENER_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	LISTENER_RES_LIST
	nj_ssn_Listener.njini
	listener.png
	listen.png
	pause.png
	)

source_virtual_folder (
	res
	${LISTENER_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Listener script library
#

add_library (
	nj_ssn_Listener
	EXCLUDE_FROM_ALL
	${LISTENER_JNC_LIST}
	${LISTENER_RES_LIST}
	)

set_target_properties (
	nj_ssn_Listener
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
