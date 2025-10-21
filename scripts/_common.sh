#!/bin/bash

#=================================================
# COMMON VARIABLES AND CUSTOM HELPERS
#=================================================

generate_secret_key() {
    (
        set +o nounset
        source "${install_dir}/venv/bin/activate"
        set -o nounset
        python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    )
}
