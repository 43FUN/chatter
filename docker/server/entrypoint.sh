#!/bin/bash

# After supervisor installing it falss with an error because logfile is not found
mkdir -p $( dirname $(cat /usr/src/app/supervisord.conf | grep logfile= | grep "\.log" | sed s/.*logfile=// ) )
touch $( cat /usr/src/app/supervisord.conf | grep logfile= | grep "\.log" | sed s/.*logfile=// )

exec "$@"