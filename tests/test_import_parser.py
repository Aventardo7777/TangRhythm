import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app.data.normalizer import parse_records

def test_parser():
    raw="""唐詩三百首全文\n\n詩名:靜夜思\n作者:李白\n詩體:五言絕句\n詩文:(押陽韻)床前明月光，疑是地上霜。\n\n詩名:春曉\n作者:孟浩然\n詩體:五言絕句\n詩文:春眠不覺曉，處處聞啼鳥。"""
    rows=parse_records(raw)
    assert len(rows)==2
    assert rows[0]["title"]=="靜夜思"
    assert rows[0]["content"].startswith("床前明月光")
