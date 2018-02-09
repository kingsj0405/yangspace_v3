# YangSpace v0.3.0
[![Build Status](https://travis-ci.org/kingsj0405/YangSpace.svg?branch=master)](https://travis-ci.org/kingsj0405/YangSpace)

## Summary

Confluence-like blog.

Visit [yangspace.co.kr](http://yangspace.co.kr)

### Main Feature

- CRUD of Page
- Page history and revert
- Page preview when writing
- Page Tree on Main
- Login/Logout for administrator

## Release

### Things to do on release branch

- Fix Version
    - [README.md](README.md)
- Translating
    - Check [I18N](#i18n)

### Run for Production

#### Requirement

Deploy requires following:
- [Git](https://git-scm.com/)
- [Docker version](https://www.docker.com/) 17.12.0-ce, build c97c6d6
- [docker-compose](https://docs.docker.com/compose/) version 1.18.0, build 8dd22a96

Backup data if you have.
```bash
# this file should moved to data/dump.json
docker exec -t $WEB_CONTAINER python manage.py dump > dump_`date +%d-%m-%Y"_"%H_%M_%S`.json
```

#### Step

```bash
git clone https://github.com/kingsj0405/YangSpace
cd YangSpace
cp YangSpace/settings/secret.py.template YangSpace/settings/secret.py
# fill variables on 'secret.py'

docker-compose up --build

# Create super user if you need
docker exec -t $WEB_CONTAINER python manage.py createsuperuser
```

## Development

```bash
bash scripts/run.sh
```

### I18N

#### Requirement

I18N requires [gettext](https://mlocati.github.io/articles/gettext-iconv-windows.html).

#### Step

```bash
python manage.py makemessages --all -i venv
# translate `.po` files
python manage.py compilemessages --exclude=venv
```

#### Static Library

Followings are downloaded in `static/lib`.
- [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/)
- [Font Awesome](http://fontawesome.io/) 4.7.0
- [jQuery](https://jquery.com/) 3.2.1
- [showdown](https://github.com/showdownjs/showdown) 1.8.4

#### Django Pakcage

- [django-ajax](https://github.com/yceruto/django-ajax)
- [django-mptt](https://github.com/django-mptt/django-mptt)
- [django-reversion](https://github.com/etianen/django-reversion)
- [django-extensions](https://github.com/django-extensions/django-extensions)
