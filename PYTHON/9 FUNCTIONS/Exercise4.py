def reverse_string(text):
    reverse = ""

    for i in range(len(text) - 1, -1, -1):
        reverse += text[i]

    return reverse


print(reverse_string("Hello World"))