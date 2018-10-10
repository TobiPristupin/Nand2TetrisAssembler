from enum import Enum

class Instruction(Enum):
    ADDRESS = 0
    COMMAND = 1

def instruction_type(ass):
    if "@" in ass:
        return Instruction.ADDRESS
    return Instruction.COMMAND

def parse_address(ass):
    return ass.replace("@", "")

def parse_jmp(ass):
    if ";" in ass:
        return ass.split(";")[1]
    return None

def _remove_jmp(ass):
    return ass[:ass.index(";")] if ";" in ass else ass

def parse_dest(ass):
    ass = _remove_jmp(ass)
    if "=" in ass:
            return ass.split("=")[0]
    return None

def parse_comp(ass):
    ass = _remove_jmp(ass)
    if "=" in ass:
        return ass.split("=")[1]
    return ass

def parse_assembly(line):
    line = "".join(line.split())
    if "//" in line:
        return line[:line.index("//")]
    return line

def valid_assembly(line):
    return len(parse_assembly(line)) > 0