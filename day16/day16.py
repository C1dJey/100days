# POO
import turtle as t
from prettytable import PrettyTable
# screen = t.Screen()
# screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirdle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

table.align

print(table)