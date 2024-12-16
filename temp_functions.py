def fahr_to_celsius(temp_fahrenheit):
    """
    This function changes a temperature from Fahrenheit to Celsius degrees.
    
    temp_fahrenheit: The temperature in Fahrenheit.
    
    Returns the temperature in Celsius degrees.
    """
    converted_temp = (temp_fahrenheit - 32) * 5 / 9    # This converts the Fahrenheit temperature to Celsius
    return converted_temp    # Returns the result


def temp_classifier(temp_celsius):
    """
    This function classifies a temperature into the suitable category:
    0 - Temperatures less than -2 degrees
    1 - Temperatures between -2 and +2 or equal to -2 or +2 degrees
    2 - Temperatures between 2 and 15 or equal to 2 or 15 degeres
    3 - Temperatures equal or higher than 15 degrees 

    Parameter temp_celsius represents the temperature that will be classified

    """
    # Classification into 4 categories
    if temp_celsius < -2:  # Category 0
        return 0
    elif -2 <= temp_celsius < 2:  # Category 1
        return 1
    elif 2 <= temp_celsius < 15:  # Category 2
        return 2
    else:  # Category 3
        return 3

""" 
This is exercise 4 part 3. This script file contains two functions. Made by Lotta Ahomäki.

"""
