import datetime
# La cadena comercial Oxxito necesita una aplicación que le permita manejar
# sus procesos de inventarios, proveedores y venta a público en general.
# Sus necesidades son las siguientes:
# - Registro de ventas --> TAREA
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

# Sección de declaración de variables globales
listaInventario = []
listaMovimientos = []
numInventario = 0
numAjuste = 0
listaRegistroVenta = []
numVenta = len(listaRegistroVenta)

listaInventario =[ 
  [123, 'Gansito Marinela', 4, 7.50, 12.00, 'Marinela', 4.50, 60.0],
  [321, 'Chips Jalapeño', 7, 10.9, 15.00, 'Barcel', 5.10, 46.79]
]

# Sección de funciones
def agregaProducto():
  while True:
    cb = int(input('Código de barras del producto: '))
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
        listaInventario[i][6] = round(float(listaInventario[i][4] - listaInventario[i][3]), 2)
        listaInventario[i][7] = round(float(100/listaInventario[i][3]*listaInventario[i][6]), 2)
      else:
        listaInventario[i][opc-1] = input('Escribe el nuevo valor: ')
      opc = input('Deseas modificar otro detalle del producto? (s/n): ')
      if opc == 'n' or opc == 'N':
        break
  else:
    print('¡Error... producto NO encontrado!')
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
  return

def getDate():
  date = datetime.datetime.now()
  month = ''
  day = ''
  year = ''
  date = datetime.datetime.now()
  if date.day < 10:
    day = '0'+str(date.day)
  else:
    day = str(date.day)
  if date.month < 10:
    month = '0'+str(date.month)
  else:
    month = str(date.month)
  if date.year < 10:
    year = '0'+str(date.year)
  else:
    year = str(date.year)
  return day+'/'+month+'/'+year

def getHour():
  hour = ''
  minute = ''
  second = ''
  date = datetime.datetime.now()
  if date.hour < 10:
    hour = '0'+str(date.hour)
  else:
    hour = str(date.hour)
  if date.minute < 10:
    minute = '0'+str(date.minute)
  else:
    minute = str(date.minute)
  if date.second < 10:
    second = '0'+str(date.second)
  else:
    second = str(date.second)
  return hour+':'+minute+':'+second

def registraMovimiento(fecha, hora, tipoMovimiento, i, cantidad, razon=False, numV=0):
    habia = 0
    hay = 0
    if tipoMovimiento == 'Entrada':
      global numInventario
      numInventario +=1
      hay = listaInventario[i][2] + cantidad
      habia = listaInventario[i][2]
      movimiento = f'Recepción de inventario #{numInventario}'
    elif tipoMovimiento == 'Salida':
      habia = listaInventario[i][2] + cantidad
      hay = listaInventario[i][2]
      movimiento = f'Venta #{numV}'
    elif tipoMovimiento == 'Devolución':
      hay = listaInventario[i][2] + cantidad
      habia = listaInventario[i][2]      
      movimiento = f'Devolución de venta #{numV}'
    elif tipoMovimiento == 'Ajuste':
      global numAjuste
      numAjuste += 1
      habia = listaInventario[i][2]
      hay = listaInventario[i][2] + cantidad
      movimiento = f'Ajuste #{numAjuste}: {razon}'
    listaMovimientos.append([
      fecha,
      hora,
      listaInventario[i][1],
      movimiento,
      habia,
      tipoMovimiento,
      cantidad,
      hay
    ])
    return

def agregaInventario(cb):
  i = buscaProducto(cb)
  if(i >= 0):
    print('numInventario',numInventario)
    print('Código de barras:', listaInventario[i][0])
    print('Descripción:', listaInventario[i][1])
    print('Existencia:', str(listaInventario[i][2]))
    cantidad = float(input('Escribe la cantidad a agregar: '))
    registraMovimiento(getDate(), getHour(), 'Entrada', i, cantidad)
    listaInventario[i][2] += cantidad
  else:
    print('¡Error... producto NO encontrado!')
  return

