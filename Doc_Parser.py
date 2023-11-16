from pathlib import Path
import persianutils as pu
import re
import string
from Preprocessor import is_alphabet


def parse_docs(docs_folder):
    try:
        path = Path(docs_folder)
        i = 0
        for docs in path.glob("*.txt"):
            i += 1
            parsed_documets = open(f"E:/Projects/Shared_Files/Edited_Docs/parsed_docs{i}.txt", "w", encoding="utf-8")
            docs = open(docs, "r", encoding="utf-8")
            for doc in docs:
                parsed_doc = pu.standardize4Word2vec(doc)
                parsed_doc = re.sub(r'([+\-,._])\s', r"\1", parsed_doc)
                parsed_doc = re.sub(r'\s([+\-.,_])', r"\1", parsed_doc)
                if parsed_doc.count("www.nigc alborz.ir"):
                    parsed_doc = parsed_doc.replace(parsed_doc, "www.nigc-alborz.ir")
                    parsed_documets.write(parsed_doc + "\n")
                    continue
                if parsed_doc.count("++visual c"):
                    parsed_doc = parsed_doc.replace("++visual c", " visual c++")
                if parsed_doc[len(parsed_doc) - 1] in string.punctuation:
                    parsed_doc = parsed_doc[:len(parsed_doc) - 1]
                if parsed_doc.count("www.googl e.com"):
                    parsed_doc = "www.google.com"
                words = parsed_doc.split()
                for word in words:
                    original_word = word
                    if word.count("ای.www.reg.tvu.ac.ir") or word.count("ای,www.reg.tvu.ac.ir"):
                        word = word.replace(word, "ای www.reg.tvu.ac.ir")
                        parsed_doc = parsed_doc.replace(original_word, word)
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
                        parsed_doc = parsed_doc.replace(original_word, word)
                        continue
                    if word.count(".fdlabnet.fda.gov.ir"):
                        word = word.replace(".fdlabnet.fda.gov.ir", "fdlabnet.fda.gov.ir")
                        parsed_doc = parsed_doc.replace(original_word, word)
                        continue
                    if word.count(".192.168.32.68"):
                        word = word.replace(word, "192.168.32.68")
                        parsed_doc = parsed_doc.replace(original_word, word)
                        continue
                    if word.count("دانلوداهنگ"):
                        word = word.replace(word, "دانلود اهنگ")
                        parsed_doc = parsed_doc.replace(original_word, word)
                        continue
                    if word.count("حز30قران"):
                        word = word.replace(word, "جز 30 قران")
                        parsed_doc = parsed_doc.replace(original_word, word)
                        continue
                    if word.count("العلمامرابطون"):
                        word = word.replace(word, "العلما مرابطون")
                        parsed_doc = parsed_doc.replace(original_word, word)
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
                        if (underline_position - 1) >= 0 and (underline_position + 1) < len(word):
                            if (word[underline_position - 1].isdigit() and word[underline_position + 1].isdigit()) \
                                    or word.count("commando.unit_iranidata.com.part1"):
                                pass
                            else:
                                word = word.replace("_", " ")
                    if "+" in word:
                        word = word.replace("+", " ")
                    parsed_doc = parsed_doc.replace(original_word, word)
                parsed_doc = " ".join(parsed_doc.split())
                parsed_documets.write(parsed_doc + "\n")
            parsed_documets.close()
            docs.close()
    except FileNotFoundError:
        print("Sorry I could not file the file you wanted")


# parse_docs("E:/Projects/Shared_Files/Docs")