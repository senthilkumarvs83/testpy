
def kelvinToFarenheit(temperature):
    assert(temperature >=0 ),'colder that absolute zero'
    return((temperature-273)*1.8)+32


print(kelvinToFarenheit(-9))