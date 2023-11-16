from whoosh.index import open_dir
from whoosh import scoring
from whoosh.qparser import QueryParser
import time


search_avg = open("search_avg.txt", "w")
search = open("search.txt", "w")


def server_one_search(queries):
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_1")
    i = 0
    total_time = 0
    df = 0
    with ix.searcher(weighting=scoring.TF_IDF) as searcher:
        for query in queries:
            i += 1
            parser = QueryParser("content", ix.schema)
            myquery = parser.parse(query)
            search_started = time.time()
            results = searcher.search(myquery)
            time_per_search = time.time() - search_started
            total_time += time_per_search
            df += len(results)
    search.write(f"Server-one's searching took {total_time / 60} minutes\n")
    search_avg.write(f"one] {total_time / len(queries)}\n")


def server_two_search(queries):
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_2")
    i = 0
    total_time = 0
    df = 0
    with ix.searcher(weighting=scoring.TF_IDF) as searcher:
        for query in queries:
            i += 1
            parser = QueryParser("content", ix.schema)
            myquery = parser.parse(query)
            search_started = time.time()
            results = searcher.search(myquery)
            time_per_search = time.time() - search_started
            total_time += time_per_search
            df += len(results)
    search.write(f"Server two searching took {total_time / 60} minutes\n")
    search_avg.write(f"two, {total_time / len(queries)}\n")


def server_three_search(queries):
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_3")
    i = 0
    total_time = 0
    df = 0
    with ix.searcher(weighting=scoring.TF_IDF) as searcher:
        for query in queries:
            i += 1
            parser = QueryParser("content", ix.schema)
            myquery = parser.parse(query)
            search_started = time.time()
            results = searcher.search(myquery)
            time_per_search = time.time() - search_started
            total_time += time_per_search
            df += len(results)
    search.write(f"Server three searching took {total_time / 60} minutes\n")
    search_avg.write(f"three, {total_time / len(queries)} \n")


def server_four_search(queries):
    ix = open_dir("E:/Projects/Final_Shared_Files/Indexes/index_4")
    i = 0
    total_time = 0
    df = 0
    with ix.searcher(weighting=scoring.TF_IDF) as searcher:
        for query in queries:
            i += 1
            parser = QueryParser("content", ix.schema)
            myquery = parser.parse(query)
            search_started = time.time()
            results = searcher.search(myquery)
            time_per_search = time.time() - search_started
            total_time += time_per_search
            df += len(results)
    search.write(f"Server four searching took {total_time / 60} minutes\n")
    search_avg.write(f"four, {total_time / len(queries)}\n")


def provide_query():
    try:
        file = open("E:/Projects/Shared_Files/Queries/Test/test_data.txt", "r", encoding="utf-8")
        queries_ = []
        counter = 0
        for query in file:
            counter += 1
            if counter > 100:
                break
            queries_.append(query)
        return queries_
        file.close()
    except NotADirectoryError:
        print("Sorry no such file")


queries = provide_query()
for i in range(0, 10):
    server_one_search(queries)
for i in range(0, 10):
    server_two_search(queries)
for i in range(0, 10):
    server_three_search(queries)
for i in range(0, 10):
    server_four_search(queries)
search_avg.close()
search.close()
