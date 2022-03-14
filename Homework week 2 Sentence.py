# OPTION 1 - Function: compile a list of words in a sentence

def compiled_sentence(words_list):
    
    sentence = []
    
    end = '.'
    
    sentence += words_list
    
    return " ".join(sentence).capitalize() + end


#OPTION 2 - Function using a for loop

def compiled_sentence_(words_list):
    
    sentence = ''     
    
    for item in range(number):
        
        sentence = sentence + x[item] + ''
    sentence = sentence + '.'
    finalSentence = sentence.capitalize()
    
    return finalSentence


#Function: word count 

def word_count(sentence, word):
    
    count = 0
    separation = words.split()
    
    for item in separation:
        final_word = "".join(c for c in item if c.isalpha())
   
        if final_word == word:
            count = count+1
            
    return f'The word "{word}", repeats {count} times.'