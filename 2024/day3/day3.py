import re

def get_data():
    data = open('2024/day3/data.txt').read()
    return data

def get_muls(data):
    mul = r"mul\(\d+,\d+\)"
    muls = re.findall(mul, data)
    for i in range(len(muls)):
        muls[i] = muls[i].replace('mul(', '')
        muls[i] = muls[i].replace(')', '')
        n1, n2 = muls[i].split(',')
        muls[i] = (int(n1), int(n2))
        
    return muls

def get_muls_and_dos(data):
    mul_and_do = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    muls_and_dos = re.findall(mul_and_do, data)
    return muls_and_dos

def remove_muls(muls):
    remove = False
    for i in range(len(muls)):
        
        if muls[i] == "do()":
            remove = False
            muls[i] = None
        elif muls[i] == "don't()":
            remove = True
            muls[i] = None
        elif remove:
            muls[i] = None
        
    muls = [x for x in muls if x is not None]
    
    for i in range(len(muls)):
        muls[i] = muls[i].replace('mul(', '')
        muls[i] = muls[i].replace(')', '')
        n1, n2 = muls[i].split(',')
        muls[i] = (int(n1), int(n2))
            
    return muls   
            

def get_muls_sum(muls):
    sum = 0
    for mul in muls:
        sum += mul[0] * mul[1]
        
    return sum

if __name__ == '__main__':
    data = get_data()
    # part 1
    muls = get_muls(data)
    muls_sum = get_muls_sum(muls)
    print(f"Sum of all muls: {muls_sum}")
    # part 2
    muls_and_dos = get_muls_and_dos(data)
    muls_and_dos = remove_muls(muls_and_dos)
    muls_sum = get_muls_sum(muls_and_dos)
    print(f"Sum of all muls after dos and don'ts: {muls_sum}")