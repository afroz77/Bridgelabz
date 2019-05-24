try: # Python compat < 3.3
    from collections.abc import Set, MutableSet, Hashable, Iterable
except ImportError:
    from collections import Set, MutableSet, Hashable, Iterable
from collections import defaultdict
from functools import reduce
from itertools import chain
import operator
try: # Python compat < 3.4
    from functools import partialmethod
except ImportError:
    from .common import partialmethod

class _base_multiset(Set):

    def __init__(self, items=None):
        self.__bag = {}
        if isinstance(items, Iterable):
            for i in items:
                self.__bag[i] = self.__bag.get(i, 0) + 1

    def __contains__(self, item):
        return self.__bag.get(item, 0) > 0

    def __len__(self):
        return sum(self.__bag.values())

    def __iter__(self):
        for item in self.__bag:
            for _ in range(self.__bag[item]):
                yield item

    def __le__(self, other):
        if not isinstance(other, _base_multiset) or isinstance(other, _orderable_mixin):
            raise NotImplementedError()
        return all((self.count(i) <= other.count(i)) for i in self.__bag)

    def __eq__(self, other):
        if not isinstance(other, _base_multiset):
            raise NotImplementedError()
        return all((self.count(i) == other.count(i)) for i in chain(self.__bag, other.__bag))

    def __lt__(self, other):
        return (self <= other) and not (self == other)

    def __gt__(self, other):
        if not isinstance(other, _base_multiset):
            raise NotImplementedError()
        return other < self

    def __ge__(self, other):
        if not isinstance(other, _base_multiset):
            raise NotImplementedError()
        return other <= self

    def __combine(self, amnt_op, this_op, other):
        if isinstance(other, _base_multiset):
            result = self.__class__()
            for element in chain(self.__bag, other.__bag):
                amount = amnt_op(self.count(element), other.count(element))
                if amount > 0:
                    result.__bag[element] = amount
            return result

        if isinstance(other, Iterable):
            return this_op(self, self.__class__(other))

        raise NotImplementedError()

    __sub__ = partialmethod(__combine, operator.sub, operator.sub)
    __add__ = partialmethod(__combine, operator.add, operator.add)
    __or__ = partialmethod(__combine, max, operator.or_)
    __and__ = partialmethod(__combine, min, operator.and_)
    __xor__ = partialmethod(__combine, lambda l, r: abs(l - r), operator.xor)

    def count(self, item):
        return self.__bag.get(item, 0)

    def items(self):
        return self.__bag.items()


class _orderable_mixin(object):
    # Using the Dershowitz-Manna ordering that gives a well-founded ordering
    # on multisets if the given carrier is ordered (strings, integers, etc.)
    # This fails if the union of the sets that are compared has elements that
    # are incomparible
    # https://en.wikipedia.org/wiki/Dershowitz%E2%80%93Manna_ordering

    def __le__(self, other):
        if not (isinstance(other, _orderable_mixin)):
            raise NotImplementedError()
        # using definition by Huet and Oppen
        M, N = self.count, other.count
        S = frozenset(self | other)
        ys = (y for y in S if M(y) > N(y))
        return all(any((y < x and M(x) < N(x)) for x in S) for y in ys)

    def __lt__(self, other):
        if not (isinstance(other, _orderable_mixin)):
            raise NotImplementedError()
        return self != other and self <= other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

class multiset(_base_multiset, MutableSet):
    def add(self, item):
        self._base_multiset__bag[item] = self.count(item) + 1

    def discard(self, item):
        bag = self._base_multiset__bag
        if item in bag:
            bag[item] = bag[item] - 1
            if bag[item] == 0:
                del bag[item]

class frozenmultiset(_base_multiset, Hashable):
    def __hash__(self):
        from operator import xor
        pots = (hash(key)**value for (key, value) in self.items())
        return reduce(xor, pots, hash(())) ^ hash(self.__class__)

class orderable_multiset(_orderable_mixin, multiset):
    pass

class orderable_frozenmultiset(_orderable_mixin, frozenmultiset):
    pass

class nestable_orderable_frozenmultiset(orderable_frozenmultiset):
    # Natural multiset extension for nested multisets over an orderable carrier
    # again gives a well-founded total ordering
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return super(self.__class__, self).__gt__(other)

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return super(self.__class__, self).__ge__(other)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return super(self.__class__, self).__lt__(other)

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return super(self.__class__, self).__le__(other)
