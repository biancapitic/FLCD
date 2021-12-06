from SymbolTable import SymbolTable
import re

class Scanner:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__identifiersST = SymbolTable()
        self.__constantsST = SymbolTable()
        self.__nbrOfOperators = 16
        self.__nbrOfSeparators = 11
        self.__nbrOfReservedWords = 10
        self.__reservedWords = []
        self.__separators = []
        self.__operators = []
        self.__pif = []
        self.__setAttributes()

    def __setAttributes(self):
        file = open('input/token.in')
        operators = False
        separators = False
        reservedW = False
        for line in file:
            if not operators:
                self.__operators.append(line[:-1])
                if len(self.__operators) == self.__nbrOfOperators:
                    operators = True
            elif not separators:
                if "space" in line:
                    self.__separators.append(' ')
                else:
                    self.__separators.append(line[:-1])
                if len(self.__separators) == self.__nbrOfSeparators:
                    separators = True
            elif not reservedW:
                self.__reservedWords.append(line[:-1])
                if len(self.__reservedWords) == self.__nbrOfReservedWords:
                    reservedW = True

    def __getOperatorToken(self, line, index):
        # it checks if there is a composed operator
        if index + 1 < len(line) and line[index + 1] in self.__operators:
            return line[index:index+2]
        return line[index]

    def __getSeparatorToken(self, line, index):
        if not line[index] == ' ':
            return line[index], index

        while index < len(line) and line[index] == ' ':
            index += 1
        return "", index - 1

    def __getStringToken(self, line, index):
        pos = index
        index += 1
        while index < len(line) and line[index] != '"':
            index += 1
        if index == len(line):
            index -= 1
        return line[pos:index + 1], index

    def __tokenize(self, line):
        index = 0
        tokens = []
        lineLength = len(line)
        while index < lineLength:
            if line[index] in self.__operators:
                token = self.__getOperatorToken(line, index)
            elif line[index] in self.__separators:
                token, index = self.__getSeparatorToken(line, index)
            else:
                pos = index
                if line[index] == '"':
                    token, index = self.__getStringToken(line, index)
                else:
                    while index < len(line) and line[index].isalnum():
                        index += 1
                    if index == len(line):
                        index -= 1
                    # this means that there is a token formed of one character
                    if pos == index:
                        token = line[index]
                    else:
                        # this case is for identifiers
                        token = line[pos:index]
                        index -= 1
            if token != "" and token != '\n' and token != '\t':
                tokens.append(token)
            index += 1
        return tokens

    def __isConstant(self, token):
        if token.isnumeric() or re.search('^"[a-zA-Z0-9\.\\+\*\?\=\!\|\:<\->;, ]*"$', token):
            return True
        return False

    def __isIdentifier(self, token):
        if re.search('^[a-zA-Z]([a-zA-Z0-9_]*)$', token) and len(token) <= 256:
            return True
        return False

    def __analyze(self, tokens, lineNr):
        lexical_errors = ""
        for token in tokens:
            if token in self.__reservedWords or token in self.__separators or token in self.__operators:
                tokenAndPos = (token, (-1, -1))
                self.__pif.append(tokenAndPos)
            elif self.__isIdentifier(token):
                posST = self.__identifiersST.add(token)
                tokenAndPos = ('identifier', posST)
                self.__pif.append(tokenAndPos)
            elif self.__isConstant(token):
                posST = self.__constantsST.add(token)
                tokenAndPos = ('constant', posST)
                self.__pif.append(tokenAndPos)
            else:
                lexical_errors += "Lexical error on line " + str(lineNr) + " at token: " + token + "\n"
        return lexical_errors

    def getPrintablePIF(self, pif):
        res = ""
        for pair in pif:
            res += str(pair) + "\n"
        return res

    def scan(self):
        file = open(self.__fileName)
        lineNr = 1
        lexical_errors = ""
        for line in file:
            tokens = self.__tokenize(line)
            lexical_errors += self.__analyze(tokens, lineNr)
            lineNr += 1
        return self.__pif, self.__constantsST, self.__identifiersST, lexical_errors