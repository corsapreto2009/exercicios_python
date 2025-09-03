idade = int(input("quantos anos você tem, meu chapa? "))

if idade < 16:
    print("você jovem demais pra votar... talvez mais uns anos pra frentes")
elif 15 < idade < 18:
    print("seu voto é opcional, meu chapa!")
elif 17 < idade < 65:
    print("seu voto é obrigatório! por favor, vote na pessoa certa, e com cuidado!")
else:
    print("seu voto é opcional, senhorzinho.")