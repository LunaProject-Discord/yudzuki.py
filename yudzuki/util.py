def staff_value(value):
    if value == 1:
        return "staff"
    elif value == 2:
        return "admin"
    elif value == 3:
        return "subowner"
    elif value == 4:
        return "owner"
    else:
        return "default"
