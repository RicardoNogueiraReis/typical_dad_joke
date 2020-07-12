def dad_joke(text):
    """
    Searches for the word "I'm" or its variants and selects what comes
    after to form a response (Ex.: "Dad, I'm hungry", "Hello hungry, I'm dad!")
    """
    
    # Variants of the word "I'm"
    word = ["i'm", "im", "i am", "iam"]
    
    # Checks if there is one of the variants present in the text
    for x in range(len(word)):
        if word[x].lower() in text.lower():

            lText = text.lower()
            lWord = word[x]

            # Finds the word "I'm"
            wordEndIndex = lText.find(lWord) + len(word[x].lower())

            # Length of the text
            text_EndIndex = len(text) - 1

            # Removes unnecessary spaces after the word "I'm"
            while text[wordEndIndex] == " ":
                wordEndIndex += 1

            # Removes unnecessary spaces at the end of the string
            while text[text_EndIndex] == " ":
                text_EndIndex -= 1

            print(f"Hello \"{text[wordEndIndex:].capitalize()}\", I'm Dad!")
            
def dad_joke_custom(list_of_words, text):
    """
    Searches for a word/list of words customized by the user
    List_of_words should be a list
    """
    
    # Checks if there is one of the variants present in the text
    for x in range(len(list_of_words)):
        if list_of_words[x].lower() in text.lower():

            lText = text.lower()
            lWord = list_of_words[x]

            # Finds the word "I'm"
            wordEndIndex = lText.find(lWord) + len(word[x].lower())

            # Length of the text
            text_EndIndex = len(text) - 1

            # Removes unnecessary spaces after the word "I'm"
            while text[wordEndIndex] == " ":
                wordEndIndex += 1

            # Removes unnecessary spaces at the end of the string
            while text[text_EndIndex] == " ":
                text_EndIndex -= 1

            print(f"Hello \"{text[wordEndIndex:].capitalize()}\", I'm Dad!")