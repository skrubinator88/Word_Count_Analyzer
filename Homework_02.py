def find_matching_strings(list):
    lower_list = map(lambda x: x.lower, list)
    words_dict = {}
    true_word_count = {}
    occurrences = {}
    for word in list:
        if word.lower() not in words_dict:
            words_dict[word.lower()] = 1
            true_word_count[word] = 1
            occurrences[word.lower()] = 1
        else:
            if word not in true_word_count:
                true_word_count[word] = 1
                occurrences[word.lower()] = occurrences[word.lower()] + 1
            else:
                true_word_count[word] = true_word_count[word] + 1
            words_dict[word.lower()] = words_dict[word.lower()] + 1
    return [words_dict, occurrences, true_word_count]


words = "word Word word WoRd apple"

words_list = words.split()
count = find_matching_strings(words_list)[0]
occurrences = find_matching_strings(words_list)[1]
total_words = find_matching_strings(words_list)[2]

for key in count.keys():
    percent = (int(count[key]) / len(words_list)) * 100
    words_occurences_list = set()
    for true_key in total_words:
        if true_key.lower() == key:
            words_occurences_list.add(true_key)
    print(key + " " + str(percent) + "% " + str(count[key]) + " total occurrences, " + \
          str(occurrences[key]) + " representations " + str(words_occurences_list))
