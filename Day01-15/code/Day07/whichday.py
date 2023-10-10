def is_leapyear(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
# def which_day(year,month,day):
#     month_normal = {zip([i for i in range(1,13)],
#                         [31,28,31,30,31,30,31,31,30,31,30,31])}
#     month_leap = {zip([i for i in range(1,13)],
#                         [31,29,31,30,31,30,31,31,30,31,30,31])}
#     if is_leapyear(year):
#         for key in range(1,month+1):
#             days += month_leap[key]
#     else:
#         for key in range(1,month+1):
#             days += month_normal[key]
#     return days

def which_day(year,month,day):
    month_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_leap =   [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    if is_leapyear(year):
        for i in range(month-1):
            days += month_leap[i]
        days += day
    else:
        for i in range(month-1):
            days += month_normal[i]
        days += day
    return days


print(which_day(2023,2,15))
