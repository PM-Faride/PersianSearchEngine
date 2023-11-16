import Multigram_Extractor as me
import pandas as pd
import Keep_Important_N_Grams as keep
from pathlib import Path
import Multigram_Extractor as extractor
server_dict_1 = {"Server_1": 0,
                 "Server_2": 0,
                 "Server_3": 0,
                 "Server_4": 0}
server_dict_2 = {"Server_1": 0,
                 "Server_2": 0,
                 "Server_3": 0,
                 "Server_4": 0}
server_dict_3 = {"Server_1": 0,
                 "Server_2": 0,
                 "Server_3": 0,
                 "Server_4": 0}
server_dict_4 = {"Server_1": 0,
                 "Server_2": 0,
                 "Server_3": 0,
                 "Server_4": 0}


def extract_one_grams_customized(doc, stop_words, bigram_checked):
    terms = doc.split()
    length = len(terms)
    one_gram_dict = {}
    for i in range(0, length):
        word = edit_word(terms[i])
        if i + 1 <= length - 1:
            if word not in stop_words:
                second = terms[i + 1]
                bigram = word + " " + second
                if bigram not in bigram_checked:
                    if word in one_gram_dict:
                        one_gram_dict[word] += 1
                    else:
                        one_gram_dict[word] = 1
        else:
            if word in one_gram_dict:
                one_gram_dict[word] += 1
            else:
                one_gram_dict[word] = 1
    return one_gram_dict


def extract_bigrams_customized(doc, first_sw, last_sw, trigram_checked):
    terms = doc.split()
    length = len(terms)
    bigrams_dict = {}
    for i in range(0, length - 1):
        first_word = terms[i]
        second_word = terms[i + 1]
        bigram = first_word + " " + second_word
        if i + 2 <= length - 1:
            trigram = bigram + " " + edit_word(terms[i + 2])
            if first_word not in first_sw and second_word not in last_sw and trigram not in trigram_checked:
                if bigram in bigrams_dict:
                    bigrams_dict[bigram] += 1
                else:
                    bigrams_dict[bigram] = 1
        else:
            if first_word not in first_sw and second_word not in last_sw:
                if bigram in bigrams_dict:
                    bigrams_dict[bigram] += 1
                else:
                    bigrams_dict[bigram] = 1
    return bigrams_dict


def extract_trigrams(doc, first_sw, last_sw):
    terms = doc.split()
    length = len(terms)
    trigrams_dict = {}
    for i in range(0, length - 2):
        first_word = terms[i]
        second_word = terms[i + 1]
        third_word = edit_word(terms[i + 2])
        if first_word not in first_sw and third_word not in last_sw:
            trigram = first_word + " " + second_word + " " + third_word
            if trigram in trigrams_dict:
                trigrams_dict[trigram] += 1
            else:
                trigrams_dict[trigram] = 1
    return trigrams_dict


def n_grams_weight(file_addresses, cols):
    unigrams = pd.read_csv(file_addresses[0], names=cols)
    bigram_f = pd.read_csv(file_addresses[1], names=cols)
    trigram_f = pd.read_csv(file_addresses[2], names=cols)
    unigrams_weight = unigrams.weight.tolist()
    bigrams_weight = bigram_f.weight.tolist()
    trigrams_weight = trigram_f.weight.tolist()
    return unigrams_weight, bigrams_weight, trigrams_weight


def edit_word(word):
    if word.find(".") is len(word):
        word = word.replace(".", "")
    if "," in word:
        word = word.replace(",", "")
    if "،" in word:
        word = word.replace("،", "")
    return word


