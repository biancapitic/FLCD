from Scanner import Scanner


def main():
    scanner = Scanner('input/p2err.txt')

    pif, constantsST, identifiersST, lexical_errors = scanner.scan()

    with open('output/PIF.out', "w") as file:
        file.write(scanner.getPrintablePIF(pif))

    with open('output/ST_Constants.out', "w") as file:
        file.write(str(constantsST))

    with open('output/ST_Identifiers.out', "w") as file:
        file.write(str(identifiersST))

    if lexical_errors == "":
        print("Lexically correct!")
    else:
        print(lexical_errors)


if __name__ == '__main__':
    main()
