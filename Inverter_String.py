try:
    string_original = input("Digite a string a ser invertida: ")
except EOFError:
    string_original = "String padrão"  
    print("Erro ao ler a entrada. Usando a string padrão:", string_original)


string_invertida = ""


for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print("String original:", string_original)
print("String invertida:", string_invertida)