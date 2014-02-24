# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_Sniffer)

#..............................................................................
#
# src folder
#

set (
	SNIFFER_JNC_LIST
	nj_ssn_SnifferLog.jnc
	nj_ssn_SnifferLog_Ethernet.jnc
	nj_ssn_SnifferLog_Ip.jnc
	nj_ssn_SnifferLog_Icmp.jnc
	nj_ssn_SnifferLog_Tcp.jnc
	nj_ssn_SnifferLog_Udp.jnc
	nj_ssn_SnifferSession.jnc
	)

source_virtual_folder (
	src
	${SNIFFER_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	SNIFFER_RES_LIST
	nj_ssn_Sniffer.njini
	sniffer.png
	)

source_virtual_folder (
	res
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
