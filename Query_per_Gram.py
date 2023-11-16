import operator
from pathlib import Path


def unigram_extractor(query, stop_words, unigrams_dict):
    terms = set(query.split())
    for i in range(0, len(terms)):
        word = terms.pop()
        word = word.lower()
        if word in stop_words:
            pass
        elif word in unigrams_dict:
            unigrams_dict[word] += 1
        else:
            unigrams_dict[word] = 1
    return unigrams_dict


def bigram_extractor(query, first_sw, last_sw, bigrams_dict):
    terms = query.split()
    length = len(terms)
    bigrams = set()
    for i in range(0, length):
        if i + 1 <= length - 1:
            first_word = terms[i]
            second_word = terms[i + 1]
            if first_word not in first_sw and second_word not in last_sw:
                bigram = first_word + " " + second_word
                bigram = bigram.lower()
                bigrams.add(bigram)
    for word in bigrams:
        if word in bigrams_dict:
            bigrams_dict[word] += 1
        else:
            bigrams_dict[word] = 1
    return bigrams_dict


def trigram_extractor(query, first_sw, last_sw, trigrams_dict):
    terms = query.split()
    length = len(terms)
    trigrams = set()
    for i in range(0, length):
        if i + 2 <= length - 1:
            first_word = terms[i]
            second_word = terms[i + 1]
            third_word = terms[i + 2]
            if first_word not in first_sw and third_word not in last_sw:
                trigram = first_word + " " + second_word + " " + third_word
                trigram = trigram.lower()
                trigrams.add(trigram)
    for word in trigrams:
        if word in trigrams_dict:
            trigrams_dict[word] += 1
        else:
            trigrams_dict[word] = 1
    return trigrams_dict


def unigram_sw_generator(file_address):
    sw = []
    stop_words_file = open(file_address, "r", encoding="utf-8")
    try:
        for word in stop_words_file:
            sw.append(word.replace("\n", ""))
        stop_words_file.close()
        return sw
    except NotADirectoryError:
        print("Sorry, the File is Nowhere to be Found!")


def bigram_sw_generator(first_file_address, second_file_address):
    try:
        sw_dbl_f_file = open(first_file_address, "r", encoding="utf-8")
        sw_dbl_first = []
        for word in sw_dbl_f_file:
            sw_dbl_first.append(word.replace("\n", ""))
        sw_dbl_f_file.close()

        sw_dbl_l_file = open(second_file_address, "r", encoding="utf-8")
        sw_dbl_scnd = []
        for word in sw_dbl_l_file:
            sw_dbl_scnd.append(word.replace("\n", ""))
        sw_dbl_l_file.close()

        return sw_dbl_first, sw_dbl_scnd
    except NotADirectoryError:
        print("Sorry, There is No Directory that Goes by that Name!")


def trigram_sw_generator(first_file_address, second_file_address):
    try:
        sw_trpl_first = []
        sw_trpl_f_file = open(first_file_address, "r", encoding="utf-8")
        for word in sw_trpl_f_file:
            sw_trpl_first.append(word.replace("\n", ""))
        sw_trpl_f_file.close()

        sw_trpl_scnd = []
        sw_trpl_l_file = open(second_file_address, "r", encoding="utf-8")
        for word in sw_trpl_l_file:
            sw_trpl_scnd.append(word.replace("\n", ""))
        sw_trpl_l_file.close()

        return sw_trpl_first, sw_trpl_scnd
    except NotADirectoryError:
        print("Sorry, I could not find the wanted directory!")


def qry_uni_tf_extractor(stop_words):
    path = Path("E:/Projects/Final_Shared_Files/Query_per_Gram")
    if not path.exists():
        path.mkdir()
    try:
        queries = open('E:/Projects/Final_Shared_Files/Queries/Train/train_data.txt', 'r', encoding='utf-8')
        one_gram = open('E:/Projects/Final_Shared_Files/Query_per_Gram/Unigrams.txt', 'w', encoding='utf-8')
        qry_uni_dict = {}
        counter = 0
        for query in queries:
            qry_uni_dict = unigram_extractor(query, stop_words, qry_uni_dict)
        for key, value in sorted(qry_uni_dict.items(), key=operator.itemgetter(1), reverse=False):
            if value > 3:
                counter += value
                one_gram.write(key + "," + str(value) + "\n")
        queries.close()
        one_gram.close()
        print(counter)

    except FileNotFoundError:
        print("The query_file does not exists!!!")


def qry_bi_tf_extractor(sw_dbl_first, sw_dbl_scnd):
    try:
        queries = open('E:/Projects/Final_Shared_Files/Queries/Train/train_data.txt', 'r', encoding='utf-8')
        bigrams = open("E:/Projects/Final_Shared_Files/Query_per_Gram/Bigrams.txt", 'w', encoding='utf-8')
        bigram_dict = {}
        counter = 0
        for query in queries:
            bigram_dict = bigram_extractor(query, sw_dbl_first, sw_dbl_scnd, bigram_dict)
        for key, value in sorted(bigram_dict.items(), key=operator.itemgetter(1), reverse=False):
            if value > 3:
                counter += value

                bigrams.write(key + "," + str(value) + "\n")
        queries.close()
        print(counter)
        bigrams.close()
    except FileNotFoundError:
        print("The query_file does not exists!!!")


def qry_tri_tf_extractor(sw_trpl_first, sw_trpl_scnd):
    try:
        queries = open('E:/Projects/Final_Shared_Files/Queries/Train/train_data.txt', 'r', encoding='utf-8')
        trigrams = open("E:/Projects/Final_Shared_Files/Query_per_Gram/Trigrams.txt", 'w', encoding='utf8')
        trigrams_dict = {}
        counter = 0
        for query in queries:
            trigrams_dict = trigram_extractor(query, sw_trpl_first, sw_trpl_scnd, trigrams_dict)
        for key, value in sorted(trigrams_dict.items(), key=operator.itemgetter(1), reverse=False):
            if value > 3:
                counter += value
                trigrams.write(key + "," + str(value) + "\n")
        queries.close()
        trigrams.close()
        print(counter)

    except FileNotFoundError:
        print("The query_file does not exists!!!")


# uni_sw = unigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Unigram/sw.txt")
# bi_frst_sw, bi_lst_sw = bigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_frst.txt",
#                                             "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_scnd.txt")
# tri_frst_sw, tri_lst_sw = trigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_frst.txt",
#                                                "E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_scnd.txt")
#
# qry_uni_tf_extractor(uni_sw)
# qry_bi_tf_extractor(bi_frst_sw, bi_lst_sw)
# qry_tri_tf_extractor(tri_frst_sw, tri_lst_sw)



