from collections import Counter


def get_min(match, string, last=True):
    if match is None:
        return string
    if len(match) == len(string):
        return string if last else match
    elif len(match) > len(string):
        return string
    else:
        return match


def is_match(n_count, string):
    return not bool(n_count - Counter(string))


class STATES(object):
    MEND = "MOVE_END"
    MSTART = "MOVE_START"
    EXIT = "EXIT"


def ninh(needle, haystack):
    if not needle:
        return ""
    if not haystack:
        return None
    n_count = Counter(needle)
    start = 0
    end = 0
    match = None
    state = STATES.MEND
    while True:
        if state == STATES.EXIT:
            return match
        elif state == STATES.MEND:
            end += 1
            if end > len(haystack):
                state = STATES.EXIT
                continue
            if haystack[end - 1] in n_count and is_match(
                    n_count, haystack[start:end]):
                match = get_min(match, haystack[start:end])
                state = STATES.MSTART
        elif state == STATES.MSTART:
            start += 1
            if start == end:
                state = STATES.MEND
            if is_match(n_count, haystack[start:end]):
                match = get_min(match, haystack[start:end])
            else:
                state = STATES.MEND
