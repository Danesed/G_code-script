f_original = input ("Quale file? trascinalo :")
f_original = f_original.replace("'","").strip() #rimuove apici dovuti al trascinamento del percorso del 'file//esempio//'
with open(f_original,encoding='utf-8',errors='replace') as original:
    num = input ("Quanti cm ? (es 4mm =0.4) :")
    print(num)
    with open(f_original[:-4]+"_out.txt", "w") as f: #crea un nuovo file col nome fileoriginale_old, andando ad escludere la porzione ".txt" del file
        for line in original:
            if '; layer' not in line: #scrive linee senza ; layer
                f.write(line);
            elif '; layer' in line: #controlla linee con ; layer
                res = line.partition('; layer')[2] #estrae dalla linea con ; layer solo la portzione successiva  2, Z = 1.500
                try:
                    layer_num = int(res.split()[0][:-1]) #estrae da  2, Z = 1.500 solo il numero e lo casta da stringa in intero
                    if (layer_num % 2) == 0:  #controllo se pari
                        Z_axis = float(res.split()[3]) #estrae da res solo il numero e lo casta in float
                        f.write(line.replace(str(Z_axis),str(Z_axis + float(num)))) #rimpiazza il numero con il numero modificato con la costante
                        #print(line)
                        print("Layer: ",res," --> ", Z_axis + float(num))
                        #print(layer_num)
                    elif (layer_num % 2) != 0: #se il numero è dispari lo stampa e basta
                        f.write(line)
                except ValueError: #controlla se non c'è un numero, ossia vede se c'è ""; layer end" e scrive la linea
                    f.write(line)
original.close();
f.close();