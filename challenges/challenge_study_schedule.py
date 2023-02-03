def study_schedule(permanence_period, target_time):
    count = 0
    if not isinstance(target_time, int):
        return None
    for tupla in permanence_period:
        if isinstance(tupla[0], int) and isinstance(tupla[1], int):
            if tupla[0] <= target_time and tupla[1] >= target_time:
                count += 1
        else:
            return None

    return count
