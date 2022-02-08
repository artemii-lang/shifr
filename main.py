import argparse
import string

def argument() -> str:
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', dest='string')
    parse.add_argument('-key', dest='key')
    args = parse.parse_args()

    return args.string.lower(), args.key.lower()

def table() -> list:
    s = list( string.ascii_lowercase + string.digits + string.punctuation + ' ')
    table = []
    for i in range(len(s)):
        strok = []
        strok.append(''.join( s[i:]) )
        strok.append(''.join( s[:i]) )
        table.append(list(''.join(strok)))
    return table

def index_key_wolk(wolk):
    indexs = []
    for i in wolk:        
        indexs.append(tab[0].index(i))
    return indexs

def get_hach(indexs_wolk, indexs_key):
    hach = ''
    for i in range(len(indexs_wolk)):
        hach += tab[indexs_wolk[i]] [indexs_key[i]]
    
    return hach


tab = table() 
# print(tab)
wolk, key = argument()

while True:
    if len(wolk) > len(key):
        key += ' '
    elif len(wolk) < len(key):
        wolk += ' '
    else:
        break

indexs_wolk = index_key_wolk(wolk)
indexs_key = index_key_wolk(key)
hach = get_hach(indexs_wolk, indexs_key)


print(f"[*] слово => {wolk}")
print(f"[*] ключь => {key}")
print(f"[*] {hach}")



