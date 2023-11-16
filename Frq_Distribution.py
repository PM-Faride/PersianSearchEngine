import pandas as pd
address1 = "E:/Projects/Final_Shared_Files/MultiGrams/All/unigrams_all.csv"
address2 = "E:/Projects/Final_Shared_Files/MultiGrams/All/bigrams_all.csv"
address3 = "E:/Projects/Final_Shared_Files/MultiGrams/All/trigrams_all.csv"


def frq_distribution(address):
    file = pd.read_csv(address, names=["word", "frq"])
    frq = file.frq.tolist()
    return frq


def chart_x_y():
    frq_1 = frq_distribution(address1)
    frq_2 = frq_distribution(address2)
    f = []
    frq_3 = frq_distribution(address3)
    uni = open("E:/Projects/Final_Shared_Files/MultiGrams/All/distribution/unigrams.txt", "w")
    bi = open("E:/Projects/Final_Shared_Files/MultiGrams/All/distribution/bigrams.txt", "w")
    tri = open("E:/Projects/Final_Shared_Files/MultiGrams/All/distribution/trigrams.txt", "w")
    while len(frq_1) > 0:
        frq_1_i = frq_1[0]
        counter = frq_1.count(frq_1_i)
        uni.write(str(frq_1[0]) + "," + str(counter) + "\n")
        while frq_1_i in frq_1:
            frq_1.remove(frq_1_i)

    while len(frq_2) > 0:
        frq_2_i = frq_2[0]
        counter = frq_2.count(frq_2_i)
        bi.write(str(frq_2[0]) + "," + str(counter) + "\n")
        while frq_2_i in frq_2:
            frq_2.remove(frq_2_i)

    while len(frq_3) > 0:
        frq_3_i = frq_3[0]
        counter = frq_3.count(frq_3_i)
        tri.write(str(frq_3[0]) + "," + str(counter) + "\n")
        while frq_3_i in frq_3:
            frq_3.remove(frq_3_i)

    uni.close()
    bi.close()
    tri.close()


chart_x_y()