def doc_weight():
    try:
        cols = ["words", "frq", "df", "weight"]
        addresses = ["E:/Projects/Final_Shared_Files/Term_Weight/unigrams.csv",
                     "E:/Projects/Final_Shared_Files/Term_Weight/bigrams.csv",
                     "E:/Projects/Final_Shared_Files/Term_Weight/trigrams.csv"]
        sw = extractor.unigram_sw_generator("E:/Projects/Shared_Files/Stop_Words/Unigram/sw.txt")
        sw_dbl_frst, sw_dbl_lst = extractor.bigram_sw_generator(
            "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_frst.txt",
            "E:/Projects/Shared_Files/Stop_Words/Bigram/sw_dbl_scnd.txt")
        sw_trpl_frst, sw_trpl_lst = extractor.trigram_sw_generator(
            "E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_frst.txt",
            "E:/Projects/Shared_Files/Stop_Words/Trigram/sw_trpl_scnd.txt")
        one_grams, bigrams, trigrams = keep.get_n_grams(addresses, cols)
        one_grams_weight, bigrams_weight, trigrams_weight = n_grams_weight(addresses, cols)
        server_1_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs3_within_Servers_url/Server_1.txt", "w", encoding="utf-8")
        server_2_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs3_within_Servers_url/Server_2.txt", "w", encoding="utf-8")
        server_3_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs3_within_Servers_url/Server_3.txt", "w", encoding="utf-8")
        server_4_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs3_within_Servers_url/Server_4.txt", "w", encoding="utf-8")
        docs_3_weight = open("E:/Projects/Final_Shared_Files/Doc_Weight/Docs3/docs_3_weight.txt", "w", encoding="utf-8")
        path = Path("E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_1")
        counter = 0
        i = 1
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            counter += 1
            server_1_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs3/server1_{counter}.txt", "w", encoding="utf-8")
            server_2_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs3/server2_{counter}.txt", "w", encoding="utf-8")
            server_3_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs3/server3_{counter}.txt", "w", encoding="utf-8")
            server_4_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs3/server4_{counter}.txt", "w", encoding="utf-8")
            for doc in docs:
                weight = 0
                trigrams_dict = extract_trigrams(doc, sw_trpl_frst, sw_trpl_lst)
                trigrams_checked = []
                bigrams_checked = []
                for i in range(0, len(trigrams)):
                    trigram = trigrams[i]
                    if trigram in trigrams_dict:
                        bigram = trigram.split()[0] + " " + trigram.split()[1]
                        bigrams_checked.append(bigram)
                        trigrams_checked.append(trigram)
                        trigram_w = trigrams_weight[i]
                        trigram_tf = trigrams_dict[trigram]
                        weight += trigram_tf * trigram_w
                bigrams_dict = extract_bigrams_customized(doc, sw_dbl_frst, sw_dbl_lst, trigrams_checked)
                for i in range(0, len(bigrams)):
                    bigram = bigrams[i]
                    if bigram in bigrams_dict:
                        bigrams_checked.append(bigram)
                        bigram_weight = bigrams_weight[i]
                        bigram_tf = bigrams_dict[bigram]
                        weight += bigram_tf * bigram_weight
                one_grams_dict = extract_one_grams_customized(doc, sw, bigrams_checked)
                for i in range(0, len(one_grams)):
                    one_gram = one_grams[i]
                    if one_gram in one_grams_dict:
                        one_gram_weight = one_grams_weight[i]
                        one_gram_tf = one_grams_dict[one_gram]
                        weight += one_gram_tf * one_gram_weight
                docs_3_weight.write(doc.split()[0] + "," + str(weight) + "\n")
                srvr_wth_mn_wght = min(server_dict_3, key=server_dict_3.get)
                server_dict_3[srvr_wth_mn_wght] += weight
                if srvr_wth_mn_wght is "Server_1":
                    server_1_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_1_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_2":
                    server_2_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_2_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_3":
                    server_3_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_3_docs.write(doc)
                else:
                    server_4_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_4_docs.write(doc)
                del bigrams_checked
                del trigrams_checked
            server_1_docs.close()
            server_2_docs.close()
            server_3_docs.close()
            server_4_docs.close()
        server_1_docs_url.close()
        server_2_docs_url.close()
        server_3_docs_url.close()
        server_4_docs_url.close()
        docs_2_weight = open("E:/Projects/Final_Shared_Files/Doc_Weight/Docs2/docs_2_weight.txt", "w", encoding="utf-8")
        path = Path("E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_2")
        counter = 0
        i = 1
        server_1_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs2_within_Servers_url/Server_1.txt", "w", encoding="utf-8")
        server_2_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs2_within_Servers_url/Server_2.txt", "w", encoding="utf-8")
        server_3_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs2_within_Servers_url/Server_3.txt", "w", encoding="utf-8")
        server_4_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs2_within_Servers_url/Server_4.txt", "w", encoding="utf-8")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            counter += 1
            server_1_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs2/server1_{counter}.txt", "w", encoding="utf-8")
            server_2_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs2/server2_{counter}.txt", "w", encoding="utf-8")
            server_3_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs2/server3_{counter}.txt", "w", encoding="utf-8")
            server_4_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs2/server4_{counter}.txt", "w", encoding="utf-8")
            for doc in docs:
                weight = 0
                bigrams_dict = {}
                bigrams_checked = []
                bigrams_dict = me.bigram_extractor(doc, sw_dbl_frst, sw_dbl_lst, bigrams_dict)
                for i in range(0, len(bigrams)):
                    bigram = bigrams[i]
                    if bigram in bigrams_dict:
                        bigrams_checked.append(bigram)
                        bigram_w = bigrams_weight[i]
                        bigram_tf = bigrams_dict[bigram]
                        weight += bigram_w * bigram_tf
                one_grams_dict = extract_one_grams_customized(doc, sw, bigrams_checked)
                for i in range(0, len(one_grams)):
                    one_gram = one_grams[i]
                    if one_gram in one_grams_dict:
                        one_gram_w = one_grams_weight[i]
                        one_gram_tf = one_grams_dict[one_gram]
                        weight += one_gram_w * one_gram_tf
                docs_2_weight.write(doc.split()[0] + "," + str(weight) + "\n")
                srvr_wth_mn_wght = min(server_dict_2, key=server_dict_2.get)
                server_dict_2[srvr_wth_mn_wght] += weight
                if srvr_wth_mn_wght is "Server_1":
                    server_1_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_1_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_2":
                    server_2_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_2_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_3":
                    server_3_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_3_docs.write(doc)
                else:
                    server_4_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_4_docs.write(doc)
                del bigrams_checked
                del bigrams_dict
            server_1_docs.close()
            server_2_docs.close()
            server_3_docs.close()
            server_4_docs.close()
        server_1_docs_url.close()
        server_2_docs_url.close()
        server_3_docs_url.close()
        server_4_docs_url.close()
        counter = 0
        i = 1
        server_1_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs1_within_Servers_url/Server_1.txt", "w", encoding="utf-8")
        server_2_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs1_within_Servers_url/Server_2.txt", "w", encoding="utf-8")
        server_3_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs1_within_Servers_url/Server_3.txt", "w", encoding="utf-8")
        server_4_docs_url = open(
            "E:/Projects/Final_Shared_Files/Servers/Servers_Weight/Docs1_within_Servers_url/Server_4.txt", "w", encoding="utf-8")
        docs_1_weight = open(
            "E:/Projects/Final_Shared_Files/Doc_Weight/Docs1/docs_1_weight.txt", "w", encoding="utf-8")
        path = Path("E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_3")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            counter += 1
            server_1_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs1/server1_{counter}.txt", "w", encoding="utf-8")
            server_2_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs1/server2_{counter}.txt", "w", encoding="utf-8")
            server_3_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs1/server3_{counter}.txt", "w", encoding="utf-8")
            server_4_docs = open(f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs1/server4_{counter}.txt", "w", encoding="utf-8")
            for doc in docs:
                weight = 0
                one_grams_dict = {}
                one_grams_dict = me.unigram_extractor(doc, sw, one_grams_dict)
                for i in range(0, len(one_grams)):
                    one_gram = one_grams[i]
                    if one_gram in one_grams_dict:
                        one_gram_w = one_grams_weight[i]
                        one_gram_tf = one_grams_dict[one_gram]
                        weight += one_gram_tf * one_gram_w
                del one_grams_dict
                docs_1_weight.write(doc.split()[0] + "," + str(weight) + "\n")
                srvr_wth_mn_wght = min(server_dict_1, key=server_dict_1.get)
                server_dict_1[srvr_wth_mn_wght] += weight
                if srvr_wth_mn_wght is "Server_1":
                    server_1_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_1_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_2":
                    server_2_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_2_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_3":
                    server_3_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_3_docs.write(doc)
                else:
                    server_4_docs_url.write(doc.split()[0] + "," + str(weight) + "\n")
                    server_4_docs.write(doc)
            server_1_docs.close()
            server_2_docs.close()
            server_3_docs.close()
            server_4_docs.close()
        server_1_docs_url.close()
        server_2_docs_url.close()
        server_3_docs_url.close()
        server_4_docs_url.close()
        counter = 0
        path = Path("E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_4")
        # n = 0
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            counter += 1
            server_1_docs = open(
                f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs4/server1_{counter}.txt", "w",
                encoding="utf-8")
            server_2_docs = open(
                f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs4/server2_{counter}.txt", "w",
                encoding="utf-8")
            server_3_docs = open(
                f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs4/server3_{counter}.txt", "w",
                encoding="utf-8")
            server_4_docs = open(
                f"E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs4/server4_{counter}.txt", "w",
                encoding="utf-8")
            for doc in docs:
                srvr_wth_mn_wght = min(server_dict_4, key=server_dict_4.get)
                server_dict_4[srvr_wth_mn_wght] += len(doc.split())
                if srvr_wth_mn_wght is "Server_1":
                    server_1_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_2":
                    server_2_docs.write(doc)
                elif srvr_wth_mn_wght is "Server_3":
                    server_3_docs.write(doc)
                else:
                    server_4_docs.write(doc)
            server_1_docs.close()
            server_2_docs.close()
            server_3_docs.close()
            server_4_docs.close()
    except NotADirectoryError:
        print("Sorry, I seem not to be able to find the file!!!!")


doc_weight()
