import os
import sys
import trafaret


def config(schema, env=None, ignore_extra=True, config_file='.env'):

    assert isinstance(schema, trafaret.Trafaret), "Unexpected schema"

    env = env or os.environ.copy()
    if ignore_extra:
        schema = schema.ignore_extra('*')

    envfile = maybe_read_envfile(config_file)

    _env = envfile.copy()
    _env.update(**env)

    agrs_env = maybe_get_argv()
    _env.update(**agrs_env)

    return schema.check(_env)


def maybe_get_argv(argv=()):
    vars = {}
    argv = argv or sys.argv[1:]
    for arg in argv:
        parts = arg.split('=')
        if len(parts) != 2:
            continue
        key, val = parts[0], parts[1]
        key = key.strip('-')
        vars[key] = val
    return vars


def maybe_read_envfile(file_name):
    return {}
