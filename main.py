from src.Elements import AlgebraicStructure
from src.FirstOrder import Identity

print(AlgebraicStructure({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y}, {Identity({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, lambda x, y: x + y == y + x)}))