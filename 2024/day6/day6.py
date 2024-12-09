def get_data():
    data = open("2024/day6/data.txt", "r").read().splitlines()
    for line in range(len(data)):
        data[line] = list(data[line])
    return data
    
def get_lin_col_guard(data):
    lin, col = 0, 0
    for i in range(len(data)):
        if '^' in data[i]:
            lin = i
            col = data[i].index('^')
            break
    return lin, col


def predict_route(data, lin, col):
    guard = data[lin][col]
    count = 0
    if lin == -1 or col == -1 or lin == len(data) or col == len(data[0]):
        return count
    
    while True:
        if lin == -1 or col == -1 or lin == len(data) or col == len(data[0]):
            return count
        
        if data[lin][col] != 'X' and data[lin][col] != '#': count += 1
        
        if data[lin][col] == '#':
            if guard == 'v':
                guard = '<'
                lin -= 1
            elif guard == '^':
                guard = '>'
                lin += 1
            elif guard == '<':
                guard = '^'
                col += 1
            elif guard == '>':
                guard = 'v'
                col -= 1
                
        data[lin][col] = 'X'
        
        if guard == 'v':
            lin += 1
        elif guard == '^':
            lin -= 1
        elif guard == '<':
            col -= 1
        elif guard == '>':
            col += 1
        
if __name__ == "__main__":
    # part 1
    data = get_data()
    lin, col = get_lin_col_guard(data)
    result = predict_route(data, lin, col)
    print(f"Distinct positions: {result}")
    # part 2
    