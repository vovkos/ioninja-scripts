# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_Serial)

#..............................................................................
#
# src folder
#

set (
	SERIAL_JNC_LIST
	nj_ssn_SerialLog.jnc
	nj_ssn_SerialSession.jnc
	)

source_virtual_folder (
	ssn
	${SERIAL_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SERIAL_RES_LIST
	nj_ssn_Serial.njini
	serial.png
	connect.png
	pause.png
	)

source_virtual_folder (
	res
	${SERIAL_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Serial script library
#

add_library (
	nj_ssn_Serial
	EXCLUDE_FROM_ALL
	${SERIAL_JNC_LIST}
	${SERIAL_RES_LIST}
	)

set_target_properties (
	nj_ssn_Serial
	PROPERTIES
	FOLDER "scripts"
	LINKER_LANGUAGE C
	)

#..............................................................................