def ajustaInventario(cb):
  i = buscaProducto(cb)
  if i>= 0:
    print('Código de barras:', listaInventario[i][0])
    print('Descripción:', listaInventario[i][1])
    print('Existencia:', listaInventario[i][2])
    cantidad = int(input('Cantidad a ajustar (la cantidad puede ser positiva o negativa): '))
    razon = input('Motivo del ajuste: ')
    registraMovimiento(getDate(), getHour(), 'Ajuste', i, cantidad, razon)
    listaInventario[i][2] += cantidad
  else:
    print('¡Error... producto NO encontrado!')

def reporteInventario():
  print('C. de barras\tDescripción\t\tExist.\tP.Compra\tP.Vta\tProveedor\t%Ganancia')
  for producto in listaInventario:
    pv = producto[4]
    cb = producto[0]
    prov = producto[5]
    exist = producto[2]
    pct = producto[7]
    pc = producto[3]
    desc = producto[1]
    print(f'{cb}\t{desc}\t{exist}\t${pc}\t\t${pv}\t{prov}\t{pct}%')

def reporteProveedores():
  print('Nombre del proveedor\t\tNúmero de contacto\tEmpresa')
  for proveedor in listaProveedores:
    detalleProv = '{}\t\t\t{}\t\t{}'
    print(detalleProv.format(proveedor[0], proveedor[1], proveedor[2]))

def registraVentas():
  global numVenta
  listaProductosxVender = []
  importe = 0
  while True:
    while True:
      update = False
      cb = int(input('Código de barras del producto: '))
      producto = buscaProducto(cb)
      print('Código de barras:',str(listaInventario[producto][0]))
      print("Descripción:",str(listaInventario[producto][1]))
      print('Precio: $',str(listaInventario[producto][4]))
      while True:
        cantidad = float(input('Cantidad a vender:'))
        if(listaInventario[producto][2] < cantidad and cantidad >0):
          print('No hay existencia suficiente, intenta con otra cantidad, o escribe -1 para continuar....')
        elif cantidad == -1:
          break
        else:
          listaInventario[producto][2] -= cantidad
          break
      if cantidad !=  -1:
        importe += cantidad * listaInventario[producto][4]
      print('El importe es $'+str(importe))
      for elementos in listaProductosxVender:
        indice = listaProductosxVender.index(elementos)
        if cb in elementos:
          listaProductosxVender[indice][3] += cantidad
          listaProductosxVender[indice][4] = listaProductosxVender[indice][3] * listaProductosxVender[indice][2]
          update = True
          break
      if not update:
        listaProductosxVender.append([cb, listaInventario[producto][1], listaInventario[producto][4], cantidad, cantidad*listaInventario[producto][4]])
      opc = input('Deseas seguir vendiendo? (s/n):')
      if opc == 'n' or opc == 'N':
        break
    opc = int(input('1--> Finalizar compra, 2-->Vender otro producto: '))
    if opc == 1:
      break
  while True:
    print('El total es $'+str(importe))
    pagar = float(input('Con cuánto paga?'))
    if pagar < importe:
      print('Te falta dinero para completar el importe, no te hagas wey!')
    else:
      print('Tu cambio es $'+str(pagar - importe))
      print('Gracias por su compra, vuelva pronto (=')
      numVenta += 1
      registro = [getDate(), getHour(), numVenta, listaProductosxVender]
      listaRegistroVenta.append(registro)
      for producto in listaProductosxVender:
        i = buscaProducto(producto[0])
        registraMovimiento(registro[0], registro[1], 'Salida', i, producto[3], False, registro[2])
      break

# Reportes de ventas:
# - Por día --> fecha(día/mes/año)
# - Por mes
#   * Mes natural --> desde fecha inicial (día actual/mes anterior/año) hasta fecha final (actual)
#   * Mes calendario --> desde 1er día del mes actual hasta último día del mes actual
# - Por año --> TAREA
#   * Año natural --> desde día/mes/año anterior hasta día/mes/año actual
#   * Año calendario --> desde el primer día del año hasta la fecha actual
# - Por periodo personalizado (fechas) --> TAREA
#   * Desde una fecha inicial hasta una fecha final elegida por el usuario
def menu():
  print('''
  --- Reporte de ventas ---
  1. Ventas por día
  2. Ventas por mes
  3. Ventas por año
  4. Ventas por periodo
  ''')
  opc = input('Elige un tipo de reporte: ')
  if opc == '1': 
    dia = input('Escribe el día: ')
    mes = input('Escribe el mes: ')
    anio = input('Escribe el año: ')
    ventasDia(dia, mes, anio)
  elif opc == '2':
    print('''
      1. Mes natural
      2. Mes calendario
      ''')
    opc = input('Elige el tipo de mes: ')    
    ventaMes(opc)
   
