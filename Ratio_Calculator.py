from pathlib import Path
import Keep_Important_N_Grams as keep

sngl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/unigrams.csv"
dbl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/bigrams.csv"
trpl_addrss = "E:/Projects/Final_Shared_Files/Survived_N-grams_DF_Included/trigrams.csv"
addresses = [sngl_addrss, dbl_addrss, trpl_addrss]
cols = ['words', 'frq', 'df']
one_grams, bigrams, trigrams = keep.get_n_grams(addresses, cols)
one_grams_frq, bigrams_frq, trigrams_frq = keep.get_n_grams_frq(addresses, cols)


def bi_one_ratio():
    try:
        path = Path("E:/Projects/Final_Shared_Files/Ratio")
        if not path.exists():
            path.mkdir()
        output = open("E:/Projects/Final_Shared_Files/ratio/2-1.txt", "w", encoding="utf-8")
        for i in range(0, len(bigrams)):
            bigram = bigrams[i]
            bigram_frq = bigrams_frq[i]
            first_word = bigram.split()[0]
            if first_word in one_grams:
                first_index = one_grams.index(first_word)
                frst_wrd_frqncy = one_grams_frq[first_index]
                ratio = bigram_frq / frst_wrd_frqncy
                output.write(bigram + "," + first_word + "," + str(ratio) + "\n")
        output.close()
    except NotADirectoryError:
        print("Sorry, there is so such file!!!!!")


def tri_bi_ratio():
    try:
        output = open("E:/Projects/Final_Shared_Files/ratio/3-2.txt", "w", encoding="utf8")
        for i in range(0, len(trigrams)):
            trigram = trigrams[i]
            trigram_frq = trigrams_frq[i]
            first_word = trigram.split()[0]
            second_word = trigram.split()[1]
            bigram = first_word + " " + second_word
            if bigram in bigrams:
                index = bigrams.index(bigram)
                bigram_frq = bigrams_frq[index]
                ratio = trigram_frq / bigram_frq
                output.write(trigram + "," + bigram + "," + str(ratio) + "\n")
        output.close()
    except NotADirectoryError:
        print("Sorry, no such a file!!!!!")


bi_one_ratio()
tri_bi_ratio()