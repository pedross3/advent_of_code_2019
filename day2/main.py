def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        lines = lines[0].split(",")
        lines = [int(i) for i in lines]
    return lines

def read_sentence(program, noun, verb):
    memory = program.copy()

    memory[1] = noun
    memory[2] = verb

    noun = 12
    verb = 4
    pointer = 0
    while True:
        operator = memory[pointer]
        if operator == 99:
            pointer += 1
            break

        pos1 = memory[pointer + 1]
        pos2 = memory[pointer + 2]
        pos3 = memory[pointer + 3]

        if operator == 1:
            memory[pos3] = memory[pos1] + memory[pos2]
        elif operator == 2:
            memory[pos3] = memory[pos1] * memory[pos2]
        else:
            raise "Invalid instruction."
        pointer += 4
    return memory[0]

program = read_input(r"input.txt")

target = 19690720

for noun in range(100):
    for verb in range(100):

        result = read_sentence(program, noun, verb)

        if result == target:
            print("Noun:", noun)
            print("Verb:", verb)
            print("Answer:", 100 * noun + verb)
            break