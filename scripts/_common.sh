#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

# dependencies used by the app
pkg_dependencies="python3 virtualenv gettext libzip-dev libssl-dev mariadb-server default-libmysqlclient-dev uwsgi uwsgi-plugin-python3 python3-uwsgidecorators"

#=================================================
# PERSONAL HELPERS
#=================================================

generate_secret_key() {
    (
        set +o nounset
        source "${final_path}/venv/bin/activate"
        set -o nounset
        python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    )
}

#=================================================
# EXPERIMENTAL HELPERS
#=================================================

#=================================================
# FUTURE OFFICIAL HELPERS
#=================================================
