#!/usr/bin/env bash

cur_dir=$(pwd)
src_dir="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd)"

cd $src_dir

docker-compose exec web python manage.py dumpdata > data/dump_`date +%d-%m-%Y"_"%H_%M_%S`.json

while [ $(ls data -1 | grep .json | wc -l) -gt 7 ]
do
  rm data/$(ls data -1 | grep -m1 .json)
done

cd $cur_dir
