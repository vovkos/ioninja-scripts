# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov
	   
#..............................................................................
#
# src folder
#

set (
	SNIFFER_JNC_LIST 
	nj_ssn_SnifferLog.jnc
	nj_ssn_SnifferSession.jnc
	)

source_group (
	src
	FILES 
	${SNIFFER_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SNIFFER_RES_LIST 
	nj_ssn_Sniffer.njini
	nj_ssn_Sniffer.ico
	)

source_group (
	res
	FILES 
	${SNIFFER_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Sniffer script library
#
  
add_library (
	nj_ssn_Sniffer
	EXCLUDE_FROM_ALL
	${SNIFFER_JNC_LIST}
	${SNIFFER_RES_LIST}
	)

set_target_properties (
	nj_ssn_Sniffer
	PROPERTIES 
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
