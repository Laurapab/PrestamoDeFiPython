from web3 import Web3
from eth_account import Account
import json


web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

contract_address = web3.to_checksum_address('0x9E3871ccC6f3Fe9b3ea06f9361483E28D46B339E')
contract_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"GarantiaLiquidada","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"PrestamoAprobado","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"PrestamoReembolsado","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"plazo","type":"uint256"}],"name":"SolicitudPrestamo","type":"event"},{"inputs":[{"internalType":"address","name":"nuevoCliente","type":"address"}],"name":"altaCliente","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"nuevoPrestamista","type":"address"}],"name":"altaPrestamista","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"aprobarPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"clientes","outputs":[{"internalType":"bool","name":"activado","type":"bool"},{"internalType":"uint256","name":"saldoGarantia","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositarGarantia","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"empleadosPrestamista","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"liquidarGarantia","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"obtenerDetalleDePrestamo","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"prestatario","type":"address"},{"internalType":"uint256","name":"monto","type":"uint256"},{"internalType":"uint256","name":"plazo","type":"uint256"},{"internalType":"uint256","name":"tiempoSolicitud","type":"uint256"},{"internalType":"uint256","name":"tiempoLimite","type":"uint256"},{"internalType":"bool","name":"aprobado","type":"bool"},{"internalType":"bool","name":"reembolsado","type":"bool"},{"internalType":"bool","name":"liquidado","type":"bool"}],"internalType":"struct PrestamoDeFi.Prestamo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"}],"name":"obtenerPrestamosPorPrestatario","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"reembolsarPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"socioPrincipal","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"monto_","type":"uint256"},{"internalType":"uint256","name":"plazo_","type":"uint256"}],"name":"solicitarPrestamo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]')

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def sign_and_send_raw_tx(transaction, private_key):
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash

def alta_prestamista(nuevo_prestamista_address):

    socio_principal_private_key = '0x29905172112b6c394d3de1aa4823ea3dcb58ba86a9989362744e848dfe940ad1'
    transaction = contract.functions.altaPrestamista(nuevo_prestamista_address).build_transaction({
        'from': web3.eth.accounts[0],
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    tx_hash = sign_and_send_raw_tx(transaction, socio_principal_private_key)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)

def alta_cliente(nuevo_cliente_address, prestamista_address, prestamista_private_key):

    transaction = contract.functions.altaCliente(nuevo_cliente_address).build_transaction({
        'from': prestamista_address,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(prestamista_address),
    })
    tx_hash = sign_and_send_raw_tx(transaction, prestamista_private_key)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)

def depositar_garantia(direccion_cliente, valor, clave_privada_cliente):
    valor = web3.to_wei(valor, 'ether')

    transaction = contract.functions.depositarGarantia().build_transaction({
        'from': direccion_cliente,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'value': valor,
        'nonce': web3.eth.get_transaction_count(direccion_cliente),
    })
    tx_hash = sign_and_send_raw_tx(transaction, clave_privada_cliente)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)

def solicitar_prestamo(direccion_cliente, monto, plazo, clave_privada_cliente):
    transaction = contract.functions.solicitarPrestamo(int(monto), int(plazo)).build_transaction({
        'from': direccion_cliente,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(direccion_cliente),
    })
    tx_hash = sign_and_send_raw_tx(transaction, clave_privada_cliente)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)
    prestamo_id = contract.functions.solicitarPrestamo(int(monto), int(plazo)).call()
    print("ID Prestamo", prestamo_id)

def aprobar_prestamo(prestatario_address, prestamo_id, prestamista_address, prestamista_private_key):
  try:
      prestamo_id_int = int(prestamo_id)

 
        nonce = w3.eth.get_transaction_count(prestamista_address)
      txn_dict = contract.functions.aprobarPrestamo(prestatario_address, prestamo_id_int).build_transaction({
          'from': prestamista_address,
          'chainId': 1337,
          'gas': 2000000,
          'gasPrice': w3.to_wei('50', 'gwei'),
          'nonce': nonce,
      })

        txn_receipt = enviar_transaccion(w3, txn_dict, prestamista_private_key)
      if txn_receipt.status == 1:
          return "Préstamo aprobado exitosamente."
      else:
          return "La transacción de aprobación falló."

 
    except Exception as e:
      return str(e)  # Devolver el mensaje de error
 

def reembolsar_prestamo(prestamo_id, cliente_address, cliente_private_key):
    transaction = contract.functions.reembolsarPrestamo(int(prestamo_id)).build_transaction({
        'from': cliente_address,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(cliente_address),
    })

    tx_hash = sign_and_send_raw_tx(transaction, cliente_private_key)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)


def liquidar_garantia(prestamo_id, prestamista_address, prestamista_private_key):
    transaction = contract.functions.liquidarGarantia(int(prestamo_id)).build_transaction({
        'from': prestamista_address,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(prestamista_address),
    })
    tx_hash = sign_and_send_raw_tx(transaction, prestamista_private_key)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacción completada:", receipt)


def obtener_prestamos_por_prestatario(prestatario_address):
    prestamos = contract.functions.obtenerPrestamosPorPrestatario(prestatario_address).call()
    return prestamos

def obtener_detalle_de_prestamo(prestatario_address, prestamo_id):
    detalle_prestamo = contract.functions.obtenerDetalleDePrestamo(prestatario_address, prestamo_id).call()
    return detalle_prestamo