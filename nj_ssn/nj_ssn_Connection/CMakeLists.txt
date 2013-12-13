# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_Connection)

#..............................................................................
#
# src folder
#

set (
	CONNECTION_JNC_LIST
	nj_ssn_ConnectionLog.jnc
	nj_ssn_ConnectionSession.jnc
	)

source_virtual_folder (
	src
	${CONNECTION_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	CONNECTION_RES_LIST
	nj_ssn_Connection.njini
	connection.png
	connect.png
	pause.png
	)

source_virtual_folder (
	res
	${CONNECTION_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Connection script library
#

add_library (
	nj_ssn_Connection
	EXCLUDE_FROM_ALL
	${CONNECTION_JNC_LIST}
	${CONNECTION_RES_LIST}
	)

set_target_properties (
	nj_ssn_Connection
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
