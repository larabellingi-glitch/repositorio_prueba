nombre = input("Cliente: ").strip()
while not nombre.isalpha() or nombre == "":
    print("Error: Solo letras.")
    nombre = input("Cliente: ").strip()

cantidad_str = input("Cantidad de productos: ").strip()
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Error: Ingrese un número mayor a 0.")
    cantidad_str = input("Cantidad de productos: ").strip()

cantidad = int(cantidad_str)
total_sin = 0
total_con = 0

for i in range(1, cantidad + 1):
    p_str = input(f"Producto {i} - Precio: ").strip()
    while not p_str.isdigit():
        p_str = input("Error, reingrese precio: ").strip()
    
    precio = int(p_str)
    total_sin += precio
    
    desc = input("¿Descuento? (S/N): ").lower().strip()
    while desc != "s" and desc != "n":
        desc = input("Error, ingrese S o N: ").lower().strip()
    
    if desc == "s":
        total_con += precio * 0.9
    else:
        total_con += precio

print(f"\nTotal sin descuentos: ${total_sin}")
print(f"Total con descuentos: ${total_con:.2f}")
print(f"Ahorro: ${total_sin - total_con:.2f}")
print(f"Promedio por producto: ${total_con / cantidad:.2f}")

usuario_ok = "alumno"
clave_ok = "python123"
intentos = 0
logueado = False

while intentos < 3:
    intentos += 1
    u = input(f"Intento {intentos}/3 - Usuario: ").strip()
    c = input("Clave: ").strip()
    if u == usuario_ok and c == clave_ok:
        logueado = True
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")

if not logueado:
    print("Cuenta bloqueada.")
else:
    opcion = ""
    while opcion != "4":
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ").strip()
        if not opcion.isdigit():
            print("Error: ingrese un número.")
            continue
        
        if opcion == "1":
            print("Inscripto")
        elif opcion == "2":
            nueva = input("Nueva clave (min 6): ").strip()
            while len(nueva) < 6:
                nueva = input("Error, muy corta. Nueva: ").strip()
            conf = input("Confirme: ").strip()
            if nueva == conf:
                clave_ok = nueva
                print("Clave cambiada.")
            else:
                print("No coinciden.")
        elif opcion == "3":
            print("¡El código es poesía en movimiento!")

            l1 = l2 = l3 = l4 = ""
m1 = m2 = m3 = ""

op = ""
while op != "5":
    print("\n1)Reservar 2)Cancelar 3)Ver Agenda 4)Resumen 5)Salir")
    op = input("Opción: ").strip()
    if op == "1":
        dia = input("1=Lunes, 2=Martes: ")
        nom = input("Paciente: ")
        if dia == "1":
            if nom in [l1, l2, l3, l4]: print("Ya existe.")
            elif l1 == "": l1 = nom
            elif l2 == "": l2 = nom
            elif l3 == "": l3 = nom
            elif l4 == "": l4 = nom
            else: print("Lleno.")
        elif dia == "2":
            if nom in [m1, m2, m3]: print("Ya existe.")
            elif m1 == "": m1 = nom
            elif m2 == "": m2 = nom
            elif m3 == "": m3 = nom
            else: print("Lleno.")
    elif op == "3":
        dia = input("Día a ver (1/2): ")
        if dia == "1":
            print(f"1:{l1 if l1 else '(libre)'} 2:{l2 if l2 else '(libre)'} 3:{l3 if l3 else '(libre)'} 4:{l4 if l4 else '(libre)'}")
        else:
            print(f"1:{m1 if m1 else '(libre)'} 2:{m2 if m2 else '(libre)'} 3:{m3 if m3 else '(libre)'}")
    elif op == "4":
        cl = 0
        if l1: cl+=1
        if l2: cl+=1
        if l3: cl+=1
        if l4: cl+=1
        cm = 0
        if m1: cm+=1
        if m2: cm+=1
        if m3: cm+=1
        print(f"Ocupados - Lunes: {cl}, Martes: {cm}")

        en = 100
t = 12
abiertas = 0
alarma = False
racha = 0

while en > 0 and t > 0 and abiertas < 3 and not alarma:
    print(f"\nE: {en} | T: {t} | Cerraduras: {abiertas}")
    op = input("1.Forzar 2.Hackear 3.Descansar: ")
    if op == "1":
        racha += 1
        en -= 20
        t -= 2
        if racha == 3:
            alarma = True
            print("¡Trabado! Alarma ON.")
        else:
            if en < 40:
                if input("Riesgo! Elegí 1-3: ") == "3": alarma = True
            if not alarma: abiertas += 1
    elif op == "2":
        racha = 0
        en -= 10
        t -= 3
        for i in range(4): print("Hackeando...")
        abiertas += 1
    elif op == "3":
        racha = 0
        en = min(100, en + 15)
        t -= 1

if abiertas == 3: print("¡GANASTE!")
else: print("PERDISTE.")

hp_g = hp_e = 100
pocs = 3

while hp_g > 0 and hp_e > 0:
    print(f"\nTu HP: {hp_g} | Enemigo HP: {hp_e}")
    op = input("1.Pesado 2.Ráfaga 3.Curar: ")
    if op == "1":
        dmg = 15.0
        if hp_e < 20: dmg *= 1.5
        hp_e -= int(dmg)
    elif op == "2":
        for i in range(3):
            hp_e -= 5
            print("Golpe!")
    elif op == "3":
        if pocs > 0:
            hp_g += 30
            pocs -= 1
        else: print("Sin pociones.")
    
    if hp_e > 0:
        hp_g -= 12
        print("El enemigo te golpea!")

if hp_g > 0: print("VICTORIA")
else: print("DERROTA")
