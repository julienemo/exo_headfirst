# this program generates random phrases structured as
# verb+adj+noun
# where each part is chosen randomly from their given list

import random

# import the fonction that otherwise in not
# automatically include

# then the three lists
# NB Atom encourages putting both brackets alone
# instead of on the same row as content
# NB also Atom prefers white space around operators

verbs = [
    'Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced',
    '24/7', 'Sync', 'Target', 'Gamify',
    'Offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot'
    ]

adjectives = [
    'A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B',
    'Oriented', 'Cloud-based', 'API-based'
    ]

nouns = [
    'Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page',
    'Productivity', 'Process', 'Tipping Point', 'Paradigm'
    ]

# randomly choose an element from each list
# this later can be rolled in a loop
# but is it worth the effort for only three
# hmmm...

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

print(verb + ' ' + adjective + ' ' + noun)
