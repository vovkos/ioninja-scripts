# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssp_Serial)

#..............................................................................
#
# src folder
#

set (
	SSP_JNC_LIST
	nj_ssp_SerialLog.jnc
	nj_ssp_SerialSession.jnc
	)

source_virtual_folder (
	ssp
	${SSP_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SSP_RES_LIST
	nj_ssp_Serial.njssp
	serial.png
	connect.png
	pause.png
	)

source_virtual_folder (
	res
	${SSP_RES_LIST}
	)

#..............................................................................
#
# nj_ssp_Serial script library
#

add_library (
	nj_ssp_Serial
	EXCLUDE_FROM_ALL
	${SSP_JNC_LIST}
	${SSP_RES_LIST}
	)

set_target_properties (
	nj_ssp_Serial
	PROPERTIES
	FOLDER "scripts"
	LINKER_LANGUAGE C
	)

#..............................................................................
