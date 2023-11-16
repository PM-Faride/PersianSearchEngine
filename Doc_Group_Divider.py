from pathlib import Path


try:
    path = Path("E:/Projects/Final_Shared_Files/Docs_Groups")
    p = 1
    for file in path.glob("*.txt"):
        counter = 1
        line_counter = 1
        block = []
        file = open(file, "r", encoding="utf-8")
        for line in file:
            block.append(line)
            if len(block) == 5000:
                f = open(f"E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_{p}/docs_with_{p}_{counter}.txt", "w",
                         encoding="utf- 8")
                for i in range(0, 5000):
                    f.write(block[i])
                del block
                block = []
                counter += 1
                f.close()
            line_counter += 1
        f = open(f"E:/Projects/Final_Shared_Files/Docs_Groups/Docs_with_{p}/docs_with_{p}_{counter}.txt", "w",
                 encoding="utf-8")
        for i in range(0, len(block)):
            f.write(block[i])
        f.close()
        p += 1
except NotADirectoryError:
    print("the file does not exist!!!!!!!!!")

