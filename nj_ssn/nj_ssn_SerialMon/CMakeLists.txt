# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov
	   
#..............................................................................
#
# src folder
#

set (
	SERIALMON_JNC_LIST 
	nj_ssn_SerialMonLog.jnc
	nj_ssn_SerialMonSession.jnc
	)

source_group (
	src
	FILES 
	${SERIALMON_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SERIALMON_RES_LIST 
	nj_ssn_SerialMon.njini
	nj_ssn_SerialMon.ico
	)

source_group (
	res
	FILES 
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
