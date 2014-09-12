# This file is part of IO Ninja project
# Tibbo Technology Inc (C) 2004-2014. All rights reserved
# Author: Vladimir Gladkov

#..............................................................................
#
# src folder
#

set (
	PLG_JNC_LIST
	PipeListenerLog.jnc
	PipeListenerSession.jnc
	)

source_group (
	src
	FILES
	${PLG_JNC_LIST}
	)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#
# prj folder
#

set (
	PLG_PRJ_LIST
	PipeListener.njplg
	)

source_group (
	prj
	FILES
	${PLG_PRJ_LIST}
	)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#
# img folder
#

set (
	PLG_IMG_LIST
	images/disconnect.png
	images/listen.png
	images/pause.png
	images/pipe.png
	)

source_group (
	img
	FILES
	${PLG_IMG_LIST}
	)

#..............................................................................
#
# nj_plg_PipeListener script library
#

add_library (
	nj_plg_PipeListener
	EXCLUDE_FROM_ALL
	${PLG_JNC_LIST}
	${PLG_PRJ_LIST}
	${PLG_IMG_LIST}
	)

set_target_properties (
	nj_plg_PipeListener
	PROPERTIES
	FOLDER scripts
	LINKER_LANGUAGE C
	)

#..............................................................................
