'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # set our base case:
    #   if word is less than two, return 0
    if len(word) < 2:
        return 0

    # set our success case:
    #  if word is equal to 'th' return 1
    elif word == 'th':
        return 1

    # structure and compare characters
    #   if word is longer than two characters
    #       capture the first two characters of the array
    #       remove the first character in the array
    elif len(word) > 2:
        comp_chars = word[0:2]
        new_word = word[1:]

        # determine if those two characters match what we need
        #   if it matches, increment the count we're returning and run again
        if comp_chars == 'th':
            return count_th(new_word) + 1

        #   if they don't match, run again without incrementing
        else:
            return count_th(new_word)

    # in the case we find nothing, return zero
    else:
        return 0