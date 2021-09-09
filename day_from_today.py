def forwarded_days(day, skip_days):
    days = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}
    day = day.lower()
    if day not in days:
        return "Invalid Day"
    key_list = list(days.keys())
    val_list = list(days.values())
    day_value = days.get(day)
    remainder_days = skip_days % 7
    resultant_day_value = (day_value + remainder_days) % 7
    position = val_list.index(resultant_day_value)
    resultant_day = key_list[position]
    return resultant_day


if __name__ == '__main__':
    print(forwarded_days('Sriday', 100))
