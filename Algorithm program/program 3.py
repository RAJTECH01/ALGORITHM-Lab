def search(pat, txt):
    n = len(txt)
    m = len(pat)
    result = []

    # Loop through the text and search for the pattern
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if txt[i + j] != pat[j]:
                break
            j += 1
        
        # If the entire pattern is found, add the index to the result list
        if j == m:
            result.append(i)
    
    return result  # Return after searching the entire text

# Example usage
txt = "AABAACAADAABAABA"
pat = "AABA"
result = search(pat, txt)
print("Pattern found at indices:", result)
