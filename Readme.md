Configus - a declarative contract for configuration


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

Let start with a simple spec that our requires `debug`, `version` and `secret_cookie` configuration params

```python
# app.py
from configus import config, trafaret as t

if __name__ == '__main__':
    # describes shape of the data params which will be taken either from env, cli args or envfile.
    schema = t.Dict(DEBUG=t.StrBool, VERSION=t.Float, SECRET_COOKIE=t.String)
    env_vars = config(schema=schema)
    assert env_vars == {'DEBUG': True, VERSION: 0.1, SECRET_COOKIE=<......>}
```

Once schema defined we can pass variables throw env

```shell
DEBUG=1 VERSION=1.0 SECRET_COOKIE=yo python app.py
```

Cmd flags
```shell
python app.py --debug=1 version=1.0
```

Or even both

```shell
export VERSION=1.0
export SECRET_COOKIE=yo
python app.py --debug=2
```
