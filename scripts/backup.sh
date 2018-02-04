#!/usr/bin/env bash

cur_dir=$(pwd)
src_dir="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd)"

cd $src_dir

docker-compose exec web python manage.py dumpdata > data/dump_`date +%d-%m-%Y"_"%H_%M_%S`.json

cd $cur_dir
