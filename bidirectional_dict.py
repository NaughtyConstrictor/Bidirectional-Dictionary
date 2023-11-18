from collections import UserDict
from collections.abc import MutableMapping


class BidirDict_V1(dict):

    POP_DEFAULT = object()

    def __init__(self, *args, **kwargs):
        self.update(dict(*args, **kwargs))

    def __delitem__(self, key):
        value = super().pop(key)
        super().pop(value)

    def pop(self, key, default=POP_DEFAULT):
        try:
            value = self[key]
        except KeyError:
            if default is not self.POP_DEFAULT:
                return default
            else:
                raise
        del self[key]
        return value

    def popitem(self):
        pair_1 = super().popitem()
        pair_2 = super().popitem()
        return [pair_2, pair_1]

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)
    
    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
            return default
        return self[key]

    def update(self, *args, **kwargs):
        mapping = dict(*args, **kwargs)
        for key, value in mapping.items():
            self[key] = value

    @classmethod
    def fromkeys(cls, *args, **kwargs):
        raise NotImplementedError(
            f"{cls.__name__}.fromkeys() is undefined."
        )

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"


class BidirDict_V2(UserDict):

    def __delitem__(self, key):
        value = self.data.pop(key)
        self.data.pop(value)
    
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        self.data[key] = value
        self.data[value] = key

    def popitem(self):
        pair_1 = self.data.popitem()
        pair_2 = self.data.popitem()
        return [pair_2, pair_1]

    @classmethod
    def fromkeys(cls, *args, **kwargs):
        raise NotImplementedError(
            f"{cls.__name__}.fromkeys() is undefined."
        )

    def __eq__(self, other):
        return self.data == other

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"


class BidirDict_V3(MutableMapping):

    def __init__(self, *args, **kwargs):
        self.mapping = {}
        self.update(*args, **kwargs)
    
    def __getitem__(self, key):
        return self.mapping[key]
    
    def __delitem__(self, key):
        value = self.mapping.pop(key)
        self.mapping.pop(value)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        self.mapping[key] = value
        self.mapping[value] = key
    
    def __iter__(self):
        return iter(self.mapping)
    
    def __len__(self):
        return len(self.mapping)

    def popitem(self):
        pair_1 = self.mapping.popitem()
        pair_2 = self.mapping.popitem()
        return [pair_2, pair_1]

    @classmethod
    def fromkeys(cls, *args, **kwargs):
        raise NotImplementedError(
            f"{cls.__name__}.fromkeys() is undefined."
        )

    def __repr__(self):
        return f"{type(self).__name__}({self.mapping!r})"


if __name__ == "__main__":
    BidirDict = BidirDict_V3
    d = BidirDict()
    # print(d)
    d['a'] = 1
    d['b'] = 2
    # print(d)
    d.update([("a", 2), ("b", 1)], c=3)
    print(d != {'a': 2, 2: 'a', 'b': 1, 1: 'b', 3: 'c', 'c':3})
    print(d)
