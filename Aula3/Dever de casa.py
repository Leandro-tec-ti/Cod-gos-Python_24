#Peça para o usuário o tamanho do aro da roda bike que ele quer comprar e com base nisso:
#Recomendo Tamanho do guidão, da manete e do quadro da bike
# O tamanho do guidão será metade do tamanho do aro da roda
# O tamanho do manete será 1/4 do tamanho do aro da roda
# O tamanho quadro da bike será o mesmo do aro da roda


#print("Qual tamanho do aro? ")
aro = int(input("Qual tamanho do aro? "))
Guidao = int(aro /2) 
manete = int(aro /4)
guadro = aro 
print(f"Recomdamos que o tamanho do guidão seja: {Guidao} ")
print(f"A manete que recomendamos é do tamanho: {manete}")
print(f"O quadro terá que ser do tamanho: {guadro}")

