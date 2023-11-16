import pandas as pd


def get_n_grams(file_addresses, cols):
    unigrams_fl = pd.read_csv(file_addresses[0], names=cols)
    unigrams = unigrams_fl.words.tolist()
    bigrams_fl = pd.read_csv(file_addresses[1], names=cols)
    bigrams = bigrams_fl.words.tolist()
    trigrams_fl = pd.read_csv(file_addresses[2], names=cols)
    trigrams = trigrams_fl.words.tolist()
    return unigrams, bigrams, trigrams


def get_n_grams_frq(file_addresses, cols):
    unigrams_fl = pd.read_csv(file_addresses[0], names=cols)
    unigram_frq = unigrams_fl.frq.tolist()
    bigrams_fl = pd.read_csv(file_addresses[1], names=cols)
    bigrams_frq = bigrams_fl.frq.tolist()
    trigrams_fl = pd.read_csv(file_addresses[2], names=cols)
    trigrams_frq = trigrams_fl.frq.tolist()
    return unigram_frq, bigrams_frq, trigrams_frq


def get_n_grams_df(file_addresses, cols):
    unigrams_fl = pd.read_csv(file_addresses[0], names=cols)
    unigram_df = unigrams_fl.df.tolist()
    bigrams_fl = pd.read_csv(file_addresses[1], names=cols)
    bigrams_df = bigrams_fl.df.tolist()
    trigrams_fl = pd.read_csv(file_addresses[2], names=cols)
    trigrams_df = trigrams_fl.df.tolist()
    return unigram_df, bigrams_df, trigrams_df


def keep_important_n_grams():
    addresses = ["E:/Projects/Final_Shared_Files/DF_TF_N-Grams/unigrams.csv",
                 "E:/Projects/Final_Shared_Files/DF_TF_N-Grams/bigrams.csv",
                 "E:/Projects/Final_Shared_Files/DF_TF_N-Grams/trigrams.csv"]
    cols = ["words", "frq", "df"]
    unigrams, bigrams, trigrams = get_n_grams(addresses, cols)
    unigrams_frq, bigrams_frq, trigrams_frq = get_n_grams_frq(addresses, cols)
    unigrams_df, bigrams_df, trigrams_df = get_n_grams_df(addresses, cols)
    survived_unigrams = open("E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/unigrams.txt", "w",
                             encoding="utf-8")
    survived_bigrams = open("E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/bigrams.txt", "w",
                            encoding="utf-8")
    survived_trigrams = open("E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/trigrams.txt", "w",
                             encoding="utf-8")
    cumulative_frq = 0
    for i in range(0, len(unigrams)):
        unigram = unigrams[i]
        unigram_frq = unigrams_frq[i]
        unigram_df = unigrams_df[i]
        frq_sum = sum(unigrams_frq)
        cumulative_frq += unigram_frq
        percent = (cumulative_frq / frq_sum) * 100
        survived_unigrams.write(unigram + "," + str(unigram_frq) + "," + str(unigram_df) + "\n")
        if percent > 90:
            break
    survived_unigrams.close()
    del unigrams_frq, unigrams_df, unigrams
    cumulative_frq = 0
    for i in range(0, len(bigrams)):
        bigram = bigrams[i]
        bigram_frq = bigrams_frq[i]
        bigram_df = bigrams_df[i]
        frq_sum = sum(bigrams_frq)
        cumulative_frq += bigram_frq
        percent = (cumulative_frq / frq_sum) * 100
        survived_bigrams.write(bigram + "," + str(bigram_frq) + "," + str(bigram_df) + "\n")
        if percent > 90:
            break
    survived_bigrams.close()
    del bigrams_frq, bigrams, bigrams_df
    cumulative_frq = 0
    for i in range(0, len(trigrams)):
        trigram = trigrams[i]
        trigram_frq = trigrams_frq[i]
        trigram_df = trigrams_df[i]
        frq_sum = sum(trigrams_frq)
        cumulative_frq += trigram_frq
        percent = (cumulative_frq / frq_sum) * 100
        survived_trigrams.write(trigram + "," + str(trigram_frq) + "," + str(trigram_df) + "\n")
        if percent > 90:
            break
    survived_trigrams.close()
    del trigrams, trigrams_df, trigrams_frq


# keep_important_n_grams()