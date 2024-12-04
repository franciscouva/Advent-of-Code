def get_data():
    data = open('2024/day4/data.txt').read().splitlines()
    return data

def check_right(data, lin, col):
    if col >= len(data[lin])-3:
        return False
    
    if data[lin][col:col+4] == 'XMAS':
        return True
    
def check_left(data, lin, col):
    if col < 3:
        return False
    
    if data[lin][col-3:col+1] == 'SAMX':
        return True
    
def check_down(data, lin, col):
    if lin >= len(data)-3:
        return False
    
    if data[lin][col] == 'X' and data[lin+1][col] == 'M' and data[lin+2][col] == 'A' and data[lin+3][col] == 'S':
        return True
    
def check_up(data, lin, col):
    if lin < 3:
        return False
    
    if data[lin-3][col] == 'S' and data[lin-2][col] == 'A' and data[lin-1][col] == 'M' and data[lin][col] == 'X':
        return True
    
def check_diag_up_right(data, lin, col):
    if lin < 3 or col >= len(data[lin])-3:
        return False
    
    if data[lin-3][col+3] == 'S' and data[lin-2][col+2] == 'A' and data[lin-1][col+1] == 'M' and data[lin][col] == 'X':
        return True
    
def check_diag_up_left(data, lin, col):
    if lin < 3 or col < 3:
        return False
    
    if data[lin-3][col-3] == 'S' and data[lin-2][col-2] == 'A' and data[lin-1][col-1] == 'M' and data[lin][col] == 'X':
        return True
    
def check_diag_down_right(data, lin, col):
    if lin >= len(data)-3 or col >= len(data[lin])-3:
        return False
    
    if data[lin][col] == 'X' and data[lin+1][col+1] == 'M' and data[lin+2][col+2] == 'A' and data[lin+3][col+3] == 'S':
        return True
    
def check_diag_down_left(data, lin, col):
    if lin >= len(data)-3 or col < 3:
        return False
    
    if data[lin][col] == 'X' and data[lin+1][col-1] == 'M' and data[lin+2][col-2] == 'A' and data[lin+3][col-3] == 'S':
        return True
    
    
def count_xmas(data):
    count = 0
    for lin in range(len(data)):
        for col in range(len(data[lin])):
            if data[lin][col] == 'X':
                if check_right(data, lin, col): count += 1
                if check_left(data, lin, col): count += 1
                if check_down(data, lin, col): count += 1
                if check_up(data, lin, col): count += 1
                if check_diag_up_right(data, lin, col): count += 1
                if check_diag_up_left(data, lin, col): count += 1
                if check_diag_down_right(data, lin, col): count += 1
                if check_diag_down_left(data, lin, col): count += 1
    return count

def check_mas_diag_up_right(data, lin, col):
    if lin < 2 or col >= len(data[lin])-2:
        return False
    
    if data[lin][col] == 'M' and data[lin-1][col+1] == 'A' and data[lin-2][col+2] == 'S':
        return True
    
def check_mas_diag_up_left(data, lin, col):
    if lin < 2 or col < 2:
        return False
    
    if data[lin][col] == 'M' and data[lin-1][col-1] == 'A' and data[lin-2][col-2] == 'S':
        return True
    
def check_mas_diag_down_right(data, lin, col):
    if lin >= len(data)-2 or col >= len(data[lin])-2:
        return False
    
    if data[lin][col] == 'M' and data[lin+1][col+1] == 'A' and data[lin+2][col+2] == 'S':
        return True
    
def check_mas_diag_down_left(data, lin, col):
    if lin >= len(data)-2 or col < 2:
        return False
    
    if data[lin][col] == 'M' and data[lin+1][col-1] == 'A' and data[lin+2][col-2] == 'S':
        return True
    
def count_mas(data):
    count = 0
    for lin in range(len(data)):
        for col in range(len(data[lin])):
            if data[lin][col] == 'M':
                if check_mas_diag_up_right(data, lin, col):
                    if check_mas_diag_down_right(data, lin-2, col) or check_mas_diag_up_left(data, lin, col+2): count += 1
                if check_mas_diag_up_left(data, lin, col):
                    if check_mas_diag_down_left(data, lin-2, col) or check_mas_diag_up_right(data, lin, col-2): count += 1
                if check_mas_diag_down_right(data, lin, col):
                    if check_mas_diag_up_right(data, lin+2, col) or check_mas_diag_down_left(data, lin, col+2): count += 1
                if check_mas_diag_down_left(data, lin, col):
                    if check_mas_diag_up_left(data, lin+2, col) or check_mas_diag_down_right(data, lin, col-2): count += 1
    return count

if __name__ == '__main__':
    # part 1
    data = get_data()
    count = count_xmas(data)
    print(f"Number of XMAS: {count}")
    # part 2
    count = int(count_mas(data) / 2) # because we are counting twice
    print(f"Number of X-MAS: {count}")
    