# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_TcpProxy)

#..............................................................................
#
# src folder
#

set (
	SSN_JNC_LIST
	nj_ssn_TcpProxyLog.jnc
	nj_ssn_TcpProxySession.jnc
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
	nj_ssn_TcpProxy.njini
	disconnect.png
	listen.png
	proxy.png
	)

source_virtual_folder (
	res
	${SSN_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_TcpProxy script library
#

add_library (
	nj_ssn_TcpProxy
	EXCLUDE_FROM_ALL
	${SSN_JNC_LIST}
	${SSN_RES_LIST}
	)

set_target_properties (
	nj_ssn_TcpProxy
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
