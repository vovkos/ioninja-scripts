# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_api_Script)

#..............................................................................
#
# src folder
#

set (
	API_JNC_LIST
	nj_doc.jnc
	nj_gui.jnc
	nj_io_File.jnc
	nj_io_PCap.jnc
	nj_io_Packet.jnc
	nj_io_Serial.jnc
	nj_io_Socket.jnc
	nj_io_Ssh.jnc
	nj_log.jnc
	nj_std.jnc
	)

source_virtual_folder (
	api
	${API_JNC_LIST}
	)

#..............................................................................
#
# nj_api script library
#

add_library (
	nj_api_Script
	EXCLUDE_FROM_ALL
	${API_JNC_LIST}
	)

set_target_properties (
	nj_api_Script
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
