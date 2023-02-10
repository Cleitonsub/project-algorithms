def is_palindrome_iterative(word):
    if word == "" or word != word[::-1]:
        # word[::-1] string reverse
        return False

    return True
