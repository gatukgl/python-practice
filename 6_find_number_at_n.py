n = 120
start_number = 10
series = [start_number]
for i in range(1, n):
    prev_number = series[i - 1]
    number = prev_number + 3
    series.append(number)
print(series)
