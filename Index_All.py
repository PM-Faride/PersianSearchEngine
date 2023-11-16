from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir
from pathlib import Path
import os.path


def indexer():
    try:
        schema = Schema(url=TEXT, content=TEXT)
        if not os.path.exists("E:/Projects/Shared_Files/index"):
            os.mkdir("E:/Projects/Shared_Files/index")
        ix = create_in("E:/Projects/Shared_Files/index", schema)
        ix = open_dir("E:/Projects/Shared_Files/index")
        writer = ix.writer()
        path = Path("E:/Projects/Shared_Files/Edited_Docs")
        for file in path.glob("*.txt"):
            docs = open(file, "r", encoding="utf-8")
            for doc in docs:
                doc = " ".join(doc.split())
                length = len(doc.split())
                if length > 1:
                    url, content = doc.split(" ", 1)
                    writer.add_document(url=url, content=content)
                else:
                    url = doc.split()[0]
                    writer.add_document(url=url, content="")
            docs.close()
        writer.commit()
    except NotADirectoryError:
        print("Sorry, no such file")


# indexer()