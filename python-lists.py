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

# - Control de inventario:
#   * Alta, modificación y eliminación de productos --> OK
#   * Agregar inventario (agregar existencias)
#   * Ajuste de inventario (modificar existencias)
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
    existencia = float(input('Cantidad a agregar: '))
    pCompra = float(input('Precio de compra: '))
    pVenta = float(input('Precio de venta: '))
    proveedor = input('Proveedor: ')
    ganancia = round(pVenta - pCompra, 2)
    pctGanancia = round(100/pCompra*ganancia, 2)
    listaInventario.append([cb, descripcion, existencia, pCompra, pVenta, proveedor, ganancia, pctGanancia])
    opc = input('Deseas agregar otro producto? (s/n): ')
    if opc == 'n' or opc == 'N':
      break
  return


def buscaProducto(cb):
  i = 0
  for lista in listaInventario:
    if cb in lista: 
      i = listaInventario.index(lista)
      return i
  return -1

def modificaProducto(cb):
  i = buscaProducto(cb)
  if(i >= 0):
    while True:      
      print('1. Código de barras:', listaInventario[i][0])
      print('2. Descripción:', listaInventario[i][1])
      print('3. Existencia:', listaInventario[i][2])
      print('4. Precio de compra:', listaInventario[i][3])
      print('5. Precio de venta:', listaInventario[i][4])
      print('6. Proveedor:', listaInventario[i][5])
      opc = int(input('Elige un número de opción a modificar: '))
      if opc == 3 or opc == 4 or opc == 5:
        listaInventario[i][opc-1] = float(input('Escribe el nuevo valor: '))
        # round(numero, decimales) --> función de redondeo
        listaInventario[i][6] = round(float(listaInventario[i][4] - listaInventario[i][3]), 2)
        listaInventario[i][7] = round(float(100/listaInventario[i][3]*listaInventario[i][6]), 2)
      else:
        listaInventario[i][opc-1] = input('Escribe el nuevo valor: ')
      opc = input('Deseas modificar otro detalle del producto? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  else:
    print('¡Error... producto NO encontrado!')
  #print(listaInventario[i])
  return

def eliminaProducto(cb):
  i = buscaProducto(cb)
  if(i >= 0):
    print('1. Código de barras:', listaInventario[i][0])
    print('2. Descripción:', listaInventario[i][1])
    print('3. Existencia:', listaInventario[i][2])
    print('4. Precio de compra:', listaInventario[i][3])
    print('5. Precio de venta:', listaInventario[i][4])
    print('6. Proveedor:', listaInventario[i][5])
    opc = input('Estás seguro de que deseas eliminar este producto? (s/n): ')
    if opc == 'n' or opc == 'N':
      return
    else:
      del listaInventario[i]
  else:
    print('¡Error... producto NO encontrado!')
  
  #print(listaInventario)
  return

def agregaInventario(cb):
  i = buscaProducto(cb)
  if(i >= 0):
    print('Código de barras:', listaInventario[i][0])
    print('Descripción:', listaInventario[i][1])
    print('Existencia:', listaInventario[i][2])
    existencia = float(input('Escribe la cantidad a agregar: '))
    #listaInventario[i][2] = float(existencia + listaInventario[i][2])
    listaInventario[i][2] += existencia
  else:
    print('¡Error... producto NO encontrado!')

  #print(listaInventario[i])
  return

agregaProducto()
modificaProducto('123')
# eliminaProducto('123')
agregaInventario('123')