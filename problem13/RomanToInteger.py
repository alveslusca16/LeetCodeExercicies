class Solution:
    def romanToInt(self, s: str) -> int:
        resultado = 0
        valores = {
            'I': 1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        } 

        lista = list(map(str, s))
        for i, n in enumerate(lista):
            valor_atual = valores[n]
            if i + 1 < len(lista):
                proximo_valor = valores[lista[i+1]]
                if valor_atual < proximo_valor:
                    resultado -= valor_atual
                    continue

            resultado += valor_atual

        return resultado