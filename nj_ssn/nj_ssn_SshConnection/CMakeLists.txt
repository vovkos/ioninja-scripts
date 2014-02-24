# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_SshConnection)

#..............................................................................
#
# src folder
#

set (
	SSN_JNC_LIST
	nj_ssn_SshConnectionLog.jnc
	nj_ssn_SshConnectionSession.jnc
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
	nj_ssn_SshConnection.njini
	connection.png
	connect.png
	disconnect.png
	)

source_virtual_folder (
	res
	${SSN_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_SshConnection script library
#

add_library (
	nj_ssn_SshConnection
	EXCLUDE_FROM_ALL
	${SSN_JNC_LIST}
	${SSN_RES_LIST}
	)

set_target_properties (
	nj_ssn_SshConnection
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
