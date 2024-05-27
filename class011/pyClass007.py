class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area


list_of_countries = [
    Country("India", 1300, 300),
    Country("China", 1400, 400),
    Country("USA", 1500, 500),
    Country("UK", 1600, 600),
    Country("Germany", 1700, 700),
    Country("France", 1800, 800),
    Country("Japan", 1900, 900),
    Country("Russia", 2000, 1000),
    Country("Australia", 2100, 1100),
    Country("South Africa", 2200, 1200),
]

for country in list_of_countries:
    print(f"Country: {country.name}", f"Population: {country.population}", f"Area: {country.area}")
