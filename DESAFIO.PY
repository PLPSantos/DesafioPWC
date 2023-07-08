import re


def inverter(string):
    palavras = string.split()
    palavras.reverse()
    string_invertida = ' '.join(palavras)
    return string_invertida


def del_duplicado(string):
    caracteres_unicos = [caractere for i, caractere in enumerate(
        string) if caractere not in string[:i]]
    nova_string = ''.join(caracteres_unicos)
    return nova_string


def encontrar_substring_palindroma(frase):

    frase = frase.lower()
    maior_substring = ""

    for i in range(len(frase)):

        substring = expandir_palindromo(frase, i, i)
        if len(substring) > len(maior_substring):
            maior_substring = substring

        substring = expandir_palindromo(frase, i, i + 1)
        if len(substring) > len(maior_substring):
            maior_substring = substring

    return maior_substring


def expandir_palindromo(frase, inicio, fim):

    while inicio >= 0 and fim < len(frase) and frase[inicio] == frase[fim]:
        inicio -= 1
        fim += 1

    return frase[inicio + 1:fim]


def capitalize_primeiras_letras_frases(string):

    frases = re.split(r'(?<=[.!?])\s+', string)
    frases_capitalizadas = []

    for frase in frases:
        if len(frase) > 0:

            frase_capitalizada = frase[0].capitalize() + frase[1:]
            frases_capitalizadas.append(frase_capitalizada)

    string_capitalizada = ' '.join(frases_capitalizadas)
    return string_capitalizada


def main():
    Entrada = 'Hello World OpenAL is amazing'
    Saida = inverter(Entrada)
    print(Saida)
    Entrada2 = 'Hello World!'
    Saida2 = del_duplicado(Entrada2)
    print(Saida2)
    Entrada3 = 'babad'
    Saida3 = encontrar_substring_palindroma(Entrada3)
    print(Saida3)
    Entrada4 = "hello. how are you? i'm fine,thank you"
    Saida4 = capitalize_primeiras_letras_frases(Entrada4)
    print(Saida4)


main()
