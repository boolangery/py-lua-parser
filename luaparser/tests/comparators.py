def node_compare_without_char(o1, o2, msg = None):
    """ Compare a node except start_char, stop_char, start_line. """
    ignored = {'start_char', 'stop_char', 'start_line'}
    d1 = o1.__dict__
    d2 = o2.__dict__
    for k1, v1 in d1.items():
        if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
            return False
    for k2, v2 in d2.items():
        if k2 not in ignored and k2 not in d1:
            return False
    return True
