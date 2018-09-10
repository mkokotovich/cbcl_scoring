#!/bin/bash

echo "Running migrations"
docker-compose exec api python manage.py migrate

echo "Restarting django"
docker-compose restart api

echo "Creating test user"
curl -X POST -H "Content-Type: application/json" -d '{"username": "test", "password": "test"}' http://localhost:8008/api/users/v1/

echo
echo "Success!"
