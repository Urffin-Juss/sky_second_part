# tests/conftest.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # корень проекта, например D:\skypro\second_one
SRC = ROOT / "src"

# Если есть папка src — добавим её в sys.path, иначе добавим корень проекта
if SRC.exists():
    sys.path.insert(0, str(SRC))
else:
    sys.path.insert(0, str(ROOT))
