from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir
from pathlib import Path
import os.path
from whoosh import scoring
from whoosh.qparser import QueryParser
import time

results_df = open("E:/Projects/Final_Shared_Files/Results/results_df_in.txt", "w")
schema = Schema(url=TEXT(stored=True, phrase=False), content=TEXT)
indexing_time = open("E:/Projects/Final_Shared_Files/Servers/Times/index_time_in.txt", "w")
searching_time = open("E:/Projects/Final_Shared_Files/Servers/Times/search/search_time_in.txt", "w")
avg_search_time = open("E:/Projects/Final_Shared_Files/Servers/Times/search/avg_search_time_in.txt", "w")


def provide_query():
    try:
        file = open("E:/Projects/Shared_Files/Queries/Test/test_data.txt", "r", encoding="utf-8")
        queries_ = []
        for query in file:
            queries_.append(query)
        file.close()
        return queries_
    except NotADirectoryError:
        print("Sorry no such file")


queries = provide_query()


def server_one_index():
    indexing_time.write("Server1:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes/index_1"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes/index_1")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes/index_1", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_1")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs1")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs2")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs3")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server1_Docs/Docs4")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                if len(doc.split()) > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server one indexing_time is equal to: {indexing_end / 60} minutes\n\n")
        total_time = 0
        df = 0
        with ix.searcher(weighting=scoring.TF_IDF) as searcher:
            for query in queries:
                parser = QueryParser("content", ix.schema)
                myquery = parser.parse(query)
                search_started = time.time()
                results = searcher.search(myquery)
                time_per_search = time.time() - search_started
                total_time += time_per_search
                df += len(results)
        searching_time.write(f"Server-one's searching took {total_time / 60} minutes\n")
        avg_search_time.write(f"Each query is server one averagely took {total_time / len(queries)} seconds\n")
        results_df.write("Server1 Returned: " + str(df) + " Documents\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_two_index():
    indexing_time.write("Server2:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes/index_2"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes/index_2")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes/index_2", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_2")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs1")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs2")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs3")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server2_Docs/Docs4")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                if len(doc.split()) > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server two indexing_time is equal to: {indexing_end / 60} minutes\n\n")
        total_time = 0
        df = 0
        with ix.searcher(weighting=scoring.TF_IDF) as searcher:
            for query in queries:
                parser = QueryParser("content", ix.schema)
                myquery = parser.parse(query)
                search_started = time.time()
                results = searcher.search(myquery)
                time_per_search = time.time() - search_started
                total_time += time_per_search
                df += len(results)
        searching_time.write(f"Server two searching took {total_time / 60} minutes\n")
        avg_search_time.write(f"Each query is server two averagely took {total_time / len(queries)} seconds\n")
        results_df.write("Server2 Returned: " + str(df) + " Documents\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_three_index():
    indexing_time.write("Server3:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes/index_3"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes/index_3")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes/index_3", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_3")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs1")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs2")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs3")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server3_Docs/Docs4")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                if len(doc.split()) > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server three indexing_time is equal to: {indexing_end / 60} minutes\n\n")
        total_time = 0
        df = 0
        with ix.searcher(weighting=scoring.TF_IDF) as searcher:
            for query in queries:
                parser = QueryParser("content", ix.schema)
                myquery = parser.parse(query)
                search_started = time.time()
                results = searcher.search(myquery)
                time_per_search = time.time() - search_started
                total_time += time_per_search
                df += len(results)
        searching_time.write(f"Server three searching took {total_time / 60} minutes\n")
        avg_search_time.write(f"Each query is server three averagely took {total_time / len(queries)} seconds\n")
        results_df.write("Server3 Returned: " + str(df) + " Documents\n")
    except NotADirectoryError:
        print("Sorry, no such file")


def server_four_index():
    indexing_time.write("Server4:\n")
    if not os.path.exists("E:/Projects/Final_Shared_Files/Indexes/index_4"):
        os.mkdir("E:/Projects/Final_Shared_Files/Indexes/index_4")
    ix = create_in("E:/Projects/Final_Shared_Files/Indexes/index_4", schema)
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_4")
    writer = ix.writer()
    try:
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs1")
        indexing_started = time.time()
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs2")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs3")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                url, content = doc.split(" ", 1)
                writer.add_document(url=url, content=content)
            docs.close()
        path = Path("E:/Projects/Final_Shared_Files/Servers/Servers_Docs/Server4_Docs/Docs4")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                # doc = " ".join(doc.split())
                if len(doc.split()) > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
            docs.close()
        writer.commit()
        indexing_end = time.time() - indexing_started
        indexing_time.write(f"Server four indexing_time is equal to: {indexing_end / 60} minutes\n")
        total_time = 0
        df = 0
        with ix.searcher(weighting=scoring.TF_IDF) as searcher:
            for query in queries:
                parser = QueryParser("content", ix.schema)
                myquery = parser.parse(query)
                search_started = time.time()
                results = searcher.search(myquery)
                time_per_search = time.time() - search_started
                total_time += time_per_search
                df += len(results)
        searching_time.write(f"Server four searching took {total_time / 60} minutes\n")
        avg_search_time.write(f"Each query is server four averagely took {total_time / len(queries)} seconds\n")
        results_df.write("Server4 Returned: " + str(df) + " Documents\n")
    except NotADirectoryError:
        print("Sorry, no such file")


server_one_index()
server_two_index()
server_three_index()
server_four_index()
indexing_time.close()
results_df.close()
searching_time.close()
avg_search_time.close()
