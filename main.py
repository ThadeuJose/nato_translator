def nato_to_normal(expr):
    resp = ''
    for c in expr:
        if c == '.':
            resp += ' '
        if c in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXZ':
            resp += c
    return resp

def normal_to_nato(expr):
    dic_nato = {
      'A': 'Alfa',
      'B': 'Bravo',
      'C': 'Charlie',
      'D': 'Delta',
      'E': 'Echo',
      'F': 'Foxtrot',
      'G': 'Golf',
      'H': 'Hotel',
      'I': 'India',
      'J': 'Juliett',
      'K': 'Kilo',
      'L': 'Lima',
      'M': 'Mike',
      'N': 'November',
      'O': 'Oscar',
      'P': 'Papa',
      'Q': 'Quebec',
      'R': 'Romeo',
      'S': 'Sierra',
      'T': 'Tango',
      'U': 'Uniform',
      'V': 'Victor',
      'W': 'Whiskey',
      'X': 'Xray',
      'Y': 'Yankee',
      'Z': 'Zulu',
    }
    resp = ''
    for c in expr:
        if c != '.':
            if c == ' ':
                resp += '.'
            if c in '1234567890':
                resp += ' '+c
            if c.upper() in dic_nato:
                resp += ' '+dic_nato[c.upper()]
    return resp.strip()


fNormal = open('inputNormal.txt')
stringNormal = ''.join(fNormal.readlines())
print('Nato Message:')
print(normal_to_nato(stringNormal))
print('Original Message:')
print(nato_to_normal(normal_to_nato(stringNormal)))