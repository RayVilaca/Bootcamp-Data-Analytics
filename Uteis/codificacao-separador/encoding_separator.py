import chardet as ch
import csv

def encoding_separator(file_name):
    # Detectar o enconding do arquivo
    with open(file_name, 'rb') as file:
        result = ch.detect(file.read(32768))
        encoding = result['encoding']

    # Detectar o separador do arquivo
    with open(file_name, 'r', encoding=encoding) as file:
        dialect = csv.Sniffer().sniff(file.readline())
        sep = dialect.delimiter
    
    return encoding, sep
