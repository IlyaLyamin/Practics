from class_1 import *

PC = Computer(color="green", size=14, weight=3, password="123")
PC.turn_on(password="111") # неудачная поптка включить пк
PC.turn_on(password="123") # удачная попытка включить пк
PC.change_password(old_password="123", new_password="321") # смена пароля
PC.check_memory()
print()
PC.download("игра")
print()
PC.download("книга")
print()
PC.download("книга")
print()
PC.download("фильм")
print()
PC.delete(5)
print()
PC.delete(3)
print()
PC.check_memory()
print()
PC.download("фильм")
print()
PC.check_memory()
print()
PC.turn_of() # выключение
# создание нового объекта и проверка на наследование 
Game_Pc = GameComputer(color="black", size=17, weight=2, password="111")
print(PC)
print()
Game_Pc.turn_on(password="111")
print(Game_Pc)
Game_Pc.change_password(old_password="111", new_password="222")
Game_Pc.turn_of()
Game_Pc.turn_on(password="222")
Game_Pc.download(obj="игра")
Game_Pc.download(obj="игра")
Game_Pc.download(obj="игра")
Game_Pc.download(obj="игра")
Game_Pc.download(obj="игра")
Game_Pc.check_memory()
Game_Pc.delete(4)
print(PC < Game_Pc)
print(PC == Game_Pc)
print(PC > Game_Pc)
