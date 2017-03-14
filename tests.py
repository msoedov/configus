import trafaret as t

from .configus import config, maybe_get_argv


def test_basic():
    env = {'var': 'hallo', 'another_var': 'holla'}
    expected = {'var': 'hallo'}
    assert config(t.Dict(var=t.String), env) == expected


def test_argv():
    assert maybe_get_argv(['--rate=1', '--backoff=2', 'debug=1']) == {'backoff': '2', 'debug': '1', 'rate': '1'}
