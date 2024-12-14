# gates.py

class ANDGate:
    def __init__(self):
        self.input_a = 0
        self.input_b = 0
        self.output = 0

    def set_inputs(self, a, b):
        assert a in (0, 1), "Input 'a' must be 0 or 1"
        assert b in (0, 1), "Input 'b' must be 0 or 1"
        self.input_a = a
        self.input_b = b
        self.compute()

    def compute(self):
        self.output = self.input_a & self.input_b

    def get_output(self):
        return self.output


class ORGate:
    def __init__(self):
        self.input_a = 0
        self.input_b = 0
        self.output = 0

    def set_inputs(self, a, b):
        assert a in (0, 1), "Input 'a' must be
