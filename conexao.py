import sqlite3
from pathlib import Path

ROOT_PATH  = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clientes.db")
print(con)
