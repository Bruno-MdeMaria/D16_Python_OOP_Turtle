from asyncio import FIRST_EXCEPTION
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Eletric","Fire", "Water"])
table.("r")
print(table)