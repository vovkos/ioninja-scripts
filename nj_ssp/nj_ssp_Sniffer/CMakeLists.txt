# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssp_Sniffer)

#..............................................................................
#
# src folder
#

set (
	SSP_JNC_LIST
	nj_ssp_SnifferLog.jnc
	nj_ssp_SnifferLog_Ethernet.jnc
	nj_ssp_SnifferLog_Ip.jnc
	nj_ssp_SnifferLog_Icmp.jnc
	nj_ssp_SnifferLog_Tcp.jnc
	nj_ssp_SnifferLog_Udp.jnc
	nj_ssp_SnifferSession.jnc
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
	nj_ssp_Sniffer.njssp
	sniffer.png
	)

source_virtual_folder (
	res
	${SSP_RES_LIST}
	)

#..............................................................................
#
# nj_ssp_Sniffer script library
#

add_library (
	nj_ssp_Sniffer
	EXCLUDE_FROM_ALL
	${SSP_JNC_LIST}
	${SSP_RES_LIST}
	)

set_target_properties (
	nj_ssp_Sniffer
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
