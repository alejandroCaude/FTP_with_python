from ftplib import FTP
import os
import sys
#****************************************************************
#*Hay que pasar el nombre de usuario y contraseña por parametros*
#****************************************************************
def Listar(ftp):
    print("Lista:")
    ftp.retrlines("LIST")

def Crear(ftp, nombre):
    ftp.mkd(nombre)
    print(f"Directorio {nombre} creado.")

def Subir(ftp, nombre):
    with open(nombre, "rb") as file:
        ftp.storbinary(f"STOR {nombre}", file)
    print(f"Archivo {nombre} subido.")

def descargar(ftp,nombre):
    with open(filename, "wb") as f:
        ftp.retrbinary("RETR " + filename, f.write)

def Eliminar(ftp, nombre):
    if os.path.exists(nombre):
        ftp.delete(nombre)
        print(f"Archivo {nombre} eliminado.")
    else:
        print("El fichero no existe o no se encuentra en el directorio")
        print("Listando archivos:")
        ftp.retrlines("LIST")
        

def main():
    ftp = FTP()
    ftp.connect(FTP_HOST,FTP_PORT)
    ftp.login(FTP_USER,FTP_PASS)
    ftp.encoding = "utf-8"
    while True:
        cmd = input("Comandos(list, cd, get, put, mkdir, rm, quit): ")
        if cmd == "list":
            Listar(ftp)
        elif cmd == "cd":
            print("cambia de directorio")
        elif cmd == "get":
            nombre = input("¿Qué fichero quieres descargar?: ")
            descargar(ftp, nombre)
        elif cmd == "put":
            nombre = input("archivo a subir: ")
            Subir(ftp, nombre)
        elif cmd == "mkdir":
            nombre = input("Nombre directorio a crear: ")
            Crear(ftp, nombre)
        elif cmd == "rm":
            nombre = input("Nombre directorio a borrar: ")
            Eliminar(ftp, nombre)
        elif cmd == "quit":
            ftp.quit()
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    # Servidor externo gratuito para pruebas
    FTP_HOST = "192.168.1.36"
    FTP_PORT=2121
    FTP_USER = sys.argv[1]
    FTP_PASS = sys.argv[2] # este password puede cambiar
    main()

