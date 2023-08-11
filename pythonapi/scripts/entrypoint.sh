#!/usr/bin/bash

API_PORT=$ENV_PORT

# Move to project folder
cd app
echo "File and folders in "$PWD
for entry in $PWD/*
do
  echo "$entry"
done
echo

echo "Project in progress.."
echo "Project port: $API_PORT"

poetry run gunicorn 'app:start_api()' \
    --name project \
    --bind 0.0.0.0:"${API_PORT}" \
    --workers 3 \
"$@"