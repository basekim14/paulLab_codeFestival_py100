# Code Festival - Python Practice 068
# Author : ㄱㄱㅊ
# Title : Bus Timetable
# Date : 20-04-20

def covert_time(time):
    if str(time).isdigit():
        return '{0:>02d}시간 {1:>02d}분'.format(time // 60, time % 60)
    else:
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute

def check_bt(bt, time):
    bt = [covert_time(bt[i]) for i in range(len(bt))]
    time = covert_time(time)
    result = [''] * len(bt)
    for i in range(len(bt)):
        if bt[i] < time:
            result[i] = '지나갔습니다'
        else:
            result[i] = covert_time(bt[i] - time)
            
    return result

bt = input().split()
time = input()
print(check_bt(bt, time))
