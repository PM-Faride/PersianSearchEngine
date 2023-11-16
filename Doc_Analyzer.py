from pathlib import Path
import xlsxwriter as writer


def analyze_docs():  # Baraye un qesmate payan name k mige chi ki has
    # kojas has chi mishe yani dadahayi k darim ro tafsir mikone
    try:
        doc_wb = writer.Workbook("e:/projects/shared_files/edited_docs/Analyzed.xlsx", options={"strings_to_urls":False})
        doc_ws = doc_wb.add_worksheet("Analyzer")
        doc_ws.set_column("A:A", 60)
        path = Path("e:/projects/shared_files/edited_docs")
        doc_counter = 0
        content_counter = 0
        cumulative_doc_sizes = 0
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                doc_counter += 1
                doc_words = doc.split()
                doc_length = len(doc_words)
                if doc_length > 1:
                    content_counter += 1
                    url, content = doc_words[0], doc_words[1:]
                    doc_ws.write(doc_counter - 1, 0, url)
                    cumulative_doc_sizes += doc_length
                    doc_ws.write(doc_counter - 1, 1, doc_length)
                elif doc_length is 1:
                    url = doc_words[0]
                    doc_ws.write(doc_counter - 1, 0, url)
                    doc_ws.write(doc_counter - 1, 1, 0)
            docs.close()
        doc_ws.write(doc_counter, 0, "Docs_AVG_Size")
        doc_ws.write(doc_counter, 1, cumulative_doc_sizes / doc_counter)
        doc_ws.write(doc_counter + 1, 0, "Content_AVG_Size")
        doc_ws.write(doc_counter + 1, 1, cumulative_doc_sizes / content_counter)
        doc_ws.write(doc_counter + 2, 0, "Doc_Counter")
        doc_ws.write(doc_counter + 2, 1, doc_counter)
        doc_ws.write(doc_counter + 3, 0, "Content_Counter")
        doc_ws.write(doc_counter + 3, 1, content_counter)
        doc_wb.close()
    except FileNotFoundError:
        print("The query_file does not exists!!!")


analyze_docs()