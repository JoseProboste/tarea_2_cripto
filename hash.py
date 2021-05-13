import hashlib

f = open('/Users/joseProboste/Downloads/tarea3_v2/diccionarios/diccionario_1','r')
p = open ('/Users/joseProboste/Downloads/tarea3_v2/diccionarios/tarea2_3','w')
mensaje = f.read()
msg = mensaje.split()
for x in msg:
    for i in range(0,1000):
        if i == 0:
            result = hashlib.md5(x.decode())
        else:
            result = hashlib.md5(result.hexdigest().decode())
    for i in range(0,1000):
        if i == 0:
            result2 = hashlib.sha1(result.hexdigest().decode())
        else:
            result2 = hashlib.sha1(result2.hexdigest().decode())
    print result2.hexdigest(),x
    p.write(result2.hexdigest()+'\n')

f.close()
p.close()

