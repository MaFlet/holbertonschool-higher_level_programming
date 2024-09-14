#!/usr/bin/python3
"""
Tester returning key with the biggest integer
value
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
