try: # Python 2.7 compat
    from collections.abc import Mapping, Iterable
except ImportError:
    from collections import Mapping, Iterable
from itertools import chain
from functools import reduce
from .common import _raise

def empty(_ = None):
    class __puredict(puredict_base):
        __getitem__ = lambda _, __: _raise(KeyError())
        __contains__ = lambda _, __: False
        __iter__ = lambda _: iter(())
        items = lambda _: iter(())
    return __puredict()

def insert(parent, key, value):
    class __puredict(puredict_base):
        __getitem__ = lambda _, _key: value if (key == _key) else parent[_key]
        __contains__ = lambda _, _key: (key == _key) or (_key in parent)
        __iter__ = lambda _: chain((key,), (k for k in parent if not key == k))
        items = lambda _: chain(((key, value),), ((k, v) for (k, v) in parent.items() if not key == k))
    return __puredict()

def delete(parent, key):
    class __puredict(puredict_base):
        __getitem__ = lambda _, _key: _raise(KeyError()) if (key == _key) else parent[_key]
        __contains__ = lambda _, _key: (not key == _key) and (_key in parent)
        __iter__ = lambda _: (_key for _key in parent if not key == _key)
        items = lambda _: ((k, v) for (k, v) in parent.items() if not key == k)
    return __puredict()

class puredict_base(Mapping):
    empty = empty
    insert = insert
    delete = delete
    __len__ = lambda self: sum(1 for _ in self.items())
    __hash__ = lambda self: hash(frozenset(self.items())) ^ hash(puredict_base)
    __repr__  = lambda self: repr(dict(self))

class puredict(puredict_base):
    from_iterable = staticmethod(lambda it: reduce(lambda x, y: insert(x, *y), it, empty()))
    from_mapping = staticmethod(lambda mapping: puredict.from_iterable(mapping.items()))
    __new__ = lambda cls, *args, **kwargs: \
        next((cons(args[0]) for (typeof, cons) in (
            (Mapping, cls.from_mapping),
            (Iterable, cls.from_iterable)
        ) if (args and isinstance(args[0], typeof))), cls.from_mapping(kwargs))
