#!/usr/bin/bash

API_PORT=$ENV_PORT

#echo "Make log files"
#touch ./logs/gunicorn.log
#touch ./logs/gunicorn-access.log

echo "Project in progress.."
echo "Project port: $API_PORT -"
poetry run gunicorn ./app/app.py \
    --name project \
    --bind 0.0.0.0:"${API_PORT}" \
#    --workers 3 \
#    --log-level=debug \
#    --error-logfile=../logs/gunicorn.log \
#    --access-logfile=../logs/gunicorn-access.log \
"$@"