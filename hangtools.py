import random


def graphics():
    yield """
    
    
    
    
    """
    yield """
    
    
    
    
         __ __"""
    yield """
    
           |
           |
           |
         __|__"""
    yield """
     ⌐----¬
           |
           |
           |
         __|__"""
    yield """
     ⌐----¬
     O     |
           |
           |
         __|__"""
    yield """
     ⌐----¬
     O     |
     |     |
           |
         __|__"""
    yield """
     ⌐----¬
     O     |
    /|     |
           |
         __|__"""
    yield"""
     ⌐----¬
     O     |
    /|\\    |
           |
         __|__"""
    yield"""
     ⌐----¬
     O     |
    /|\\    |
    /      |
         __|__"""
    yield"""
     ⌐----¬
     O     |
    /|\\    |
    / \\    |
         __|__"""


def get_word():
    with open("words_alpha.txt") as the_word:
        get_line = random.choice(the_word.readlines())
        return str(get_line.rstrip())


if __name__ == "__main__":
    word = get_word()
    print(word)
