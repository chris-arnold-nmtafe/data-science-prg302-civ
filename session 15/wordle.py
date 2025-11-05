'''
Wordle functionality
'''
def score_guess(target,guess):
    '''
    This function scores a wordle guess
    
    Parameters
    ----------
    target: The secret word that our user is trying to guess
    guess: A user's individual guess (one of 6 in a full game)
    Returns
    -------
    A tuple of 5 numbers (1 per letter) with 2 if the letter matches, 1 if the letter exists in the wrong place, 0 otherwise 
    '''
    if (target==guess):
        return (2,2,2,2,2)
    return (0,0,0,0,0)