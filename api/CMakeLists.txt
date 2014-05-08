# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_api_jnc)

#..............................................................................
#
# src folder
#

set (
	API_JNC_LIST
	doc_Plugin.jnc
	doc_PluginHost.jnc
	doc_Storage.jnc
	gui_Base.jnc
	gui_Dialog.jnc
	gui_PropertyGrid.jnc
	io_FileStream.jnc
	io_MappedFile.jnc
	io_NamedPipe.jnc
	io_NetworkAdapter.jnc
	io_PCap.jnc
	io_Packet.jnc
	io_Serial.jnc
	io_SerialMon.jnc
	io_Socket.jnc
	io_SocketAddress.jnc
	io_Ssh.jnc
	log.jnc
	std.jnc
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
	nj_api_jnc
	EXCLUDE_FROM_ALL
	${API_JNC_LIST}
	)

set_target_properties (
	nj_api_jnc
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
