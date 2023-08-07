#Napíšte program, ktorý na vstupe dostane zadaný ľubovoľný
# reťazec a na výstupe vypíše reťazec po znaku pod seba.

retazec = input('Zadaj retazec: ')

pom = 0

while pom < len(retazec):
    print(retazec[pom])
    pom += 1