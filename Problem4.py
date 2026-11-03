def sefe_int(text):
    text = text.strip()
    if text.lstrip("-").isdigit():
        return int(text)
    try:
        return int(float(text))
    except ValueError:
        return None
    
for sample in ["42","-8","3.9","abc",""]:
    print(repr(sample),"->", sefe_int(sample))
