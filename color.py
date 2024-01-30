r, g, b = 105,21,51
color = r
color <<= 8
color |= g
color <<= 8
color |= b
print(hex(color))