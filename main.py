import parser
from opcodes import destination, computation, jump
from symbol_table import SymbolTable
from collections import deque

assembly_in = "assembly.asm"
binary_out = "binary.asm"

def build_symbol_table(program):
    symbols = SymbolTable()
    i = 0
    for line in program:
        if "(" in line:
            line = line.replace("(", "").replace(")", "")
            symbols.add_label(line, i)
            i -= 1
        i += 1
    return symbols

def translate_address(command, symbol_table):
    address = parser.parse_address(command)
    if address.isdigit():
        return '{:016b}'.format(int(address))
    if not symbol_table.has(address):
        symbol_table.add_variable(address)

    return '{:016b}'.format(symbol_table.get(address))    
    

def translate_command(command):
    dest = parser.parse_dest(command)
    comp = parser.parse_comp(command)
    jmp = parser.parse_jmp(command)
    a = "1" if "M" in comp else "0"
    return "111" + a + computation[a][comp] + destination[dest] + jump[jmp]

def translate(program, symbol_table):
    translated = deque()
    for line in program:
        if "(" in line:
            continue
        if parser.instruction_type(line) is parser.Instruction.ADDRESS:
            translated.append(translate_address(line, symbol_table))
        else:
            translated.append(translate_command(line))
    return translated


with open(assembly_in, "r") as f:
    program = [parser.parse_assembly(line) for line in f if parser.valid_assembly(line)]
    symbol_table = build_symbol_table(program)
    translated = translate(program, symbol_table)
    output = open(binary_out, "w")
    print("\n".join(translated))
    print("\n".join(translated), file=output)
    
    
