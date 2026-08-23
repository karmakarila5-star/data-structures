habit_info = ("Exercise", 5, "Health")
weekly_log = (1, 1, 0, 1, 0, 1, 1)

print("Habit Info:", habit_info)
print("Weekly Log:", weekly_log)
print("Log Length:", len(weekly_log))
print("Monday Status:", weekly_log[0])
print("Weekday Slicing:", weekly_log[0:5])

try:
    weekly_log[2] = 1
except TypeError as e:
    print("Immutability Error:", e)

log_list = list(weekly_log)
log_list[2] = 1
weekly_log = tuple(log_list)
print("Updated Log:", weekly_log)