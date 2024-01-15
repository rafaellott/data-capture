from collections import namedtuple

SingleStat = namedtuple("SingleStat", "current, lower, greater")


class _DataStats:

    def __init__(self, data, lowest, highest):
        self._data = data
        self._lowest = lowest
        self._highest = highest

    def _get_default_el(self, value):
        if value < self._lowest:
            el = self._data[self._lowest]
            return SingleStat(current=0, lower=el.lower, greater=(el.current + el.greater))

        if value > self._highest:
            el = self._data[self._highest]
            return SingleStat(current=0, lower=(el.current + el.lower), greater=el.greater)

    def _check_ends(self, value, operation):
        el = self._get_default_el(value)
        if not el:
            return None

        val = getattr(el, operation)
        if value < self._lowest and operation == 'greater':
            val += el.current
        if value > self._highest and operation == 'lower':
            val += el.current
        return val

    def __lt__(self, other):
        other = int(other)
        check = self._check_ends(other, 'lower')
        return self._data[other].lower if check is None else check

    def __gt__(self, other):
        other = int(other)
        check = self._check_ends(other, 'greater')
        return self._data[other].greater if check is None else check

    def less(self, value):
        value = int(value)
        return self < value

    def greater(self, value):
        value = int(value)
        return self > value

    def between(self, start, end):
        start = int(start)
        end = int(end)
        start_el = self._data.get(start) or self._get_default_el(start)
        end_el = self._data.get(end) or self._get_default_el(end)
        a = start_el.greater
        b = end_el.greater
        c = abs(a - b)
        if self._data.get(start):
            return c + start_el.current
        return c


class DataCapture:

    def __init__(self):
        self._internal_data = {}
        self._total = 0
        self._lowest = 1000
        self._highest = 0

    def add(self, number):
        number = int(number)
        if 0 < number <= 1000:
            self._total += 1
            if not self._internal_data.get(number):
                self._internal_data[number] = 1
            else:
                self._internal_data[number] += 1
            if number < self._lowest:
                self._lowest = number
            if number > self._highest:
                self._highest = number
        else:
            raise ValueError(
                "Invalid value '%s'. Please provide a value between 1 and 1000.", number
            )

    def build_stats(self):
        stats = {}
        prev = 0
        for index in range(self._lowest, self._highest + 1):
            value = self._internal_data.get(index, 0)
            g = (self._total - prev - value)
            stats[index] = SingleStat(current=value, lower=prev, greater=g)
            prev += value
        return _DataStats(data=stats, lowest=self._lowest, highest=self._highest)
