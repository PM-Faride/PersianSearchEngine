from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import pandas as pd
import time

start = time.time()


def df_calculator(): # un raveshi k khodam dasti hesab mikardam kamtar vaqt migeref
    try:
        unigrams_df = []
        bigrams_df = []
        trigrams_df = []
        unigrams_fl = pd.read_csv("E:/Projects/Final_Shared_Files/MultiGrams/unigrams.csv", names=["word", "frq"])
        unigrams = unigrams_fl.word.tolist()
        unigram_frq = unigrams_fl.frq.tolist()
        bigram_fl = pd.read_csv("E:/Projects/Final_Shared_Files/MultiGrams/bigrams.csv", names=["word", "frq"])
        bigrams = bigram_fl.word.tolist()
        bigrams_frq = bigram_fl.frq.tolist()
        trigram_fl = pd.read_csv("E:/Projects/Final_Shared_Files/MultiGrams/trigrams.csv", names=["word", "frq"])
        trigrams = trigram_fl.word.tolist()
        trigrams_frq = trigram_fl.frq.tolist()
        ix = open_dir("e:/projects/shared_files/index")
        qp = QueryParser("content", schema=ix.schema)
        with ix.searcher() as s:
            for i in range(0, len(unigrams)):
                query_term = '"' + unigrams[i] + '"'
                query = qp.parse(f'{query_term}')
                r = s.search(query)
                df = len(r)
                unigrams_df.append(df)
            for i in range(0, len(bigrams)):
                query_term = '"' + bigrams[i] + '"'
                query = qp.parse(f'{query_term}')
                r = s.search(query)
                df = len(r)
                bigrams_df.append(df)
            for i in range(0, len(trigrams)):
                query_term = '"' + trigrams[i] + '"'
                query = qp.parse(f'{query_term}')
                r = s.search(query)
                df = len(r)
                trigrams_df.append(df)
        unigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/unigrams.txt", "w", encoding="utf-8")
        bigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/bigrams.txt", "w", encoding="utf-8")
        trigram_output = open("E:/Projects/Final_Shared_Files/DF_TF_N-Grams/trigrams.txt", "w", encoding="utf-8")
        for i in range(0, len(unigrams)):
            df = unigrams_df[i]
            if df > 2:
                unigram_output.write(unigrams[i] + "," + str(unigram_frq[i]) + "," + str(df) + "\n")
        unigram_output.close()
        for i in range(0, len(bigrams)):
            df = bigrams_df[i]
            if df > 2:
                bigram_output.write(bigrams[i] + "," + str(bigrams_frq[i]) + "," + str(df) + "\n")
        bigram_output.close()
        for i in range(0, len(trigrams)):
            df = trigrams_df[i]
            if df > 2:
                trigram_output.write(trigrams[i] + "," + str(trigrams_frq[i]) + "," + str(df) + "\n")
        trigram_output.close()
    except FileNotFoundError:
        print("Hey, I couldnt find the file")


df_calculator()

print((time.time() - start) / 60)