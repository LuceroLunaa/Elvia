usuario_ = "manager"
usuario_2 = "validador"
usuario_3 = "restringido"

print("Bienvenido a BBVA")

usuario = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if usuario == usuario_ or usuario == usuario_2 or usuario == usuario_3:
    print("Bienvenido ", usuario)
else:
    print("Usuario inválido")