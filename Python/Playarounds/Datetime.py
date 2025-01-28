from datetime import datetime, date, timedelta

now = datetime.now()

Days = {
    1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th', 10: 'th',
    11: 'th', 12: 'th', 13: 'th', 14: 'th', 15: 'th', 16: 'th', 17: 'th', 18: 'th', 19: 'th', 20: 'th',
    21: 'st', 22: 'nd', 23: 'rd', 24: 'th', 25: 'th', 26: 'th', 27: 'th', 28: 'th', 29: 'th', 30: 'th',
    31: 'st'
}

Months = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December',
}

wordMonth = Months.get(now.month)
wordDay = Days.get(now.day)

print(f"\nToday's date: {date.today()}\nDay: {now.day}{wordDay}\nMonth: {wordMonth}\nYear: {now.year} years\nHour: {now.hour} hours\nMinute: {now.minute} minutes\nSecond: {now.second} seconds\n")
