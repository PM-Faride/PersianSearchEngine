from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir
from pathlib import Path
import os.path
import time

schema = Schema(url=TEXT(stored=True, phrase=False), content=TEXT)
indexing_time = open("E:/Projects/Final_Shared_Files/Servers - Copy/Times/index_time_in.txt", "w")


def server_one_index():
    indexing_time.write("Server1:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes_v2/index_1"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes_v2/index_1")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes_v2/index_1", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes_v2/index_1")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server1_Docs")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                if len(doc.split()) > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server one indexing_time is equal to: {indexing_end / 60} minutes\n\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_two_index():
    indexing_time.write("Server2:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes_v2/index_2"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes_v2/index_2")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes_v2/index_2", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes_v2/index_2")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server2_Docs")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                if len(doc.split()) > 1:
                    index_started = time.time()
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server two indexing_time is equal to: {indexing_end / 60} minutes\n\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_three_index():
    indexing_time.write("Server3:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes_v2/index_3"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes_v2/index_3")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes_v2/index_3", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes_v2/index_3")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server3_Docs")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                if len(doc.split()) > 1:
                    started = time.time()
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server three indexing_time is equal to: {indexing_end / 60} minutes\n\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_four_index():
    indexing_time.write("Server4:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes_v2/index_4"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes_v2/index_4")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes_v2/index_4", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes_v2/index_4")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers - Copy/Servers_Docs/Server4_Docs")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                if len(doc.split()) > 1:
                    started = time.time()
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server four indexing_time is equal to: {indexing_end / 60} minutes\n")
    except NotADirectoryError:
        print("Sorry, no such file")


server_one_index()
server_two_index()
server_three_index()
server_four_index()
indexing_time.close()

