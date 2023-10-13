>>> cad = "abcdefghijklmnñopqrstuvwxyz"
>>> cad[::]   # Seleccionamos todo, equivalente a cad[0:len(cad)]
"abcdefghijklmnñopqrstuvwxyz"
>>> cad[5:]   # Desde el índice 5 hasta el final
"fghijklmnñopqrstuvwxyz"
>>> cad[:5]   # Desde el incio hasta el índice 5 (no incluido)
"abcde"
>>> cad[2: 7] # Desde el índice 2 hasta el 5 (no incluido)
"cdefg"

#Por otro lado Python permite usar índices negativos, siendo -1 el índice del último elemento, -2 el del penúltimo, etc:
>>> cad[-6: -2]
"uvwx"

   Notación      ║                          Selecciona                          ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [:]               ║ Todo                                                         ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [:stop]           ║ Desde el primer elemento hasta el anterior a `stop`          ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [start:]          ║ Desde `start` hasta el final                                 ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [start:stop]      ║ Desde `start` hasta el anterior a `stop`                     ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [start:stop:step] ║ Desde `start` hasta `stop - 1` tomando elementos cada `step` ║
╠═══════════════════╬══════════════════════════════════════════════════════════════╣
║ [::step]          ║ Todo pero tomando solo cada `step` elementos.                ║
╚═══════════════════╩═══════════════════════════════════════════════════════

[::-1]
Esto indica que se seleccione desde último elemento hasta el primero tomando todos los elementos, el resultado es que invertimos los elementos. Recordemos (*), en este caso (step negativo) el índice inicial es igual a len por defecto mientras que el final es -1 - len:

>>> cad[::-1]
'zyxwvutsrqpoñnmlkjihgfedcba'

>>> cad[len(cad): -1 - len(cad): -1]
'zyxwvutsrqpoñnmlkjihgfedcba'

>>> cad[slice(None, None, -1)]
'zyxwvutsrqpoñnmlkjihgfedcba'