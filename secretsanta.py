import random

# Declare members in the pool.
pool = ['Alex', 'Benjamin', 'Chloe', 'Daniel', 'Emma', 'Fernando', 'Grace',
        'Hannah', 'Isaac', 'Julia', 'Kevin', 'Lily', 'Mike', 'Natalie']

# Assign each member to a different member halfway down the list.
assignments = {}

for n in range(len(pool)):
    if n < len(pool) / 2:
        assignments[pool[n]] = pool[int(len(pool) / 2) + n - 1]
        
    else:
        assignments[pool[n]] = pool[n - int(len(pool) / 2) - 1]

# Print the answer key for assignments.
def print_answers(key):
    for person in key:
        print('Member: {}, Assigned to: {}'.format(person, key[person]))

# Declare a quiz which will store a list of possible choices.
quiz = {}

# Add each person's assigned recipient, and a chosen number of false choices.
for person in assignments:
    
    choices = []
    additional_choices = 3
    
    choices.append(assignments[person])
    
    for i in range(additional_choices):
        
        # Perpetual loop to seek random choices from the pool.
        while True:
            potential = random.choice(pool)
            
            # Break loop once potential choice found not to be unique.
            if potential not in choices and potential is not person:
                choices.append(potential)
                break

    # Shuffle the choices into a random order a few times.
    to_shuffle = 19
    
    for n in range(to_shuffle):
        random.shuffle(choices)

    # Add Secret Santa with their choices to the quiz.
    quiz[person] = choices

# Print the quiz.
def print_quiz(questionnaire):
    for person in quiz:
        print('Who is the correct Secret Santa for {} ?\nA. {}\nB. {}\nC. {}\nD. {}'.
              format(person, questionnaire[person][0], questionnaire[person][1],
                     questionnaire[person][2], questionnaire[person][3]))

print_quiz(quiz)

print_answers(assignments)