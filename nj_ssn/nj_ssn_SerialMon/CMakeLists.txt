# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_SerialMon)

#..............................................................................
#
# src folder
#

set (
	SERIALMON_JNC_LIST
	nj_ssn_SerialMonLog.jnc
	nj_ssn_SerialMonSession.jnc
	)

source_virtual_folder (
	src
	${SERIALMON_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SERIALMON_RES_LIST
	nj_ssn_SerialMon.njini
	serialmon.png
	)

source_virtual_folder (
	res
	${SERIALMON_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_SerialMon script library
#

add_library (
	nj_ssn_SerialMon
	EXCLUDE_FROM_ALL
	${SERIALMON_JNC_LIST}
	${SERIALMON_RES_LIST}
	)

set_target_properties (
	nj_ssn_SerialMon
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
