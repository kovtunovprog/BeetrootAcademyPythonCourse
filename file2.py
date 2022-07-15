#Task 2
#Creating a dictionary.
#Create a function called make_country, which takes in a country’s name and capital as parameters.
#Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
#Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(country, capital):
    country_dict = {country:capital}
    print(country_dict)
make_country('Ukraine', 'Kiyv')