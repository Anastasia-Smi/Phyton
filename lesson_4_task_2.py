import requests
from requests import Response


def cur():
    data = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    cont = data.content.decode(data.encoding)
    code = "USD"
    codeStart = cont.find(code)
    print(codeStart)
    valStart = cont.find("<Value>", codeStart)
    print(valStart+7)
    print(cont[valStart+7:valStart+14])
cur()