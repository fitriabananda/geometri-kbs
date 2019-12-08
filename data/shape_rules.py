import clips

env = clips.Environment()

# Assert the first ordeded-fact as string so its template can be retrieved


def py_pfact():
    for fact in env.facts():
        print(fact)

env.define_function(py_pfact)

env.load('shape_rules.clp')
env.reset()
# template = env.find_template('shape')

fact_string = "(besarsudut 60 60 60)"
env.assert_string(fact_string)
fact_string = "(jumlahsisi 3)"
env.assert_string(fact_string)

# template = fact.template

# assert template.implied == True

# new_fact = template.new_fact()
# new_fact.extend((3, 4, 5))
# new_fact.assertit()

env.run()