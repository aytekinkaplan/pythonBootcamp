class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


# Create instances of Country
countries = [Country('India', 1300, 300), Country('China', 1400, 400), Country('USA', 1500, 500),
             Country('UK', 1600, 600), Country('Germany', 1700, 700), Country('France', 1800, 800),
             Country('Japan', 1900, 900), Country('Russia', 2000, 1000), Country('Australia', 2100, 1100),
             Country('South Africa', 2200, 1200), Country('Canada', 2300, 1300), Country('Mexico', 2400, 1400),
             Country('Brazil', 2500, 1500), Country('Argentina', 2600, 1600), Country('Colombia', 2700, 1700),
             Country('Peru', 2800, 1800), Country('Venezuela', 2900, 1900), Country('Egypt', 3000, 2000),
             Country('Nigeria', 3100, 2100), Country('Bangladesh', 3200, 2200), Country('Pakistan', 3300, 2300),
             Country('Afghanistan', 3400, 2400), Country('Philippines', 3500, 2500), Country('Indonesia', 3600, 2600),
             Country('Myanmar', 3700, 2700), Country('Thailand', 3800, 2800), Country('Vietnam', 3900, 2900),
             Country('Malaysia', 4000, 3000), Country('Singapore', 4100, 3100), Country('Hong Kong', 4200, 3200),
             Country('Taiwan', 4300, 3300), Country('South Korea', 4400, 3400), Country('Japan', 4500, 3500),
             Country('Russia', 80, 900)]

# Append a new country to the list

# Import attrgetter for sorting and finding max/min
from operator import attrgetter

# Sort countries by population in descending order
countries.sort(key=attrgetter('population'), reverse=True)
print("Sorted by population (descending):", countries)

# Find the country with the maximum population
max_population_country = max(countries, key=attrgetter('population'))
print("Country with maximum population:", max_population_country)

# Find the country with the minimum population
min_population_country = min(countries, key=attrgetter('population'))
print("Country with minimum population:", min_population_country)

# Find the country with the minimum area
min_area_country = min(countries, key=attrgetter('area'))
print("Country with minimum area:", min_area_country)

# Find the country with the maximum area
max_area_country = max(countries, key=attrgetter('area'))
print("Country with maximum area:", max_area_country)
