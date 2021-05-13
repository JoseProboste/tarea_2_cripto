import os

p = open('/Users/joseProboste/Desktop/Tarea3_CRIPTO/tarea2_3','r')

for entry in p.readlines():
    password = entry.strip()
    try:
        passw = os.system('7za x JOSE_IGNACIO_PROBOSTE_SEPULVEDA.7z -p%s -y > /dev/null 2>&1' % (password))
        if passw == 0:
            print ("----------- Pass correcta : %s -----------" % entry)
            break
        else:
            print ("Pass incorrecta : %s " % entry
            pass

    except:
        print ("Pass no encontrada en el archivo")
        pass




