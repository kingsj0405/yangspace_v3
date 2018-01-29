# YangSpace

## Summary

Confluence-like blog.

Visit [yangspace.co.kr](http://yangspace.co.kr)

## Run for Production

### Reuiqrement

Deploy requires following:
- [Docker version](https://www.docker.com/) 17.12.0-ce, build c97c6d6
- [docker-compose](https://docs.docker.com/compose/) version 1.18.0, build 8dd22a96

### Step

```bash
cp YangSpace/settings/secret.py.template YangSpace/settings/secret.py
# fill variables
docker-compose up --build
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

### Static Library

Followings are downloaded in `static/lib`.
- [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/)
- [Font Awesome](http://fontawesome.io/) 4.7.0
- [jQuery](https://jquery.com/) 3.2.1
- [showdown](https://github.com/showdownjs/showdown) 1.8.4

