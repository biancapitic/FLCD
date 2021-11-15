from finiteAutomata import FiniteAutomata

def printOptions():
    print("0: Stop app.\n"
          "1: Set of states of the FA.\n"
          "2: The alphabet of the FA.\n"
          "3: All the transitions of the FA.\n"
          "4: The set of final states of the FA.\n"
          "5: Check if a given sequence is accepted by the DFA.\n")

def printTransitions(transitions):
    for trans in transitions.keys():
        for t in transitions[trans]:
            print('(' + trans[0] + ", " + trans[1] + ") = " + t)

def checkIfSequenceIsAccepted(sequence, fa):
    try:
        if fa.isSequenceAccepted(sequence):
            print("Sequence is accepted!")
        else:
            print("Sequence is not accepted")
    except ValueError as err:
        print(err)


def main():
    myFA = FiniteAutomata('FA.in')
    while True:
        print("\n -----------------------------")
        printOptions()
        option = input('Chosen option: ')
        if option == '0':
            print("Stopping program...")
            break
        elif option == '1':
            print("Set of states: ")
            print(myFA.getSetOfStates())
        elif option == '2':
            print("Alphabet of the FA: ")
            print(myFA.getAlphabet())
        elif option == '3':
            print("Transitions of the FA: ")
            printTransitions(myFA.getTransitions())
        elif option == '4':
            print("Final states of the FA: ")
            print(myFA.getFiniteStates())
        elif option == '5':
            seq = input("Give sequence: ")
            checkIfSequenceIsAccepted(seq, myFA)
        else:
            print("Wrong option, try again!")


if __name__ == '__main__':
    main()
