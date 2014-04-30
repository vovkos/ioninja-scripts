# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_prp_Echo)

#..............................................................................
#
# src folder
#

set (
	PRP_JNC_LIST
	nj_prp_EchoProtocol.jnc
	)

source_virtual_folder (
	src
	${PRP_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	PRP_RES_LIST
	nj_prp_Echo.njprp
	echo.png
	)

source_virtual_folder (
	res
	${PRP_RES_LIST}
	)

#..............................................................................
#
# nj_prp_Echo script library
#

add_library (
	nj_prp_Echo
	EXCLUDE_FROM_ALL
	${PRP_JNC_LIST}
	${PRP_RES_LIST}
	)

set_target_properties (
	nj_prp_Echo
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
