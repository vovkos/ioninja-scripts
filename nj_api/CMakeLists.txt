# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2013. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................

project_virtual_folder (nj_api)

#..............................................................................
#
# src folder
#

set (
	API_JNC_LIST
	nj_doc.jnc
	nj_gui.jnc
	nj_io.jnc
	nj_log.jnc
	nj_std.jnc
	)

source_virtual_folder (
	src
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
