class FA:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.FA = self.read_FA()
        self.FA_Q = self.FA[0]  # set of states
        self.FA_E = self.FA[1]  # the alphabet
        self.FA_d = self.represent_transitions(self.FA[4])  # transitions
        self.FA_q0 = self.FA[2]  # initial state
        self.FA_F = self.FA[3]  # the final states

    def read_FA(self):
        fa = []
        with open(self.__file_name) as f:
            # get the finite set of states
            line = f.readline()
            fa.append(line[0:-1].split(" "))
            # get the alphabet
            line = f.readline()
            fa.append(line[0:-1].split(" "))
            # get the start state
            line = f.readline()
            fa.append(line[0:-1].split(" "))
            # get the final states
            line = f.readline()
            fa.append(line[0:-1].split(" "))
            # get the transition function
            d = []
            line = f.readline()
            while line:
                transition = line[0:-1]
                d.append(transition.split(","))
                line = f.readline()
            fa.append(d)

        return fa

    @staticmethod
    def represent_transitions(transitions):
        rep = {}
        for t in transitions:
            s = (t[0], t[1])
            if s not in rep.keys():
                rep[s] = []
            rep[s].append(t[2])
        return rep

    def is_deterministic(self):
        for val in self.FA_d.values():
            if len(val) > 1:
                return False
        return True

    def check_sequence(self, sequence):
        if not self.is_deterministic():
            return False
        current_state = self.get_FA_q0()[0]

        for i in sequence:
            if i not in self.FA_E:
                return False
            if (current_state, i) not in self.FA_d.keys():
                return False
            current_state = self.FA_d[(current_state, i)][0]
        if current_state not in self.FA_F:
            return False
        return True

    def get_FA_Q(self):
        return self.FA_Q

    def get_FA_E(self):
        return self.FA_E

    def get_FA_d(self):
        return self.FA_d

    def get_FA_q0(self):
        return self.FA_q0

    def get_FA_F(self):
        return self.FA_F
