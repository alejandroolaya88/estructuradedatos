tablero = [
    ["t", "c", "a", "d", "r", "a", "c", "t"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["T", "C", "A", "D", "R", "A", "C", "T"],
]

print("  A B C D E F G H")
print("  ----------------")
for i in range(8):
    fila = 8 - i
    print(f"{fila}|", end=" ")
    for j in range(8):
        print(tablero[i][j], end=" ")
    print(f"|{fila}")
print("  ----------------")
print("  A B C D E F G H")

#minusculas fichas negras y mayusculas fichas blancas
#P de peón T Torre C Caballo A Alfil R Rey D Dama 