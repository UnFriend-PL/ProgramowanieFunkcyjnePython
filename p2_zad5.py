is_palindrome = lambda s: (cleaned := ''.join(filter(str.isalnum, s.lower()))) == cleaned[::-1]
print(is_palindrome("kajak"))