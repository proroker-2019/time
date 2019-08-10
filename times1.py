import datetime
import sys
time = datetime.datetime.now()


def func(time):
    if input("Введите запрос: ") == "Время":
        print(str(time.hour) + ":" + (str(time.minute)))
    if input("Введите запрос: ") == "Выход":
        print("Выхожу!")
        sys.exit()
    return func(time)


func(time)

#except .KeyboardInterrupt:
    #print("Неизвестный запрос!")












