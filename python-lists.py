# La cadena comercial Oxxito necesita una aplicación que le permita manejar
# sus procesos de inventarios, proveedores y venta a público en general.
# Sus necesidades son las siguientes:
# - Registro de ventas
# - Reportes (ventas por día, inventario, proveedores)

# - Llevar un registro de sus proveedores (nombre, número de contacto, empresa)
# --> OK
# - Registro de usuarios del sistema (vendedores) --> OK
listaProveedores = []
listaVendedores = []

# tipoRegistro = 1 --> Proveedor
# tipoRegistro = 2 --> Vendedor
def registra(tipoRegistro):
  if tipoRegistro == 1:
    while True:
      nombre = input('Nombre del proveedor: ')
      numContacto = input('Número telefónico de contacto: ')
      empresa = input('Empresa a la que pertenece: ')
      listaProveedores.append([nombre, numContacto, empresa])
      opc = input('Deseas agregar otro proveedor? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  elif tipoRegistro == 2:
    while True:  
      nombre = input('Nombre del colaborador: ')
      numContacto = input('Número telefónico de contacto: ')
      direccion = input('Escribe la dirección completa del colaborador: ')
      usuario = input('Escribe un nombre de usuario para el colaborador: ')
      password = input('Escribe una contraseña para el colaborador:')
      listaVendedores.append([nombre, numContacto, direccion, usuario, password])
      opc = input('Deseas agregar otro colaborador? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  return

# registra(1)
# print(listaProveedores)
# registra(2)
# print(listaVendedores)

# - Control de inventario (alta, modificación y eliminación de productos)
# Información de los productos:
# - Código de barras
# - Descripción del producto
# - Existencia
# - Precio de compra*
# - Precio de venta*
# - Proveedor
# - Ganancia --

listaInventario = []
def agregaProducto():
  while True:
    cb = input('Código de barras del producto: ')
    descripcion = input('Descripción del producto: ')
    existencia = input('Cantidad a agregar: ')
    pCompra = float(input('Precio de compra: '))
    pVenta = float(input('Precio de venta: '))
    proveedor = input('Proveedor: ')
    ganancia = pVenta - pCompra
    pctGanancia = 100/pCompra*ganancia
    listaInventario.append([cb, descripcion, existencia, pCompra, pVenta, proveedor, ganancia, pctGanancia])
    opc = input('Deseas agregar otro producto? (s/n): ')
    if opc == 'n' or opc == 'N':
      break
  return


def modificaProducto(cb):
  # while True:
  for lista in listaInventario:
    if cb in lista: 
      print(lista)
  return

agregaProducto()
modificaProducto('123')