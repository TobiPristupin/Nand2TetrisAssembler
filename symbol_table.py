class SymbolTable():

    table = {
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "LOOP": 4,
        "STOP": 18,
        "END": 22
        }

    def __init__(self):
        self.counter = 16

    def get(self, symbol):
        return self.table[symbol]

    def has(self, key):
        return key in self.table

    def add_label(self, symbol, address):
        self.table[symbol] = address

    def add_variable(self, variable):
        self.table[variable] = self.counter
        self.counter += 1
