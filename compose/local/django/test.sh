#!/bin/sh

set -o errexit
#set -o pipefail
set -o nounset
set -o xtrace


python manage.py test --no-input
