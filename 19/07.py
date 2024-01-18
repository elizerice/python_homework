def same_by(criterion, objects):
    result_set = set(map(criterion, objects))
    if len(result_set) > 1:
        return False
    else:
        return True
