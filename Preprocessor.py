from pathlib import Path
import xlsxwriter as writer
import persianutils as pu
import re
import string
import random


def merge_queries():  # query se ruz ro darim in miyad in se ruz ro yeki mikone
    path = Path("e:/projects/shared_files/original_queries_by_day")
    output = open("e:/projects/shared_files/original_queries_all/queries.txt", "w", encoding="utf-8")
    query_counter = 0
    for file in path.glob("*.txt"):
        queries = open(file, "r", encoding="utf-8")
        for query in queries:
            query_counter += 1
            output.write(query)
    output.close()
    print(query_counter)


def analyze_keep_completed_queries():  # qesmathaye query ro az baqqiye etelaat joda krde va
    # q haye kamel shode ro nega midare
    try:
        query_counter = 0
        query_length = 0
        search_from_here = 0
        quotation_counter = 0
        queries = open("e:/projects/shared_files/original_queries_all_completed/completed_queries.txt", 'w',
                       encoding='utf-8')
        file = open("e:/projects/shared_files/original_queries_all/queries.txt", "r", encoding="utf-8")
        query_wb = writer.Workbook("e:/projects/shared_files/original_queries_all/Analyzed.xlsx")
        query_ws = query_wb.add_worksheet("Analyzer")
        query_ws.set_column("A:A", 20)
        first_line = file.readline()
        ip_start = first_line.find('"', 0) + 1
        ip_end = first_line.find('"', ip_start)
        previous_ip = str(first_line[ip_start:ip_end])
        query_start = first_line.find('"', ip_end + 1) + 1
        previous_query = first_line[query_start:first_line.find('"', query_start)]
        for line in file:
            search_from_here = line.find('"', search_from_here) + 1
            quotation_counter += 1
            end_of_ip = line.find('"', search_from_here)
            quotation_counter += 1
            current_ip = str(line[search_from_here:end_of_ip])
            search_from_here = end_of_ip + 1
            search_from_here = line.find('"', search_from_here) + 1
            quotation_counter += 1
            if quotation_counter == 3:
                start_of_query = search_from_here
                end_of_query = line.find('"', search_from_here)
                after_quotation = line[line.find('"', search_from_here) + 1:line.find('"', search_from_here) + 6]
                while after_quotation.count('2017-') == 0:
                    end_of_query = line.find('"', search_from_here)
                    search_from_here = end_of_query + 1
                    after_quotation = line[
                                        line.find('"', search_from_here) + 1:line.find('"', search_from_here) + 6]
                current_query = line[start_of_query:end_of_query]
                if current_ip == previous_ip:
                    previous_query = current_query
                else:
                    previous_query = previous_query.replace('"', "")
                    queries.write(previous_query + "\n")
                    query_ws.write(query_counter, 0, f"Query_{query_counter + 1}")
                    length = len(previous_query.split())
                    query_length += length
                    query_ws.write(query_counter, 1, length)
                    query_counter += 1
                    previous_query = current_query
                    previous_ip = current_ip
                search_from_here = 0
                quotation_counter = 0
        file.close()
        queries.close()
        query_ws.write(query_counter, 0, "Query_Counter")
        query_ws.write(query_counter, 1, query_length/query_counter)
        query_wb.close()
    except FileNotFoundError:
        print("The query_file does not exists!!!")


def is_alphabet(character):
    if (character in "abcdefghijklmnopqrstuvwxyz") or (character in "abcdefghijklmnopqrstuvwxyz".upper()):
        return True
    else:
        return False


# def is_persian_alphabet(character):
#     if character in "ابپتثجچحخدذرزژسشصضطظعغفقکلمنوهی":
#         return True
#     else:
#         return False


