numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

lengths_of_numbers = [len(number) for number in numbers]
print(lengths_of_numbers)

states_of_usa = ['California', 'New York', 'Florida', 'Texas', 'Arizona', 'Alaska', 'Hawaii', 'Pennsylvania',
                 'Illinois', 'Georgia']
states_of_america = [state.upper() for state in states_of_usa]
print(states_of_america)

cars = ['Ford', 'Chevy', 'Toyota', 'BMW', 'Mercedes', 'Nissan', 'Honda', 'Hyundai', 'Kia', 'Mazda']

cars_with_m = [car for car in cars if 'm' in car.lower()]
print(cars_with_m)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

short_planets = [planet for planet in planets if len(planet) < 5]
print(short_planets)

planets_with_v = [planet for planet in planets if 'v' in planet.lower()]
print(planets_with_v)

plants = ['Cactus', 'Cabbage', 'Cucumber', 'Cucumber', 'Eggplant', 'Garlic', 'Garlic', 'Jalapeno', 'Kale', 'Kale']

unique_plants = list(set(plants))
print(unique_plants)

fruit = ['Apple', 'Banana', 'Orange', 'Pear', 'Pear', 'Pear', 'Pear', 'Pear', 'Pear', 'Pear', 'Pear']

unique_fruits = list(set(fruit))
print(unique_fruits)

