
class TuringMachine:
    def __init__(self):
        self.states = []  # list of all the rows in the turing machine
        self.current_state_num = 0  # increment each time a state is required
        self.__write_start_state()  # start state

# -- high level methods --
    
    def compare():
        pass

    def swap():
        pass

# -- helper macros --

    def move_forward_n(self, steps: int):
        pass

    def move_backward_n(self, steps: int):
        pass

    def move_forward_n_remember_x(self, steps: int, remember: str):
        pass

    def move_backward_n_remember_x(self, steps: int, remember: str):
        pass

    # the turing machine writes to the input string tape
    # TODO: workout params
    def write_tape(self):
        pass

# -- private methods --

    # internal class method just for writing to the output file
    def __write_state(self, current_state: str, current_symbol: str, move: str, next_symbol: str, next_state: str):
        self.states.append([current_state, current_symbol, move, next_symbol, next_state])

    def __write_start_state(self):
        pass
        #self.__write_state("⎆", "[", "")

# -- out to file --

    def output_to_file(self):
        with open("../turing-maching-output.tsv", "w") as f:
            for state in self.states:
                f.write("\t".join(state))