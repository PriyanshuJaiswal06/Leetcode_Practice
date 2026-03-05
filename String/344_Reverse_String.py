def reverseString(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        j = len(s)- 1
        for i in range(len(s)):
            if i>=j:
                break
            s[i],s[j] = s[j],s[i]
            j -= 1
        return s
print(reverseString(["h","e","l","l","o"]))
