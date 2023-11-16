from pathlib import Path
import Keep_Important_N_Grams as keep
from Multigram_Extractor import unigram_sw_generator, bigram_sw_generator, trigram_sw_generator


def extract_unique_features(document):
    doc_terms = document.split()
    single_features = set()
    double_features = set()
    triple_features = set()
    sw = unigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/unigram/sw.txt")
    for word in doc_terms:
        if word not in sw:
            single_features.add(word)
    sw_dbl_frst, sw_dbl_lst = bigram_sw_generator(
        "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_frst.txt",
        "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_scnd.txt")
    sw_trpl_frst, sw_trpl_lst = trigram_sw_generator(
        "E:/Projects/Shared_Files/Stop_Words/trigram/sw_trpl_frst.txt",
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


def df_finder(sngl_wrds, dbl_wrds, trpl_wrds, counter_1, counter_2, counter_3, file):
    try:
        docs = open(file, "r", encoding="utf-8")
        for line in docs:
            sngl_ftrs, dbl_ftrs, trpl_ftrs = extract_unique_features(line)
            for i in range(0, len(sngl_wrds)):
                word = sngl_wrds[i]
                if word in sngl_ftrs:
                    counter_1[i] += 1
            for i in range(0, len(dbl_wrds)):
                word = dbl_wrds[i]
                if word in dbl_ftrs:
                    counter_2[i] += 1
            for i in range(0, len(trpl_wrds)):
                word = trpl_wrds[i]
                if word in trpl_ftrs:
                    counter_3[i] += 1
        docs.close()
        return counter_1, counter_2, counter_3
    except NotADirectoryError:
        print('The directory is not found!')


sngl_addrss = "E:/Projects/Final_Shared_Files/MultiGrams/unigrams.csv"
dbl_addrss = "E:/Projects/Final_Shared_Files/MultiGrams/bigrams.csv"
trpl_addrss = "E:/Projects/Final_Shared_Files/MultiGrams/trigrams.csv"


def starter():
    try:
        one_gram_df = []
        bigram_df = []
        trigram_df = []
        addresses = [sngl_addrss, dbl_addrss, trpl_addrss]
        one_gram, bigram, trigram = keep.get_n_grams(addresses, cols=["words", "frq"])
        one_gram_frq, bigram_frq, trigram_frq = keep.get_n_grams_frq(addresses, cols=["words", "frq"])
        for i in range(0, len(one_gram)):
            one_gram_df.append(0)
        for i in range(0, len(bigram)):
            bigram_df.append(0)
        for i in range(0, len(trigram)):
            trigram_df.append(0)
        path = Path("E:/Projects/Shared_Files/Edited_Docs")
        for file in path.glob("*.txt"):
            one_gram_df, bigram_df, trigram_df = df_finder(one_gram, bigram, trigram, one_gram_df, bigram_df,
                                                           trigram_df
                                                           , file)
        unigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/unigrams.txt", "w", encoding="utf-8")
        bigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/bigrams.txt", "w", encoding="utf-8")
        trigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/trigrams.txt", "w", encoding="utf-8")
        for i in range(0, len(one_gram)):
            word = one_gram[i]
            frq = one_gram_frq[i]
            df = one_gram_df[i]
            if df > 2:
                unigram_output.write(word + "," + str(frq) + "," + str(df) + "\n")
        unigram_output.close()
        for i in range(0, len(bigram)):
            word = bigram[i]
            frq = bigram_frq[i]
            df = bigram_df[i]
            if df > 2:
                bigram_output.write(word + "," + str(frq) + "," + str(df) + "\n")
        bigram_output.close()
        for i in range(0, len(trigram)):
            word = trigram[i]
            frq = trigram_frq[i]
            df = trigram_df[i]
            if df > 2:
                trigram_output.write(word + "," + str(frq) + "," + str(df) + '\n')
        trigram_output.close()
    except NotADirectoryError:
        print("The file does not exist!")


# starter()