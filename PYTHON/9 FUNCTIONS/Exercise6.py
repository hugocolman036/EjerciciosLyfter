def sort_words(text):

    # String to a list
    words = text.split("-")

    # Organize alphabetically
    words.sort()

    # List to a string
    result = "-".join(words)

    return result


message = "python-variable-function-computer-monitor"

result = sort_words(message)

print(result)