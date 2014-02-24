# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssn_Udp)

#..............................................................................
#
# src folder
#

set (
	UDP_JNC_LIST
	nj_ssn_UdpLog.jnc
	nj_ssn_UdpSession.jnc
	)

source_virtual_folder (
	src
	${UDP_JNC_LIST}
	)

#..............................................................................
#
# res folder
#

set (
	UDP_RES_LIST
	nj_ssn_Udp.njini
	udp.png
	)

source_virtual_folder (
	res
	${UDP_RES_LIST}
	)

#..............................................................................
#
# nj_ssn_Udp script library
#

add_library (
	nj_ssn_Udp
	EXCLUDE_FROM_ALL
	${UDP_JNC_LIST}
	${UDP_RES_LIST}
	)

set_target_properties (
	nj_ssn_Udp
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
