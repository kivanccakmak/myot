#!/bin/python3
"""
helper methods
"""
import json

def read_json(fname):
    """
    :fname: Str
    :return: dict
    """
    with open(fname, 'r') as datafile:
        data = json.load(datafile)
    return data

def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 +
            obj.microsecond / 1000
        )
        return millis
    raise TypeError('Not sure how to serialize %s' % (obj,))

def write_json(fname, data):
    """
    :fname: Str
    :data: dict
    """
    with open(fname, "w") as datafile:
        json.dump(data, datafile, indent=1, default=default)
