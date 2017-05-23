Configus - a declarative spec for configuration


### Instalation

```
pip install configus
```

### Features

- [x] Unified spec for process config
- [x] Strict validation of config, no more trailing whitespaces or runtime panics from malphormed uri's

- [x] Support parametrization from env variables and cli arguments at the same time.
    - [x] The same param could passed as `export DEBUG=on` or `--debug=on`
- [x] Auto load of `.env` file
- [x] Easy to mock for unit tests

### Usage

```python

from configus import config, trafaret as t

if __name__ == '__main__':
    schema = t.Dict(DEBUG=t.StrBool, VERSION=t.Float, SECRET_COOKIE=t.String)
    env_vars = config(schema=schema)
    assert env_vars == {'DEBUG': True, VERSION: 0.1, SECRET_COOKIE=<......>}
```
