def dad_joke(text, list_of_words=["i'm", "im", "i am", "iam"]):
    """
    Searches for the list_of_words "I'm" or its variants and selects what comes
    after to form a response (Ex.: "Dad, I'm hungry" -> "Hello hungry, I'm dad!")

    @text String | Contains the variant of the work "I'm"
    @list_of_words List | Finds them in a text so it can print a response
    """

    text = text.lower()

    # Checks if there is one of the variants present in the text
    for x in range(len(list_of_words)):
        if list_of_words[x].lower() in text:
            list_of_words[x] = list_of_words[x].lower()

            # Finds the word "I'm" or any words specified in the optional parameter
            word_end_index = text.find(list_of_words[x]) + len(list_of_words[x])

            return f"Hello \"{text[word_end_index:].strip().capitalize()}\", I'm Dad!"


# print(text := dad_joke("Dad, I'm hungry"))
