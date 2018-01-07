# MDWiki

## Summary

Confluence like blog

## I18N

### Requirement

I18N requires [gettext](https://mlocati.github.io/articles/gettext-iconv-windows.html).

### Step

```bash
python manage.py makemessages --all -i venv
# translate `.po` files
python manage.py compilemessages --exclude=venv
```