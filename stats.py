def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        return num_words

def count_repitions(text):
    ret = dict()
    for word in text.split():
        lword = word.lower()
        for char in lword:
            if char in ret:
                ret[char] += 1
            else:
                ret[char] = 1
    return ret

def sorted_dict(unsorted):
    return sorted(unsorted.items(), key=lambda x: x[1], reverse=True)