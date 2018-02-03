#!/bin/sh

pushd ../

docker-compose exec web python manage.py dumpdata > data/dump_`date +%d-%m-%Y"_"%H_%M_%S`.json

popd