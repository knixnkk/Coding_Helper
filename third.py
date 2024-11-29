def replaceWords(dictionary, sentence):
    root_set = set(dictionary)
    
    words = sentence.split()
    
    for i, word in enumerate(words):
        for j in range(1, len(word) + 1):
            prefix = word[:j]
            if prefix in root_set:
                words[i] = prefix
                break
    
    return ' '.join(words)

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print("Test :", replaceWords(dictionary, sentence))
