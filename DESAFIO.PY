
def inverter(string):
    palavras = string.split()
    palavras.reverse()
    string_invertida = ' '.join(palavras)
    return string_invertida

def del_duplicado(string):
    caracteres_unicos = [caractere for i, caractere in enumerate(string) if caractere not in string[:i]]
    nova_string = ''.join(caracteres_unicos)
    return nova_string


def main():
    Entrada = 'Hello World OpenAL is amazing'
    Saida = inverter(Entrada)
    print(Saida)
    Entrada2 = 'Hello World!'
    Saida2 = del_duplicado(Entrada2)
    print(Saida2)

main()