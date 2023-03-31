cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (i for i in cities for j in range(1000000))
[print(next(gen), end= ' ') for _ in range(20)]
