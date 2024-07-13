from pathlib import Path

try:
    file = open("my_file.py")

except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)

ROOT_PATH = Path(__file__).parent

try:
    file = open(ROOT_PATH / "new-folder")

except PermissionError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")