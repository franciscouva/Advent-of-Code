def get_reports():
    data = open('2024/day2/data.txt').read().splitlines()

    reports = []

    for line in data:
        tup = ()
        for num in line.split(' '):
            tup += (int(num),)
        reports.append(tup)
    
    return reports

def report_is_asc_or_desc(report):
    report_asc = tuple(sorted(report))
    report_desc = tuple(sorted(report, reverse=True))
    
    if report_asc == report:
        return True
    elif report_desc == report:
        return True
    else:
        return False
    
def report_levels_are_valid(report):
    for i in range(len(report)-1):
        difference = abs(report[i] - report[i + 1])
        if difference > 3 or difference == 0:
            return False
        
    return True


def is_safe_report(report):
    if report_is_asc_or_desc(report) and report_levels_are_valid(report):
        return True
    else:
        return False

def is_safe_report_problem_dampener(report):
    for i in range(len(report)):
        report_without_item = report[:i] + report[i+1:]
        if is_safe_report(report_without_item):
            return True
    return False
    
def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
            
    return count

def count_safe_reports_with_problem_dampener(reports):
    count = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
        elif is_safe_report_problem_dampener(report):
            count += 1
            
    return count

        
if __name__ == '__main__':
    # part 1
    reports = get_reports()
    safe_reports = count_safe_reports(reports)
    print(f"Safe reports: {safe_reports}")
    # part 2
    safe_reports_with_problem_dampener = count_safe_reports_with_problem_dampener(reports)
    print(f"Safe reports with problem dampener: {safe_reports_with_problem_dampener}")