def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

infile = open("dict.opcorpora.txt", "r", encoding = 'utf-8')
outfile = open("morphlib.pl", "w", encoding = 'utf-8')

for line in infile:
    if isInt(line):
        continue
    
    full = line.lower().replace(',', ' ').replace('-','_').replace("’",'_').split()

    if full == []:
        continue

    for i in range(len(full)):
        if full[i][0].isdigit():
            full[i] = '_'+full[i]

    outfile.write('word(' + full[0] + ',' + full[1] + '(')
    count = len(full) - 1
    for i in range(2, count):
        outfile.write(full[i])
        outfile.write(',')
    if count > 2:
        outfile.write(full[count])
    outfile.write(')).\n')

outfile.close()
infile.close()
