# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssp_TcpProxy)

#..............................................................................
#
# src folder
#

set (
	SSP_JNC_LIST
	nj_ssp_TcpProxyLog.jnc
	nj_ssp_TcpProxySession.jnc
	)

source_virtual_folder (
	src
	${SSP_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SSP_RES_LIST
	nj_ssp_TcpProxy.njssp
	disconnect.png
	listen.png
	proxy.png
	)

source_virtual_folder (
	res
	${SSP_RES_LIST}
	)

#..............................................................................
#
# nj_ssp_TcpProxy script library
#

add_library (
	nj_ssp_TcpProxy
	EXCLUDE_FROM_ALL
	${SSP_JNC_LIST}
	${SSP_RES_LIST}
	)

set_target_properties (
	nj_ssp_TcpProxy
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
