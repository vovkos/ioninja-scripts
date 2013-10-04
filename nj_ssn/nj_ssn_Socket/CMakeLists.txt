# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov
	   
#..............................................................................
#
# src folder
#

set (
	SOCKET_JNC_LIST 
	nj_ssn_ConnectionSocketLog.jnc
	nj_ssn_ConnectionSocketSession.jnc
	nj_ssn_ListenerSocketLog.jnc
	nj_ssn_ListenerSocketSession.jnc
	)

source_group (
	src
	FILES 
	${SOCKET_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SOCKET_RES_LIST 
	nj_ssn_ConnectionSocket.njini
	nj_ssn_ConnectionSocket.ico
	nj_ssn_ListenerSocket.njini
	nj_ssn_ListenerSocket.ico
	)

source_group (
	res
	FILES 
	${SOCKET_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Socket script library
#
  
add_library (
	nj_ssn_Socket
	EXCLUDE_FROM_ALL
	${SOCKET_JNC_LIST}
	${SOCKET_RES_LIST}
	)

set_target_properties (
	nj_ssn_Socket
	PROPERTIES 
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
