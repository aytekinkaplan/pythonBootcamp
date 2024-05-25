def provide_weather_advisory(temperature):
    if temperature < 0:
        return "It's freezing! Wear a heavy coat."
    elif 0 <= temperature <= 10:
        return "It's cold! Bundle up."
    elif 11 <= temperature <= 20:
        return "It's cool! A light jacket will do."
    else:
        return "It's warm! Enjoy the day."


# Example usage:
print(provide_weather_advisory(-5))  # Output: "It's freezing! Wear a heavy coat."
print(provide_weather_advisory(5))  # Output: "It's cold! Bundle up."
print(provide_weather_advisory(15))  # Output: "It's cool! A light jacket will do."
print(provide_weather_advisory(25))  # Output: "It's warm! Enjoy the day."
