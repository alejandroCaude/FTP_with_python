from ftplib import FTP
import sys
import os

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
    opcion = sys.argv[1]
    if opcion == "-l":
        Listar(ftp)
    elif opcion == "-d":
        nombre = sys.argv[2]
        Crear(ftp, nombre)
    elif opcion == "-f":
        nombre = sys.argv[2]
        Subir(ftp, nombre)
    elif opcion == "-r":
        nombre = sys.argv[2]
        Eliminar(ftp, nombre)
    ftp.quit()

if __name__ == "__main__":
    # Servidor externo gratuito para pruebas
    FTP_HOST = "192.168.1.35"
    FTP_PORT=12400
    FTP_USER = "user"
    FTP_PASS = "password" # este password puede cambiar
    main()

