

def get_query_time():
    try:
        queries = open('E:/Projects/Shared_Files/Original_Queries_All/queries.txt', "r", encoding="utf-8")
        output = open("E:/Projects/Shared_Files/Queries_per_Hour.txt", 'w', encoding='utf-8')
        for query in queries:
            beginning_of_date = query.find("2017-")
            if query[beginning_of_date - 1] is not '"':
                beginning_of_date = query.find("2017-", beginning_of_date + 1)
            end_of_date = query.find('"', beginning_of_date)
            date = query[beginning_of_date:end_of_date]
            output.write(str(date) + "\n")
        queries.close()
        output.close()
    except NotADirectoryError:
        print("sorry, not such a file!!!")


# get_query_time()
