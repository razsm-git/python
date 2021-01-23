time = int(input("Введите кол-во секунд: "))
sec = None
minute = None
hour = None
if time < 60:
    hour = 0
    minute = 0
    sec = time
elif 60 <= time < 3600:
    hour = 0
    minute = time // 60
    sec = time % 60
else:
    hour = time // 3600
    minute = time % 3600 // 60
    sec = time % 3600 % 60
if sec < 10:
    sec = "0" + str(sec)
if minute < 10:
    minute = "0" + str(minute)
if hour < 10:
    hour = "0" + str(hour)
new_time = f"Вы ввели {time}c, это {hour}:{minute}:{sec}"
print(new_time)

