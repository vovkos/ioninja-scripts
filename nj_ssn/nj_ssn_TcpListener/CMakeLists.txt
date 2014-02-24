# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_TcpListener)

#..............................................................................
#
# src folder
#

set (
	SSN_JNC_LIST
	nj_ssn_TcpListenerLog.jnc
	nj_ssn_TcpListenerSession.jnc
	)

source_virtual_folder (
	src
	${SSN_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SSN_RES_LIST
	nj_ssn_TcpListener.njini
	disconnect.png
	listener.png
	listen.png
	pause.png
	)

source_virtual_folder (
	res
	${SSN_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_TcpListener script library
#

add_library (
	nj_ssn_TcpListener
	EXCLUDE_FROM_ALL
	${SSN_JNC_LIST}
	${SSN_RES_LIST}
	)

set_target_properties (
	nj_ssn_TcpListener
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
