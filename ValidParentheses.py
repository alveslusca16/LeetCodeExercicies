#Minha Resposta - 3 ms
class Solution:
    def isValid(self, s: str) -> bool:
        lista = list(map(str, s))

        if len(lista) == 1:
            return False
        if lista[0] == ")" or lista[0] == "]" or lista[0] == "}" :
            return False 

        stack = []
        for ind in range(len(lista)):

            if lista[ind] == "(" or lista[ind] == "[" or lista[ind] == "{":
                stack.append(lista[ind])

            if lista[ind] == ")" or lista[ind] == "]" or lista[ind] == "}":
                if len(stack) > 0:
                    teste = stack[-1]
                if teste == "(" and (lista[ind] == "]" or lista[ind] == "}"):
                    return False
                if teste == "[" and (lista[ind] == ")" or lista[ind] == "}"):
                    return False
                if teste == "{" and (lista[ind] == "]" or lista[ind] == ")"):
                    return False
                if teste == "" and (lista[ind] == "]" or lista[ind] == ")" or lista[ind] == "}"):
                    return False
                else:
                    if len(stack) > 0:
                        teste = ""
                        stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False


#Resposta com menor custo computacional - 0 ms

class Solution:
    def isValid(self, s: str) -> bool:

        pares = {
        ")": "(",
        "]": "[",
        "}": "{"
        }

        if len(s) == 1:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}" :
            return False 

        stack = []
        for ind in s:

            if ind in "([{":
                stack.append(ind)
            else:
                if not stack:
                    return False
                if stack[-1] != pares[ind]:
                    return False
                stack.pop()
                
        if len(stack) == 0:
            return True
        else:
            return False