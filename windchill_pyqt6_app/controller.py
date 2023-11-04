"""
controller.py by Chris Winikka
Some functions to control our windchill app.
"""
# imports


# Functions
def get_windchill(temp: int, speed: int) -> str:
    """ calculates windchill and returns results """
    results = ""
    windchill = (35.74 + 0.6215 * temp - 35.75 * (speed**0.16) +
                 0.4275 * temp * (speed**0.16))
    windchill = round(windchill, 2)
    results = f"With a windspeed of {speed} mph and "
    results += f"a temperature of {temp}F, it feels "
    results += f" like it's {windchill} degrees Fahrenheit."
    return results


# Variables
credits = "Yo, it's Winikka"

# Global scope
if __name__ == "__main__":
    # test your functions here.
    results = get_windchill(-45, 60)
    print(results)
