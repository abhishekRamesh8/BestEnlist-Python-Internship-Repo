# Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature
# should be 98 degree


def covid(name, temp='98 degree'):
    return f'Patient name is {name} and temperature is {temp}'


print(covid(input('Enter the patients name: ')))
