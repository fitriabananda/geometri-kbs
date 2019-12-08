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
        self.env.run()
        


# template = env.find_template('shape')


# template = fact.template

# assert template.implied == True

# new_fact = template.new_fact()
# new_fact.extend((3, 4, 5))
# new_fact.assertit()