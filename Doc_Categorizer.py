from pathlib import Path
import pandas as pd
from Keep_Important_N_Grams import get_n_grams
import Multigram_Extractor as func


def extract_unique_features(document):
    doc_terms = document.split()
    single_features = set()
    double_features = set()
    triple_features = set()
    sw = func.unigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Unigram/sw.txt")
    for word in doc_terms:
        if word not in sw:
            single_features.add(word)
    sw_dbl_frst, sw_dbl_lst = func.bigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_frst.txt",
                                                       "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_scnd.txt")
    sw_trpl_frst, sw_trpl_lst = func.trigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_frst.txt",
                                                          "E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_scnd.txt")
    for i in range(len(doc_terms)):
        length = len(doc_terms)
        if i + 1 <= length - 1:
            first_word = doc_terms[i]
            second_word = doc_terms[i + 1]
            if first_word not in sw_dbl_frst and second_word not in sw_dbl_lst:
                double = first_word + " " + second_word
                double_features.add(double)
        if i + 2 <= length - 1:
            third_word = doc_terms[i + 2]
            if first_word not in sw_trpl_frst and second_word not in sw_trpl_lst:
                triple = first_word + " " + second_word + " " + third_word
                triple_features.add(triple)

    return single_features, double_features, triple_features


def check(set_1, list_2):   # for checking if the set of doc words and trigrams have any intersections
    set_2 = set(list_2)
    if len(set_2.intersection(set_1)) > 0:
        return True
    else:
        return False


def get_bigrams(bigram_file, cols):
    bigrams = pd.read_csv(bigram_file, names=cols)
    bigrams = bigrams.words.tolist()
    return bigrams


def get_trigrams(trigram_file, cols):
    trigrams = pd.read_csv(trigram_file, names=cols)
    trigrams = trigrams.words.tolist()
    return trigrams


def docs_categorizer():
    try:
        cols = ["words", "frq", "df"]
        addresses = ["E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/unigrams.csv",
                     "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/bigrams.csv",
                     "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/trigrams.csv"]
        one_grams, bigrams, trigrams = get_n_grams(addresses, cols)
        one_gram_container = open("E:/Projects/Final_Shared_Files/Docs_Groups/docs_with_11.txt", "w", encoding="utf-8")
        bigram_container = open("E:/Projects/Final_Shared_Files/Docs_Groups/docs_with_22.txt", "w", encoding="utf-8")
        trigram_container = open("E:/Projects/Final_Shared_Files/Docs_Groups/docs_with_33.txt", "w", encoding="utf-8")
        nothing = open("E:/Projects/Final_Shared_Files/Docs_Groups/docs_with_nothing.txt", "w", encoding="utf-8")
        path = Path("E:/Projects/Shared_Files/Edited_Docs")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                single_featueres, bi_features, tri_features = extract_unique_features(doc)  # the output is set
                if check(tri_features, trigrams):
                    trigram_container.write(doc)
                elif check(bi_features, bigrams):
                    bigram_container.write(doc)
                elif check(single_featueres, one_grams):
                    one_gram_container.write(doc)
                else:
                    nothing.write(doc)
        docs.close()
        one_gram_container.close()
        bigram_container.close()
        trigram_container.close()
        nothing.close()
    except NotADirectoryError:
        print("Sorry, there is not such file.")


docs_categorizer()