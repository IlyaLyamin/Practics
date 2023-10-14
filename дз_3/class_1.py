from random import choices


class Computer:
    type_pc = "обычный пк"
    vin = "".join(choices(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"], k=8))
    def __init__(self, color=str, size=int, weight=int, password=str):
        self._color, self._size, self._weight = color, size, weight
        self._password = password
        self.energo = False
        self.ram = 4 # оперативная память
        self.video_mem = 2 # видеопамять
        self.hd = [] # жёсткий диск
        self.memory = 35 # память
        self.type_pc = "обычный пк"
    
    def change_password(self, old_password=str, new_password=str):
        if self.energo == True:
            if old_password == self._password:
                self._password = new_password
            else:
                print("Пароль неверный")
        else:
            print("Включите компьютер")
    
    def turn_on(self, password=str):
        if self.energo == False:
            if password == self._password:
                self.energo = True
                print("Компьютер включен")
            else:
                print("Пароль неверный")
        else:
            print("Компьютер включен")
    
    def turn_of(self):
        self.energo = False
        print("Компьютер выключен")
    
    def download(self, obj=str):
        """можно скачать: фильм, игру, книгу"""
        if self.energo == True:
            obj_dict = {"фильм": 10,
                        "игра": 20,
                        "книга": 5}
            if (sum(self.hd) + obj_dict[obj]) <= self.memory:
                self.hd.append(obj_dict[obj])
                print(f"{obj} скачен(а)")
            else:
                print(f"Не хватает {obj_dict[obj] - (self.memory - sum(self.hd))} гб памяти, удалите что-нибудь")
        else:
            print("Включите компьютер")

    def delete(self, obj=int):
        """удаление происходит по индексу объекта"""
        if (obj - 1) <= len(self.hd):
            del self.hd[obj - 1]
            print(f"свободно {self.memory - sum(self.hd)} гб")
        else:
            print("повторите запрос")

    def check_memory(self):
        if self.energo == True:
            print(self.memory - sum(self.hd), "гб свободно")
            for i in range(len(self.hd)):
                print(i + 1, "->", self.hd[i])
        else:
            print("Включите компьютер")

    def __repr__(self) -> str:
        return f"""--------------------
{self.type_pc}\nОЗУ: {self.ram}
Видео память: {self.video_mem}\nВстроенная память: {self.memory}
цвет: {self._color}\nДиагональ: {self._size}
--------------------"""
    
    def __lt__(self, other):
        if ((self.video_mem * 2 + self.ram) / 2) < ((other.video_mem * 2 + other.ram) / 2):
            return True
        return False
        
    def __eq__(self, object) -> bool:
        if ((self.video_mem * 2 + self.ram) / 2) == ((object.video_mem * 2 + object.ram) / 2):
            return True
        return False
    
    def __gt__(self, object):
        if ((self.video_mem * 2 + self.ram) / 2) > ((object.video_mem * 2 + object.ram) / 2):
            return True
        return False

class GameComputer(Computer):
    type_pc = "игровой пк"
    vin = "".join(choices(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"], k=8))
    def __init__(self, color=str, size=int, weight=int, password=str):
        super().__init__(color=str, size=int, weight=int, password=str)
        self._color, self._size, self._weight = color, size, weight
        self._password = password
        self.ram = 16 # оперативная память
        self.video_mem = 12 # видеопамять
        self.hd = [] # жёсткий диск
        self.memory = 80 # память
        self.type_pc = "игровой пк"

    def change_video_memory(self, new_v_memory):
        self.video_mem = new_v_memory

    def change_memory(self, new_memory):
        self.memory = new_memory

    def change_ram(self, new_ram):
        self.ram = new_ram

    def play(self):
        if (self.ram + self.video_mem) > 20:
            print("Игра запущена")
        else:
            print("Обновите железо")