def query_editor():
    analyze_keep_completed_queries()
    original_word = ""
    edited_queries = open("E:/Projects/Shared_Files/Queries/Edited_Queries/edited_queries.txt", 'w',
                          encoding='utf-8')
    try:
        file = open("e:/projects/shared_files/original_queries_all_completed/completed_queries.txt", 'r',
                    encoding='utf-8')
        for unedited_query in file:
            edited_query = pu.standardize4Word2vec(unedited_query)
            if edited_query.count("/") or edited_query.count(":"):
                for char in ':/':
                    edited_query[char] = " "
            edited_query = re.sub(r'([+\-,._])\s', r"\1", edited_query)
            edited_query = re.sub(r'\s([+\-.,_])', r"\1", edited_query)
            if edited_query.count("www.nigc alborz.ir"):
                edited_query = edited_query.replace(edited_query, "www.nigc-alborz.ir")
                edited_queries.write(edited_query + "\n")
                continue
            if edited_query.count("++visual c"):
                edited_query = edited_query.replace("++visual c", " visual c++")
            if edited_query[len(edited_query) - 1] in string.punctuation:
                edited_query = edited_query[:len(edited_query) - 1]
            if edited_query.count("www.googl e.com"):
                edited_query = "www.google.com"
            words = edited_query.split()
            for word in words:
                original_word = word
                if word.count("ای.www.reg.tvu.ac.ir") or word.count("ای,www.reg.tvu.ac.ir"):
                    word = word.replace(word, "ای www.reg.tvu.ac.ir")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count("msi.tmp") or word.count("yahoo.mail") or word.count("11.5") \
                        or word.count("shabab.bsj") or word.count("bluestacks.2.7.307.8213") \
                        or word.count("teamviewer.free_10.0.38475") or word.count("2017.1080p.farsi_uptv.co") \
                        or word.count("www.mehr_fci.ir") or word.count("soroush_0.2.0.msi") \
                        or word.count("www.farda_ac.ir") or word.count("rouhollah_talebblog") \
                        or word.count("rouhollah_taleb") or word.count("tehran_test.ir") \
                        or word.count("cactus_art.biz") or word.count("+18") or word.count("پلیس+10") \
                        or word.count("5+1") or word.count("notepad++") or word.count("s8+") \
                        or word.count("s.g.s"):
                    continue
                if word.count("c++"):
                    word = word.replace("c++", "c++ ")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count(".fdlabnet.fda.gov.ir"):
                    word = word.replace(".fdlabnet.fda.gov.ir", "fdlabnet.fda.gov.ir")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count(".192.168.32.68"):
                    word = word.replace(word, "192.168.32.68")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count("دانلوداهنگ"):
                    word = word.replace(word, "دانلود اهنگ")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count("حز30قران"):
                    word = word.replace(word, "جز 30 قران")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if word.count("العلمامرابطون"):
                    word = word.replace(word, "العلما مرابطون")
                    edited_query = edited_query.replace(original_word, word)
                    continue
                if "," in word:
                    if (word.find(",com") >= 0) or (word.find(",ir") >= 0) or \
                            (word.find(".com") >= 0) or (word.find(".ir") >= 0):
                        word = word.replace(',', '.')
                    else:
                        word = word.replace(',', ' ')
                if "." in word:
                    dot_position = word.find(".")
                    if word.find(".-") >= 0:
                        word = word.replace(".-", "-")
                    if word.find(".."):
                        word = word.replace("..", ".")
                    if dot_position - 1 >= 0 and dot_position + 1 < len(word):
                        if word.count("v1.3"):
                            place = word.find("v1.3")
                            word_first = word[:place]
                            word_second = word[(place + 4):len(word)]
                            word_first = word_first.replace(".", " ")
                            word = word_first + "v1.3" + word_second
                        elif word[dot_position - 1].isdigit() and word[dot_position + 1].isdigit():
                            pass
                        elif word.count("www.") or word.count(".com") or word.count(".ir") or word.count(".org") \
                                or word.count(".io") or word.count(".dll") or word.count(".net") or word.count(".tmp") \
                                or word.count(".medu") or word.count(".exe") or word.count("s.w.a.t") \
                                or word.count(".azad") or word.count(".js") or word.count(".mazum") \
                                or word.count(".ajums") or word.count(".swf"):
                            pass
                        elif word.count("r.b.c"):
                            word = word.replace("r.b.c", "rbc ")
                        elif word.count("c.b.c"):
                            word = word.replace("c.b.c", "cbc")
                        elif word.count("c.b.r"):
                            word = word.replace("c.b.r", "cbr")
                        elif word.count("f.b.s"):
                            word = word.replace("f.b.s", "fbs")
                        elif word.count("نج.م"):
                            word = word.replace(word, "نجم")
                        elif word.count("پیر.زی"):
                            word = word.replace(word, "پیروزی")
                        elif word.count("پروبی.تیک"):
                            word = word.replace(word, "پروبیوتیک")
                        elif word.count("خو.د") or word.count("خ.ود"):
                            word = word.replace(word, "خودرو")
                        elif word.count("کامپی.تر"):
                            word = word.replace(word, "کامپیوتر")
                        else:
                            word = word.replace(".", " ")
                    else:
                        word = word.replace(".", " ")
                if "-" in word:
                    dash_position = word.find('-')
                    if ((dash_position - 1) >= 0) and ((dash_position + 1) < len(word)):
                        both_sides_are_letters = is_alphabet(word[dash_position - 1]) \
                                                 and is_alphabet(word[dash_position + 1])
                        both_sides_are_digits = word[dash_position - 1].isdigit() and word[dash_position + 1].isdigit()
                        first_letter_then_digit = is_alphabet(word[dash_position - 1]) and word[
                            dash_position + 1].isdigit()
                        if both_sides_are_letters or first_letter_then_digit or both_sides_are_digits:
                            pass
                        else:
                            word = word.replace("-", " ")
                    else:
                        word = word.replace("-", " ")
                if "_" in word:
                    underline_position = word.find("_")
                    if (word[underline_position - 1].isdigit() and word[underline_position + 1].isdigit()) \
                            or word.count("commando.unit_iranidata.com.part1"):
                        pass
                    else:
                        word = word.replace("_", " ")
                if "+" in word:
                    word = word.replace("+", " ")
                edited_query = edited_query.replace(original_word, word)
            edited_query = " ".join(edited_query.split())
            edited_queries.write(edited_query + "\n")
        file.close()
        edited_queries.close()
    except FileNotFoundError:
        print("The query_file does not exists!!!")


def test_train_provider():
    try:
        queries_ = []
        queries = open("E:/Projects/Shared_Files/Queries/Edited_Queries/edited_queries.txt", "r", encoding="utf-8")
        for query in queries:
            queries_.append(query)
        queries.close()
        length = len(queries_)
        random_queries = []
        random_queries = random.sample(range(0, length), round(0.2 * length))
        test_query = open("e:/projects/shared_files/Queries/Test/test_data.txt", "w", encoding="utf8")
        for i in random_queries:
            query = queries_[i]
            test_query.write(query)
        test_query.close()
        train_data = open("e:/projects/shared_files/Queries/train/train_data.txt", "w", encoding="utf8")
        for i in range(0, length):
            if i not in random_queries:
                query = queries_[i]
                train_data.write(query)
        del queries_, random_queries
        train_data.close()
    except NotADirectoryError:
        print("Hey there, I am sorry there is no such file!!!!")


#
# query_editor()
# test_train_provider()