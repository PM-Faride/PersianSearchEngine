import pandas as pd


try:
    out = open("C:/Users/LENOVO/Desktop/u.txt", "w")
    fl = pd.read_csv("C:/Users/LENOVO/Desktop/unigrams.csv", names=["frq", "words"])
    frq = fl.frq.tolist()
    # print(frq)
    words = fl.words.tolist()
    for i in range(0, len(words)):
        counter = words[i]
        for j in range(0, counter):
            out.write(str(frq[i]) + "\n")
    out.close()
except NotADirectoryError:
    print("Sorry, there is no such a file!!!!")