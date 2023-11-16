import pandas as pd
import math
import Keep_Important_N_Grams as keep
sngl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/unigrams.csv"
dbl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/bigrams.csv"
trpl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/trigrams.csv"


def get_bigram_ratios(ratio_file, cols):
    try:
        ratio_fl = pd.read_csv(ratio_file, names=cols)
        bigrams = ratio_fl.words.tolist()
        unigrams = ratio_fl.root_words.tolist()
        ratios = ratio_fl.ratios.tolist()
        return bigrams, unigrams, ratios
    except NotADirectoryError:
        print("Sorry, there is no such a file!!!!")


def get_trigram_ratios(ratio_file, cols):
    try:
        ratio_fl = pd.read_csv(ratio_file, names=cols)
        trigrams = ratio_fl.words.tolist()
        bigrams = ratio_fl.root_words.tolist()
        ratios = ratio_fl.ratios.tolist()
        return trigrams, bigrams, ratios
    except NotADirectoryError:
        print("Sorry , there is no such a file!!!")


def scale():
    addresses = [sngl_addrss, dbl_addrss, trpl_addrss]
    cols = ['words', 'frq', 'df']
    ratio_cols = ["words", "root_words", "ratios"]
    one_grams, bigrams, trigrams = keep.get_n_grams(addresses, cols)
    one_grams_frq, bigrams_frq, trigrams_frq = keep.get_n_grams_frq(addresses, cols)
    one_grams_df, bigrams_df, trigrams_df = keep.get_n_grams_df(addresses, cols)
    bi_ratio_words, bi_uni, bi_uni_ratios = get_bigram_ratios("E:/Projects/Final_Shared_Files/ratio/2-1.txt",
                                                              ratio_cols)
    tri_ratio_words, tri_bi, tri_bi_ratios = get_trigram_ratios("E:/Projects/Final_Shared_Files/ratio/3-2.txt",
                                                                ratio_cols)
    one_grams_weight = open("E:/Projects/Final_Shared_Files/Term_Weight/unigrams.txt", "w", encoding="utf-8")
    bigrams_weight = open("E:/Projects/Final_Shared_Files/Term_Weight/bigrams.txt", "w", encoding="utf-8")
    trigrams_weight = open("E:/Projects/Final_Shared_Files/Term_Weight/trigrams.txt", "w", encoding="utf-8")
    bi_uni_weight = {}
    tri_bi_weight = {}
    for i in range(0, len(one_grams)):
        df = one_grams_df[i]
        word = one_grams[i]
        frqncy = one_grams_frq[i]
        idf_log = math.log10((460879 / df) + 1)
        tf_log = math.log10(frqncy)
        weight = tf_log * idf_log
        bi_uni_weight[word] = weight
        one_grams_weight.write(word + "," + str(frqncy) + "," + str(df) + "," + str(weight) + "\n")
    one_grams_weight.close()
    for i in range(0, len(bigrams)):
        word = bigrams[i]
        frqncy = bigrams_frq[i]
        df = bigrams_df[i]
        df_log = math.log10(df + 1)
        tf_log = math.log10(frqncy)
        extra = 0
        if word in bi_ratio_words:
            index = bi_ratio_words.index(word)
            uni = bi_uni[index]
            ratio = bi_uni_ratios[index]
            extra = ratio * bi_uni_weight[uni]
        weight = df_log * tf_log + extra
        tri_bi_weight[word] = weight
        bigrams_weight.write(word + "," + str(frqncy) + "," + str(df) + "," + str(weight) + "\n")
    bigrams_weight.close()
    for i in range(0, len(trigrams)):
        word = trigrams[i]
        frqncy = trigrams_frq[i]
        df = trigrams_df[i]
        df_log = math.log10(df + 1)
        tf_log = math.log10(frqncy)
        extra = 0
        if word in tri_ratio_words:
            index = tri_ratio_words.index(word)
            bi = tri_bi[index]
            ratio = tri_bi_ratios[index]
            extra = ratio * tri_bi_weight[bi]
        weight = tf_log * df_log + extra
        trigrams_weight.write(word + "," + str(frqncy) + "," + str(df) + "," + str(weight) + "\n")
    trigrams_weight.close()


# scale()
