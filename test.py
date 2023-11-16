from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir
import os.path
from whoosh import scoring
from whoosh.qparser import QueryParser
schema = Schema(url=TEXT(stored=True, phrase=False), content=TEXT)

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
ix = open_dir("index")
writer = ix.writer()
content = "ali is the best but ali ali ali ali"
writer.add_document(url="h", content=content)
content = "ali is is is is ali ali ali ali ali ali ali ali ali ali ali ali ali ali ali but hadi"
writer.add_document(url="f", content=content)
writer.commit()
with ix.searcher(weighting=scoring.TF_IDF) as searcher:
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse("ali")
    results = searcher.search(myquery)
    idf = searcher.idf("content", "but ali")
    print(idf)
