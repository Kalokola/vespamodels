
def modify(line):
    import re
    line = re.sub('[_]', ' ', line)
    return line.title()

print(modify('Straw_Berry'))