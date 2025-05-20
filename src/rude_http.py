import requests
from gc import collect

q=["%","+","ä","ö","ü","Ä","Ö","Ü",
   "ß"," ","°","!","\"","§","$",
   "&","/","?","\\","^","|","(",")",";",
   ":","#","'","[","]","{","}",
    ]
z=["%25","%2B","%C3%A4","%C3%B6","%C3%BC","%C3%84","%C3%96","%C3%9C",
   "%C3%9F","%20","%C2%B0","%21","%22","%C2%A7","%24",
   "%26","%2F","%3f","%5C","%5E","%7C","%28","%29","%3B",
   "%3A","%23","%27","%5B","%5D","%7B","%7d",
   ]

def urlencode_string(string: str):
    for i in range(len(q)):
        if q[i] in string:
            string=string.replace(q[i],z[i])
        collect()
    return string

def urlencode(params: dict = None) -> str:
    if not params:
        return ""

    string = ""
    for key, value in params.items():
        string = string + f"&{key}={value}"

    return string[1:]

def get(url, params=None, **kw):
    if params:
        url = url.rstrip('?') + '?' + urlencode(params)#, doseq=True)

    return requests.get(url, **kw)
