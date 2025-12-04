def isPalindrome(s):
    left = 0                      # 1
    right = len(s) - 1            # 2

    while left < right:           # 3
        
        # skip non-alphanumeric left side
        if not s[left].isalnum(): # 4
            left += 1             # 5
            continue              # 6
        
        # skip non-alphanumeric right side
        if not s[right].isalnum():# 7
            right -= 1            # 8
            continue              # 9

        # compare lowercase chars
        if s[left].lower() != s[right].lower():  # 10
            return False          # 11
        
        left += 1                 # 12
        right -= 1                # 13

    return True                   # 14
