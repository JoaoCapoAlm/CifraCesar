# -*- encoding: utf-8 -*-

maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculo = "abcdefghijklmnopqrstuvxyz"


def converter(texto, chave, opcao, inicio):
    if not chave.isnumeric():
        return "ERRO: A chave deve ser um número inteiro!"
    else:
        chave = int(chave)
    opcao = opcao.upper()
    if not opcao.startswith("C") and not opcao.startswith("D"):
        return "ERRO: Opção inválida! Escolher entre D para decifrar e C para cifrar"

    convertido = ""

    for caractere in texto:
        if caractere in maiusculo:
            inicio = inicio.upper()
            num = addLetra(maiusculo, caractere, opcao, chave, inicio)
            convertido += maiusculo[num]

        elif caractere in minusculo:
            inicio = inicio.lower()
            num = addLetra(minusculo, caractere, opcao, chave, inicio)
            convertido += minusculo[num]

        else:
            convertido += caractere

    return convertido


def addLetra(alfabeto, letra, opcao, chave, begin):
    num = alfabeto.find(letra)
    inicial = alfabeto.find(begin)

    num += inicial

    if opcao == "C":
        num += chave
    else:
        num -= chave

    if num >= len(alfabeto):
        num -= len(alfabeto)
    elif num < 0:
        num += len(alfabeto)

    return num


if __name__ == '__main__':
    entrada = str(input("Digite o texto a ser cifrado ou decifrado: "))
    deslo = input("Entre com o valor da chave(deslocamento): ").strip()
    letraIni = str(input("Digite a letra que deverá ser considerado como o início: "))

    opc = str(input("\nC - Cifrar\n"
                    "D - Decifrar\n"
                    "Opção escolhida: ").strip())

    conversao = converter(entrada, deslo, opc, letraIni)

    if conversao.startswith("ERRO:"):
        print("\n" + conversao)
    else:
        print(f"\nTexto original: {entrada}\n"
              f"Texto convertido: {conversao}")