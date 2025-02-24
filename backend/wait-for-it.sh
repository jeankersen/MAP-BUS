#!/bin/bash

# wait-for-it.sh script
# https://github.com/vishnubob/wait-for-it

host="$1"
shift
port="$1"
shift
cmd="$@"

# Wait for the db to be available
until nc -v -w30 $host $port </dev/null 2>&1 | grep -q "succeeded"; do
  echo "Waiting for database to be ready..."
  sleep 5
done

echo "Database is up - executing command"
exec $cmd
