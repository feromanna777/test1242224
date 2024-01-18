
# class Monster :
#     def __init__(self, name, character):
#  # Атрибут
#
#         self.Name = name
#         self.Character = character
#      # Метод
#      def show(self) :
#          print("Имя: " + self.Name)
#          print("Особенность: " + self.Character)
#
# class SMonster (Monster):
#     pass
# class GMonster (Monster):
#     pass
# Albert = GMonster("Альберт", "задумчивый")
# Albert.show()
# Sigmund = SMonster("Зигмунд", "веселый")
# Sigmund.show()


class Monster :
 # Инициализация атрибута
 def __init__(self, name, character) :
     self.Name = name
     self.Character = character
 # Метод
 def show(self) :
     print("Имя: " + self.Name)
     print("Особенность: " + self.Character)
class GMonster (Monster):
    pass

class SMonster (Monster):
    pass

Frank = Monster("Фрэнки", "необй")
Frank.show()
Albert = GMonster("Альберт", "задумчивый")
Albert.show()
Sigmund = SMonster("Зигмунд", "веселый")
Sigmund.show()