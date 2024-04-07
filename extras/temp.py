'''
Implement the transform_temperature_data function to process a dictionary, temperature_data, representing temperature readings for various dates. Structure of 
Temperature_data:{‘01-01-2020’:[10,20,30] }  , where every key  is the date, and every value is the list of temperatures for that date.

For each date , remove non-numeric characters except hyphen(“-”) in between day,month and year, and calculate the maximum, minimum, and the average temperatures. Store the transformed data in a new dictionary named result, where each date is a key(type will be string), and the corresponding value is a dictionary containing “max_temp”,”min_temp” and “average_temp” . Return the final result dictionary.

In the input section there will be two more inputs  n_date and kind  which will be used in extracting the kind of temperature (from min, max and average) from the n_date.

Note: - Round off the average temperatures to a 2 decimal points.
'''
def transform_temperature_data(temperature_data, n_date, kind):
    result = {}
    for date, temperatures in temperature_data.items():
        # Remove non-numeric characters except hyphen
        cleaned_date = ''.join(c if c.isdigit() or c == '-' else '' for c in date)
        # Calculate max, min, and average temperatures
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        avg_temp = round(sum(temperatures) / len(temperatures), 2)
        # Store the transformed data in the result dictionary
        result[cleaned_date] = {
            'max_temp': max_temp,
            'min_temp': min_temp,
            'average_temp': avg_temp
        }

    # Extract the required kind of temperature from the n_date
    if n_date in result:
        return result[n_date][kind]
    else:
        return "Date not found in the temperature data."

# Example usage:
temperature_data = {'01-01-2020': [10, 20, 30], '02-01-2020': [15, 25, 35]}
n_date = '01-01-2020'
kind = 'max_temp'
result = transform_temperature_data(temperature_data, n_date, kind)
print(result)  # Output: 30
