# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_plg_TcpConnection)

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	TcpConnectionLog.jnc
	TcpConnectionSession.jnc
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
	TcpConnection.njplg
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
	images/connection.png
	images/connect.png
	images/disconnect.png
	)

source_virtual_folder (
	img
	${PLG_IMG_LIST}
	)

#..............................................................................
#
# nj_plg_TcpConnection script library
#

add_library (
	nj_plg_TcpConnection
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_TcpConnection
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
