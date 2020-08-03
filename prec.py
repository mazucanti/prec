import re

l_final = []

with open('teste.txt', 'r') as fp:
    for i, linha in enumerate(fp):
        if i != 0:
            linha = linha.replace("-9.96921e+36", "0")
            linha = linha.split()
            linha[1] = round(float(linha[1]))
            linha[2] = round(float(linha[2]))
            linha[3] = round(float(linha[3]))
            l_final.append(linha)

            if l_final[i-1][0] == l_final[i-2][0] and l_final[i-1][1] == l_final[i-2][1] and l_final[i-1][2] == l_final[i-2][2]:
                l_final[i-1][3] = float((l_final[i-2][3] + l_final[i-1][3]) / 2)
                l_final[i-2] = "-"


with open('prec.txt', 'w') as fp:
    for linha in l_final:
        if type(linha) == list:
            linha = tuple(linha)
            to_fp = "%s,%s,%s,%s" % linha
        
        else:
            continue

        fp.write(to_fp+'\n')
