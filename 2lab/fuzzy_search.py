
from nltk.util import ngrams

def levenshtein_distance(s1, s2): # вставки, удаления, замены
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def ngram_distance(s1, s2, n=2):
    ngrams1 = set(ngrams(s1, n))
    ngrams2 = set(ngrams(s2, n))
    intersection = ngrams1.intersection(ngrams2)
    return 1 - len(intersection) / max(len(ngrams1), len(ngrams2))