duration = int(input("Введите время в секундах: "))
sec = duration % 60
min = 60
hour = 60 * 60
day = hour * 24
if duration <= min:
    print(sec, 'сек')
elif duration > min and hour >= duration :
    this_min = duration // min
    this_sec = duration % min
    print(this_min, 'мин', this_sec, 'сек')
elif duration > hour and duration < day:
    this_hour = duration // hour
    duration = duration % hour
    this_min = duration // min
    this_sec = duration % min
    print(this_hour, 'час', this_min, 'мин', this_sec, 'сек')
elif duration >= day:
   this_day = duration // day
   duration = duration % day
   this_hour = duration // hour
   duration = duration % hour
   this_min = duration // min
   this_sec = duration % min
print(this_day, 'дн', this_hour, 'час', this_min, 'мин', this_sec, 'сек')





