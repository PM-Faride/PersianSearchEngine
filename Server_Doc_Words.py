from pathlib import Path


doc_word = open("words.txt", "w")
path1 = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server1_Docs")
path2 = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server2_Docs")
path3 = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server3_Docs")
path4 = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server4_Docs")

counter = 0
number = 0
for docs in path1.glob("*.txt"):
    docs_ = open(docs, "r", encoding="utf-8")
    for doc in docs_:
        number += 1
        counter += len(doc.split())

doc_word.write(f"server1:    {counter/number}\n")

counter = 0
number = 0
for docs in path2.glob("*.txt"):
    docs_ = open(docs, "r", encoding="utf-8")
    for doc in docs_:
        number += 1
        counter += len(doc.split())

doc_word.write(f"server2:    {counter/number}")

counter = 0
number = 0
for docs in path3.glob("*.txt"):
    docs_ = open(docs, "r", encoding="utf-8")
    for doc in docs_:
        number += 1
        counter += len(doc.split())

doc_word.write(f"server3:    {counter/number}")

counter = 0
number = 0
for docs in path4.glob("*.txt"):
    docs_ = open(docs, "r", encoding="utf-8")
    for doc in docs_:
        number += 1
        counter += len(doc.split())

doc_word.write(f"server4:    {counter/number}")


doc_word.close()