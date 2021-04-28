# Release New Version
Update version in `setup.py` and `version.py`.

Build new version locally:
```shell
python setup.py sdist  
```

Release new version to pip using `twine`:
```shell
twine upload dist/*
```