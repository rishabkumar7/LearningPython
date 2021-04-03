# This  program says hello and asks for my name.

print ('Hellow World')
print ('What is your name?') #asks for the name
myName = input()
print('it is good to meet you, ' + myName)
print('The lenght of your name is:')
print(len(myName))
print('What is your age?') #asks for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')