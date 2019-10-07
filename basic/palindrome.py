def is_palindrome(word):
    length = (int(len(word) / 2))
    flag = False
    for num in range(length):
        if word[num] == word[len(word) - 1 - num]:
            flag = True
        else:
            flag = False

    return flag

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))