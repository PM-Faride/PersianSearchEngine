

def avg_q_terms():
    queries = open("E:/Projects/Final_Shared_Files/Queries/Edited_Queries/edited_queries.txt", "r", encoding="utf-8")
    term_counter = 0
    query_counter = 0
    for query in queries:
        query_counter += 1
        term_counter += len(query.split())
    print(term_counter / query_counter)
    return term_counter / query_counter


avg_q_terms()