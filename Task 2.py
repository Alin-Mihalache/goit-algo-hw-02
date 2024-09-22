from collections import deque

def is_palindrome(s):
    char_dequeu = deque(s)
    while len(char_dequeu) > 1:
        if char_dequeu.popleft() != char_dequeu.pop():
            return False
    return True

print(is_palindrome('radar'))
print(is_palindrome('test'))