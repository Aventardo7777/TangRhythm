import hashlib, re

def parse_records(text: str):
    pattern = re.compile(r"詩名:(?P<title>[^\n]+)\n作者:(?P<author>[^\n]+)\n詩體:(?P<genre>[^\n]+)\n詩文:(?P<content>.*?)(?=\n\n詩名:|\Z)", re.S)
    records=[]
    for idx,m in enumerate(pattern.finditer(text), start=1):
        rec=m.groupdict()
        content=rec["content"].strip()
        content=re.sub(r"^\([^)]{1,12}韻\)","",content).strip()
        records.append({"anthology_index":idx,"title":rec["title"].strip(),"author":rec["author"].strip(),"genre":rec["genre"].strip(),"content":content})
    return records

def stable_id(title:str, author:str, index:int)->str:
    return hashlib.sha1(f"{title}|{author}|{index}".encode()).hexdigest()[:16]
