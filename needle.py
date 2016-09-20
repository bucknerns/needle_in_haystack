from collections import Counter


def get_min(match, string, last=False):
    if match is None:
        return string
    if len(match) == len(string):
        return string if last else match
    elif len(match) > len(string):
        return string
    else:
        return match


def is_match(n_count, s_count):
    return not bool(n_count - s_count)


class STATES(object):
    MEND = "MOVE_END"
    MSTART = "MOVE_START"


def ninh(needle, haystack, last=False):
    if not needle:
        return ""
    if not haystack:
        return None
    n_count = Counter(needle)
    s_count = Counter()
    start = 0
    end = 0
    match = None
    state = STATES.MEND
    while True:
        if state == STATES.MEND:
            end += 1
            if end > len(haystack):
                break
            s_count.update(haystack[end - 1])
            if is_match(n_count, s_count):
                match = get_min(match, haystack[start:end], last)
                state = STATES.MSTART
        elif state == STATES.MSTART:
            start += 1
            s_count.subtract(haystack[start - 1])
            if start == end:
                state = STATES.MEND
                continue
            if is_match(n_count, s_count):
                match = get_min(match, haystack[start:end], last)
            else:
                state = STATES.MEND
    return match
