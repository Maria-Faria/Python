import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "new-folder")
#file = open(ROOT_PATH / "new.txt", "w")
#file.close()

#os.rename(ROOT_PATH / "new.txt", ROOT_PATH / "updated.txt")

#os.remove(ROOT_PATH / "updated.txt")

shutil.move(ROOT_PATH / "new.txt", ROOT_PATH / "new-folder" / "new.txt")