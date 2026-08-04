'''
Nice subarray:
1248. Count Number of Nice Subarrays
1763. Longest Nice Substring
'''
def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""
        
    uniq = set(s)
    for i,ch in enumerate(s):
        if ch.lower() in uniq and ch.upper() in uniq:
            continue

        left_str = longestNiceSubstring(s[:i])
        right_str = longestNiceSubstring(s[i+1:])

        return left_str if len(left_str) >= len(right_str) else right_str

    return s
s1 = "YazaAay"
s2 = "Bb"
s3 = "c"
print(longestNiceSubstring(s1))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))