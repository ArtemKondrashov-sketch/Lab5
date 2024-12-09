#day of programmist
def find_a_date(n):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = 0
    while n > months[month]:
        n -= months[month]
        month += 1
        return n, month + 1
    n = int(input())
    day, month = find_a_date(n)
    print(f" a date {month}.")