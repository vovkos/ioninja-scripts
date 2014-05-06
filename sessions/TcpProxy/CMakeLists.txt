# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_plg_TcpProxy)

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	TcpProxyLog.jnc
	TcpProxySession.jnc
	)

source_virtual_folder (
	src
	${PLG_JNC_LIST}
	)

#..............................................................................
#
# prj folder
#

set (
	PLG_PRJ_LIST
	TcpProxy.njplg
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
	images/disconnect.png
	images/listen.png
	images/proxy.png
	)

source_virtual_folder (
	img
	${PLG_IMG_LIST}
	)

#..............................................................................
#
# nj_plg_TcpProxy script library
#

add_library (
	nj_plg_TcpProxy
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_TcpProxy
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
