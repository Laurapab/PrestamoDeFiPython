from PrestamoDeFi import *

def mostrar_menu():
    print("Bienvenido al sistema de préstamos DeFi")
    print("Seleccione una opción:")
    print("1. Dar de alta un prestamista")
    print("2. Dar de alta un cliente")
    print("3. Depositar garantía")
    print("4. Solicitar un préstamo")
    print("5. Aprobar un préstamo")
    print("6. Reembolsar un préstamo")
    print("7. Liquidar garantía")
    print("8. Obtener préstamos por prestatario")
    print("9. Obtener detalle de préstamo")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción: ")
        if opcion == '1':
            nuevo_prestamista_address = input("Ingrese la dirección Ethereum del nuevo prestamista: ")
            alta_prestamista(nuevo_prestamista_address)
        elif opcion == '2':ValueError: {'message': 'VM Exception while processing transaction: revert No estas registrado como cliente', 'stack': 'CallError: VM Exception while processing transaction: revert No estas registrado como cliente\n    at Blockchain.simulateTransaction (C:\\Program Files\\WindowsApps\\GanacheUI_2.7.1.0_x64__rb4352f0jd4m2\\app\\resources\\static\\node\\node_modules\\ganache\\dist\\node\\1.js:2:72658)', 'code': -32000, 'name': 'CallError', 'data': '0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000204e6f206573746173207265676973747261646f20636f6d6f20636c69656e7465'}

            nuevo_cliente_address = input("Ingrese la dirección Ethereum del nuevo cliente: ")
            prestamista_address = input("Ingrese la dirección Ethereum del prestamista que registra al cliente: ")
            prestamista_private_key = input("Ingrese la clave privada del prestamista: ")
            alta_cliente(nuevo_cliente_address, prestamista_address, prestamista_private_key)
        elif opcion == '3':
            direccion_cliente = input("Ingrese la dirección Ethereum del cliente: ")
            valor = input("Ingrese el monto de la garantía a depositar: ")
            clave_privada_cliente = input("Ingrese la clave privada del cliente: ")
            depositar_garantia(direccion_cliente, valor, clave_privada_cliente)
        elif opcion == '4':
            direccion_cliente = input("Ingrese la dirección Ethereum del cliente que solicita el préstamo: ")
            monto = input("Ingrese el monto del préstamo solicitado: ")
            plazo = input("Ingrese el plazo del préstamo en segundos: ")
            clave_privada_cliente = input("Ingrese la clave privada del cliente: ")
            solicitar_prestamo(direccion_cliente, monto, plazo, clave_privada_cliente)
        elif opcion == '5':
            prestatario_address = input("Ingrese la dirección Ethereum del prestatario: ")
            prestamo_id = input("Ingrese el ID del préstamo a aprobar: ")
            prestamista_address = input("Ingrese la dirección Ethereum del prestamista: ")
            prestamista_private_key = input("Ingrese la clave privada del prestamista: ")
            aprobar_prestamo(prestatario_address, prestamo_id, prestamista_address, prestamista_private_key)
        elif opcion == '6':
            prestamo_id = input("Ingrese el ID del préstamo a reembolsar: ")
            cliente_address = input("Ingrese la dirección Ethereum del cliente: ")
            cliente_private_key = input("Ingrese la clave privada del cliente: ")
            reembolsar_prestamo(prestamo_id, cliente_address, cliente_private_key)
        elif opcion == '7':
            prestamo_id = input("Ingrese el ID del préstamo cuya garantía será liquidada: ")
            prestamista_address = input("Ingrese la dirección Ethereum del prestamista: ")
            prestamista_private_key = input("Ingrese la clave privada del prestamista: ")
            liquidar_garantia(prestamo_id, prestamista_address, prestamista_private_key)
        elif opcion == '8':
            prestatario_address = input("Ingrese la dirección Ethereum del prestatario: ")
            prestamos = obtener_prestamos_por_prestatario(prestatario_address)
            print("Préstamos del prestatario:", prestamos)
        elif opcion == '9':
            prestatario_address = input("Ingrese la dirección Ethereum del prestatario: ")
            prestamo_id = input("Ingrese el ID del préstamo a consultar: ")
            detalle = obtener_detalle_de_prestamo(prestatario_address, prestamo_id)
            print("Detalle del préstamo:", detalle)
        elif opcion == '0':
            print("¡Gracias por usar nuestro sistema!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()