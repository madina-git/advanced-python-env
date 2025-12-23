def all_eq(lst):
    max_len = 0

    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []

    
    for s in lst:
        while len(s) < max_len:
            s = s + "_"
        result.append(s)

    return result
