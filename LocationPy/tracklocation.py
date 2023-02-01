import phonenumbers

# Importe o Phonenumbers

from phonenumbers import geocoder

# Importe o Geocoder 

searchNumber = input("Digite um número e o DDD: ")

phonenumber = phonenumbers.parse(searchNumber)

print(geocoder.description_for_number(phonenumber, 'en'));