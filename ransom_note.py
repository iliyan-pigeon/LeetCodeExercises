def canConstruct(ransomNote, magazine):
    symbols = set(ransomNote)

    result = True

    for symbol in symbols:
        if ransomNote.count(symbol) > magazine.count(symbol):
            return False

    return result
