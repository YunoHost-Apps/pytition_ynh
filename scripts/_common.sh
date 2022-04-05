#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

# dependencies used by the app
pkg_dependencies=(
    python3 virtualenv
    gettext libzip-dev libssl-dev
    mariadb-server default-libmysqlclient-dev
    uwsgi uwsgi-plugin-python3 python3-uwsgidecorators
)

#=================================================
# PERSONAL HELPERS
#=================================================

#=================================================
# EXPERIMENTAL HELPERS
#=================================================

#=================================================
# FUTURE OFFICIAL HELPERS
#=================================================
