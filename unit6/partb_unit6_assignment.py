# Part (b): Sentence Processing and Wordlist Reversal

print("PART (b): SENTENCE TO WORDLIST CONVERSION AND REVERSAL")

def process_sentence(sentence):
    """
    This function demonstrates string manipulation by converting a sentence into a word list,
    reversing the word list, and displaying both the original and reversed versions.
    
    Technical Process:
    1. split() method converts the input sentence string into a list of words
    2. [::-1] slicing creates a reversed copy of the word list
    3. join() method converts the reversed list back into a string
    """
    
    # Convert sentence to wordlist using split() method
    # split() without parameters splits on whitespace and removes extra spaces
    wordlist = sentence.split()
    
    # Reverse the wordlist using slicing
    # [::-1] creates a reversed copy of the list by stepping backwards
    reversed_wordlist = wordlist[::-1]
    
    # Convert reversed wordlist back to sentence using join()
    # ' '.join() inserts spaces between words in the list
    reversed_sentence = ' '.join(reversed_wordlist)
    
    # Display results
    print(f"Original sentence: '{sentence}'")
    print(f"Wordlist: {wordlist}")
    print(f"Number of words: {len(wordlist)}")
    print(f"Reversed wordlist: {reversed_wordlist}")
    print(f"Reversed sentence: '{reversed_sentence}'")
    
    return wordlist, reversed_wordlist

# Test Case 1: Demonstrate basic functionality
print("Test Case 1:")
sentence1 = "Data analysis is a crucial skill for modern businesses"
wordlist1, reversed1 = process_sentence(sentence1)


# Test Case 2: Show versatility with different sentence structure
print("Test Case 2:")
sentence2 = "Python programming makes data manipulation efficient"
wordlist2, reversed2 = process_sentence(sentence2)


# Test Case 3: Interactive user input demonstration
print("Test Case 3 - User Input:")
user_sentence = input("Enter your own sentence to process: ")
user_wordlist, user_reversed = process_sentence(user_sentence)

print("PROGRAM COMPLETED SUCCESSFULLY")