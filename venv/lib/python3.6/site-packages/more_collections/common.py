def _raise(ex):
    raise ex

def partialmethod(fun, *args, **kwargs):
    def __partial(self, *_args, **_kwargs):
        kw = {}
        kw.update(kwargs)
        kw.update(_kwargs)
        return fun(self, *(args + _args), **kw)
    return __partial