def ventaMes(opc):
  print('#Vta\tFecha\t\tHora\tDescripción\tCantidad\tPrecio\tImporte')
  fechaActual = getDate().split('/')
  if opc == '1':
    fechaMesAnterior = [fechaActual[0], str(f'0{int(fechaActual[1])-1}' if int(fechaActual[1])-1<10 else int(fechaActual[1])-1), fechaActual[2]]
    if fechaMesAnterior[1] == '00':
      fechaMesAnterior[1] = '12'
      fechaMesAnterior[2] = str(int(fechaActual[2])-1)
    for ventas in listaRegistroVenta:
      fechapro=ventas[0].split("/")
      print(fechapro)
      diaproducto=int(fechapro[0])
      diamespasado=int(fechaMesAnterior[0])
      diaactual=int(fechaActual[0])
      if fechapro[2]==fechaMesAnterior[2] or fechaMesAnterior[1]=="12":
        if (fechapro[1] == fechaActual[1] and diaproducto <= diaactual) or (fechapro[1] == fechaMesAnterior[1] and diaproducto >= diaactual)
          print(ventas)
  elif opc=="2":
    fechahoy = getDate().split('/')
    diahoy=int(fechahoy[0])
    for ventas in listaRegistroVenta:
      fechapro=ventas[0].split("/")
      diaproducto=int(fechapro[0])
      if (fechahoy[2]==fechapro[2] and fechahoy[1]==fechapro[1]) and (diaproducto<=diahoy):
          print(ventas)
   
# registraVentas()
ventaMes('1')

def ventasDia(dia, mes, anio):
  print('#Vta\tFecha\t\tHora\tDescripción\tCantidad\tPrecio\tImporte')
  for venta in listaRegistroVenta:
    fecha = venta[0].split('/')
    if dia in fecha and mes in fecha and anio in fecha:
      fecha = venta[0]
      hora = venta[1]
      nVenta = venta[2]
      for producto in venta[3]:
        descripcion = producto[1]
        cantidad = producto[3]
        precio = producto[2]
        importe = producto[4]
        detalleVenta = '{}\t{}\t{}\t{}\t{}\t{}\t{}' 
        print(detalleVenta.format(nVenta, fecha, hora, descripcion, cantidad, precio, importe))

def cancelaVenta(numVenta):
  cantidad = 0
  for venta in listaRegistroVenta:
    if numVenta in venta:
      venta.append('CANCELADA')
      for productos in venta[3:-1]:
        for producto in productos:
          cantidad = producto[3]
          registraMovimiento(getDate(), getHour(), 'Devolución', buscaProducto(producto[0]), cantidad, False, numVenta)
          listaInventario[buscaProducto(producto[0])][2] += cantidad
      break

def cancelaProducto(numVenta, cb):
  found = False
  for venta in listaRegistroVenta:
    if numVenta in venta:
      for productos in venta[3:]:
        for producto in productos:
          if cb in producto:
            registraMovimiento(getDate(), getHour(), 'Devolución', buscaProducto(producto[0]), producto[3], False, numVenta)
            listaInventario[buscaProducto(producto[0])][2] += producto[3]
            del venta[venta.index(productos)][productos.index(producto)]
            found = True
            break
        if found == True: break
      if found == True: break

# registraVentas()
# print(listaMovimientos)
# cancelaVenta(1)
# cancelaProducto(1, 123)
# print('lista de movimientos: ',listaMovimientos)
# print('reg. Venta: ',listaRegistroVenta)
# print('reg. inventario: ',listaInventario)

# ajustaInventario(123)
# print(listaMovimientos)

# reporteVentas('5','5','2020')

