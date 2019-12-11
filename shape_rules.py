import clips

class Shape:

    def __init__(self):
        self.env = clips.Environment()
        self.env.load('data/shape_rules.clp')
        self.env.reset()
        

    def py_pfact(self):
        facts = []
        for fact in self.env.facts():
            facts.append(fact) 
        return facts
    def add_fact(self, new_fact):
        new_fact = "(" + new_fact + ")"
        self.env.assert_string(new_fact)

    def run_clp(self):
        self.env.run(1)
        
    def print_agenda(self):
        agendas = []
        for agenda in self.env.activations():
            agendas.append(agenda)
        return agendas