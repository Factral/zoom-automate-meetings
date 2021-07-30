from datetime import *
import datetime as dt
import csv
import os
import sys
import schedule
import pause


def terminarprogama():
    input("\n*presiona ENTER para salir* ....")
    sys.exit(0)


def main():
    # abre el archivo y chekea si es un csv
    try:
        archivo = open(sys.argv[1])
        archivo.close()
        if not sys.argv[1].endswith(".csv"):
            raise ValueError
    except FileNotFoundError:
        print("\nERROR: El archivo no existe")
        print("Introduce un archivo valido, preferiblemente que el archivo este en la misma carpeta")
        terminarprogama()
    except ValueError:
        print("\nERROR: Porfavor introduce un archivo valido, con extension csv")
        terminarprogama()

    ReunionNoEncontrada = [True, True]

    with open(sys.argv[1]) as csv_file:
        ArchivoReuniones = csv.reader(csv_file, delimiter=',')
        next(ArchivoReuniones)
        for row in ArchivoReuniones:
            if int(row[0]) == datetime.today().isoweekday():
                ReunionNoEncontrada[0] = False
                classtime = int(row[1].split(":")[0]) * 60 + int(row[1].split(":")[1])
                hora = int(datetime.now().strftime("%H")) * 60 + int(datetime.now().strftime("%M"))
                if (hora > classtime - 5) and (hora < classtime + int(row[4])):
                    ReunionNoEncontrada[1] = False
                    print("\nEntrando a la reunion....")
                    print("Reunion: {}".format(row[5]))
                    print("Duracion: {}:{:02d} horas".format(*divmod(int(row[4]), 60)))
                    os.system(
                        r"%appdata%\Zoom\bin\Zoom.exe --url=zoommtg://zoom.us/join?confno=" + row[2] + "^&pwd=" + row[
                            3])
                    future = dt.datetime.combine(dt.date.today(), dt.time(int(row[1].split(":")[0]),
                                                                          int(row[1].split(":")[1]))) + dt.timedelta(
                        minutes=int(row[4]))
                    print("La reunion acaba a las: {}:{:02d} son las {}:{:02d}".format(future.time().hour,
                                                                                       future.time().minute,
                                                                                       datetime.now().hour,
                                                                                       datetime.now().minute))
                    print("\n..El programa va a esperar a que acabe la reunion..")
                    pause.until(future)
                    print("\n\nla reunion ACABo\n")
                    os.system("taskkill /f /im zoom.exe")
                    # vuelve a ejecutar la funcion y verificar si hay reuniones para el momento
                    main()
                    break
                else:
                    if hora < classtime:
                        ReunionNoEncontrada[1] = False
                        print("\n** No se encontraron reuniones para este momento **")
                        print("- La siguiente reunion sera: {}".format(row[5]))
                        print("- A las: {}".format(row[1]))
                        break
        if ReunionNoEncontrada[0]:
            print("\n** No hay ninguna reunion programada para este dia **")
            terminarprogama()
        if ReunionNoEncontrada[1]:
            print("\n** Ya no quedan mas reuniones para hoy **")
            terminarprogama()


print("\nReuniones Zoom Automaticas Version 0.0.1")
print("Cargado e inicializado")
main()
schedule.every(15).minutes.do(main)

while True:
    schedule.run_pending()
    pause.seconds(1)
