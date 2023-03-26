# class Human
#   location = "Новосибирск" #public statik
#   __priv = "что-то"   #private static
#
#     def __init__(self, rost=1, ves=100):
#         self.height = rost
#         self.__jir = ves
#
# def public(self):
#     pass
#
# def __private(self):
#     pass
#
#
# peson = Human(47)
# print(peson.height)
# print(peson.jir)



class Human:
    default_name = "Valera"
    default_age = 23
      def __init__(self, lav=default_name, ner=default_age):
        self.name = lav
        self.age = ner
        self.__money = 1000
        self.__house = None

      def info(self):
          return self.name, self.age, self.__money, self.__house.

#Чясть 2
 class House:
     def __init__(self, ar, pr):
         self._area = ar
         self._price = pr
     def final_price(self):
         return self.__price - (self.__price * self.skidka)

Valera = Human()
dom1 = House("Новосибирск", 500)
print(dom1.final_price())
print(dom1.
class House:


















      )
