""" Graph edge entity - Line
"""

class Line(object):
    """
    Line entity defined by:
    two points (p0, p1),
    length,
    unique id
    """
    def __init__(self, idx, length, p0, p1):
        self.idx = idx
        self.length = length
        self.point = (p0, p1)
