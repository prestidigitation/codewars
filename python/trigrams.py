# Trigrams are a special case of the n-gram, where n is 3. One trigram is a continious sequence of 3 chars in phrase.
# * return all trigrams for the given phrase
# * replace spaces with _
# * return an empty string for phrases shorter than 3
# Example:
# trigrams('the quick red') == the he_ e_q _qu qui uic ick ck_ k_r _re red


# naive solution
def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    trigrams = []
    i = 0
    while i + 3 <= len(phrase):
        trigrams.append(phrase[i:i + 3])
        i += 1
    return ' '.join(trigrams)
