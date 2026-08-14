import asyncio, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from import_tang_poetry import download_source
from app.data.normalizer import parse_records

async def main():
    text=await download_source(); records=parse_records(text)
    titles=[f"{x['title']} · {x['author']}" for x in records]
    print("source records:", len(records))
    print("first:", titles[:3])
    print("last:", titles[-3:])
    assert 280 <= len(records) <= 340

if __name__ == "__main__": asyncio.run(main())
