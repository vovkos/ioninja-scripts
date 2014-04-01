# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_ssp_Udp)

#..............................................................................
#
# src folder
#

set (
	SSP_JNC_LIST
	nj_ssp_UdpLog.jnc
	nj_ssp_UdpSession.jnc
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
	nj_ssp_Udp.njssp
	udp.png
	)

source_virtual_folder (
	res
	${SSP_RES_LIST}
	)

#..............................................................................
#
# nj_ssp_Udp script library
#

add_library (
	nj_ssp_Udp
	EXCLUDE_FROM_ALL
	${SSP_JNC_LIST}
	${SSP_RES_LIST}
	)

set_target_properties (
	nj_ssp_Udp
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
