def check_palindrome(strings):
    result = []
    for s in strings:
        palindrome_status = s == s[::-1]  
        result.append((s, palindrome_status))
    return result

strings = ["madam", "racecar", "hello", "world", "level"]
print(check_palindrome(strings))
