image = open('out.png', 'rb').read()
hdr = image[:0x36]
a = image[0x36:0xA66]
b = image[0xA66:0x10754]
c = image[0x10754:0x2056C]
d = image[0x2056C:0x3038F]

seqs = [
    [a, b, c, d],
    [a, b, d, c],
    [a, c, b, d],
    [a, c, d, b],
    [a, d, b, c],
    [a, d, c, b],
    [b, a, d, c],
    [b, a, c, d],
    [b, c, a, d],
    [b, c, d, a],
    [b, d, a, c],
    [b, d, c, a],
    [c, a, b, d],
    [c, a, d, b],
    [c, b, a, d],
    [c, b, d, a],
    [c, d, a, b],
    [c, d, b, a],
    [d, a, b, c],
    [d, a, c, b],
    [d, b, a, c],
    [d, b, c, a],
    [d, c, b, a],
    [d, c, a, b]
]
i = 0
for seq in seqs:
    f = open(f'test{i}.png', 'wb')
    i += 1
    for part in seq:
        f.write(part)
    f.close()
