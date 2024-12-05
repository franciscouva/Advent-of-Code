def get_data():
    data = open('2024/day5/data.txt').read().splitlines()
    return data

def split_lists(data):
    before_rules, after_rules, updates = [], [], []
    flag = 0
    for item in data:
        if item == '':
            flag = 1
        elif flag == 0:
            before, after = item.split('|')
            before_rules.append(int(before))
            after_rules.append(int(after))
        elif flag == 1:
            update = item.split(',')
            update_tuple = ()
            for i in update:
                update_tuple += (int(i),)
            updates.append(update_tuple)
            
    return before_rules, after_rules, updates

def get_result(before_rules, after_rules, updates):
    result = 0
    for update in updates:
        is_valid = True
        for i in range(len(update)):
            for j in range(len(before_rules)):
                if update[i] == before_rules[j] and after_rules[j] in update:
                    index_before = update.index(before_rules[j])
                    index_after = update.index(after_rules[j])
                    if index_after < index_before:
                        is_valid = False
        if is_valid:
            mid_index = len(update) // 2
            result += update[mid_index]
    return result

def get_incorrect_updates(updates, before_rules, after_rules):
    incorrect_updates = []
    for update in updates:
        is_valid = True
        for i in range(len(update)):
            for j in range(len(before_rules)):
                if update[i] == before_rules[j] and after_rules[j] in update:
                    index_before = update.index(before_rules[j])
                    index_after = update.index(after_rules[j])
                    if index_after < index_before:
                        is_valid = False
        if not is_valid:
            incorrect_updates.append(update)
    return incorrect_updates

def order_incorrect_updates(incorrect_updates, before_rules, after_rules):
    ordered_incorrect_updates = []
    for update in incorrect_updates:
        ordered_update = list(update)
        i = 0
        while i < len(update):
            for j in range(len(before_rules)):
                if update[i] == before_rules[j] and after_rules[j] in update:
                    index_before = ordered_update.index(before_rules[j])
                    index_after = ordered_update.index(after_rules[j])
                    if index_after < index_before:
                        ordered_update[index_before], ordered_update[index_after] = ordered_update[index_after], ordered_update[index_before]
                        i = -1
                        break
            i += 1
        ordered_incorrect_updates.append(tuple(ordered_update))
    return ordered_incorrect_updates
                    
if __name__ == '__main__':
    # part 1
    data = get_data()
    before_rules, after_rules, updates = split_lists(data)
    result = get_result(before_rules, after_rules, updates)
    print(f"Result: {result}")
    # part 2
    incorrect_updates = get_incorrect_updates(updates, before_rules, after_rules)
    ordered_incorrect_updates = order_incorrect_updates(incorrect_updates, before_rules, after_rules)
    result2 = get_result(before_rules, after_rules, ordered_incorrect_updates)
    print(f"Result 2: {result2}")