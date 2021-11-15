
class FiniteAutomata:
    def __init__(self, filename):
        self.filename = filename
        self.states = []
        self.alphabet = []
        self.initialState = None
        self.finalStates = []
        self.transitions = {}
        self.__readAutomata()

    def __readAutomata(self):
        file = open(self.filename)
        lines = file.readlines()
        self.states = lines[0][:-1].strip().split(', ')
        self.alphabet = lines[1][:-1].strip().split(', ')
        self.initialState = lines[2][:-1]
        self.finalStates = lines[3][:-1].strip().split(', ')

        ind = 4
        while ind < len(lines):
            arguments = lines[ind][:-1].strip().split('-')
            states = arguments[0].strip().split(', ')
            terminals = arguments[1].strip().split(', ')
            for terminal in terminals:
                key = (states[0], terminal)
                keys = self.transitions.keys()
                if key not in keys:
                    self.transitions[key] = []
                self.transitions[key].append(states[1])
            ind += 1

    def getFiniteStates(self):
        return self.finalStates.copy()

    def getSetOfStates(self):
        return self.states.copy()

    def getAlphabet(self):
        return self.alphabet.copy()

    def getTransitions(self):
        return self.transitions.copy()

    def checkIfValidSequence(self, sequence):
        for symbol in sequence:
            if symbol not in self.alphabet:
                return False
        return True

    def isSequenceAccepted(self, sequence):
        if self.checkIfValidSequence(sequence):
            symbol = self.initialState
            keys = self.transitions.keys()
            for i in range(len(sequence)):
                pair = (symbol, sequence[i])
                if pair in keys:
                    symbol = self.transitions[pair][0]
                else:
                    return False
            if symbol in self.finalStates:
                return True
            return False
        return False
