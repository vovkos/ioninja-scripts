# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssp_PipeListener)

#..............................................................................
#
# src folder
#

set (
	SSP_JNC_LIST
	nj_ssp_PipeListenerLog.jnc
	nj_ssp_PipeListenerSession.jnc
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
	nj_ssp_PipeListener.njssp
	disconnect.png
	listener.png
	listen.png
	pause.png
	)

source_virtual_folder (
	res
	${SSP_RES_LIST}
	)

#..............................................................................
#
# nj_ssp_PipeListener script library
#

add_library (
	nj_ssp_PipeListener
	EXCLUDE_FROM_ALL
	${SSP_JNC_LIST}
	${SSP_RES_LIST}
	)

set_target_properties (
	nj_ssp_PipeListener
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
