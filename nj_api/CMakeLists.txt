# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov
	   
#..............................................................................
#
# src folder
#

set (
	API_JNC_LIST 
	nj_gui.jnc
	nj_io_Serial.jnc
	nj_io_Socket.jnc
	nj_log.jnc
	nj_std.jnc
	)

source_group (
	src
	FILES 
	${API_JNC_LIST}
	)

#..............................................................................
#
# nj_api script library
#
  
add_library (
	nj_api
	EXCLUDE_FROM_ALL
	${API_JNC_LIST}
	)

set_target_properties (
	nj_api 
	PROPERTIES 
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
