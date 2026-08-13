def parse(question):

    text = question.strip()

    text = text.replace("?", "")

    words = text.split()

    for word in words:

        if word.isupper() and "_" in word:

            return word

    return text