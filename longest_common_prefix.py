def longestCommonPrefix(strs):
    prefix = ""
    words_amount = len(strs)
    min_length_word = min([len(i) for i in strs])

    for i in range(min_length_word, -1, -1):
        current_prefixes = [strs[j][:i] for j in range(words_amount)]

        if len(set(current_prefixes)) == 1:
            prefix = current_prefixes[0]
            break

    return prefix
