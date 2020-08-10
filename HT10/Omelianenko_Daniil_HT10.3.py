def parse(rules):
    result = []
    initial_val = 0
    for rule in rules:
        if rule == 'i':
            initial_val += 1
        elif rule == 's':
            initial_val *= initial_val #initial_val **2
        elif rule == 'd':
            initial_val -= 1
        elif rule == 'o':
            result.append(initial_val)
    return result

print (parse("iiisdoso"))
