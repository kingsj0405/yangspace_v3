# MDWiki

## Summary

Confluence like blog

## Run for Production

### Reuiqrement

Deploy requires [docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/), [docker-compose](https://docs.docker.com/compose/install/).

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

## I18N

### Requirement

I18N requires [gettext](https://mlocati.github.io/articles/gettext-iconv-windows.html).

### Step

```bash
python manage.py makemessages --all -i venv
# translate `.po` files
python manage.py compilemessages --exclude=venv
```
