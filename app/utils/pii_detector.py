import re

CPF_RE = re.compile(r'\b\d{3}[.\-]?\d{3}[.\-]?\d{3}[-]?\d{2}\b')
EMAIL_RE = re.compile(r'[\w\.-]+@[\w\.-]+')
PHONE_RE = re.compile(r'\b\d{4,5}[- ]?\d{4}\b')

def find_pii(text):
    res = {}
    cpfs = CPF_RE.findall(text)
    emails = EMAIL_RE.findall(text)
    phones = PHONE_RE.findall(text)
    if cpfs:
        res['cpf'] = cpfs
    if emails:
        res['emails'] = emails
    if phones:
        res['phones'] = phones
    return res
