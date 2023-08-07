# napiste program, ktory nacita na vstupe lubovolny text  a nahradi vsetky
# ahoj inym lubovolnym slovom.
# a vypise aj povodny aj upraveny retazec

retazec = input('zadaj lubovolny text: ')
retazecUpraveny = retazec.replace('ahoj', 'hello')

print(retazec)
print(retazecUpraveny)