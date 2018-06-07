def const_arvore(numero, raiz):
    if numero > raiz:
        if dicionario[raiz][1] == '':
            dicionario[raiz][1] = numero
            dicionario[numero] = ['', '']
        else:
            const_arvore(numero, dicionario[numero][1])
    else:
        if dicionario[raiz][0] == '':
            dicionario[raiz][0] = numero
            dicionario[numero] = ['', '']
        else:
            const_arvore(numero, dicionario[raiz][0])
    return dicionario


