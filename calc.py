"""Four small arithmetic helpers. One of them is wrong."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def average(values):
    """The arithmetic mean of a non-empty list."""
    return sum(values) / len(values)


def percent_change(before, after):
    """How much `after` differs from `before`, as a percentage of `before`."""
    return (after - before) / after * 100
