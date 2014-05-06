# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_plg_TcpListener)

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	TcpListenerLog.jnc
	TcpListenerSession.jnc
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
	TcpListener.njplg
	)

source_virtual_folder (
	prj
	${PLG_PRJ_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	PLG_IMG_LIST
	images/disconnect.png
	images/listener.png
	images/listen.png
	images/pause.png
	)

source_virtual_folder (
	img
	${PLG_IMG_LIST}
	)

#..............................................................................
#
# nj_plg_TcpListener script library
#

add_library (
	nj_plg_TcpListener
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_TcpListener
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
