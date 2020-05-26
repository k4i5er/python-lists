import datetime
import calendar
import sys
import dateutil.relativedelta
# La cadena comercial Oxxito necesita una aplicación que le permita manejar
# sus procesos de inventarios, proveedores y venta a público en general.
# Sus necesidades son las siguientes:
# - Registro de ventas --> TAREA
# - Reportes (ventas por día, inventario, proveedores)

# - Llevar un registro de sus proveedores (nombre, número de contacto, empresa)
# --> OK
# - Registro de usuarios del sistema (vendedores) --> OK
# Sección de declaración de variables globales
listaInventario = []
listaMovimientos = []
numInventario = 0
numAjuste = 0
listaRegistroVenta = []
numVenta = len(listaRegistroVenta)
listaProveedores = []
listaVendedores = []

listaInventario =[ 
  [123, 'Gansito Marinela', 4, 7.50, 12.00, 'Marinela', 4.50, 60.0],
  [321, 'Chips Jalapeño', 7, 10.9, 15.00, 'Barcel', 5.10, 46.79]
]

# Sección de funciones

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

def agregaProducto():
  while True:
    while True:
      try:
        cb = int(input('Código de barras del producto: '))
        break
      except ValueError:
        print("Inserta solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
    descripcion = input('Descripción del producto: ')
    while True:
      try:
        existencia = float(input('Cantidad a agregar: '))
        break
      except ValueError:
        print("Inserta solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")

    while True:
      try:
        pCompra = float(input('Precio de compra: '))
        break
      except ValueError:
        print("Ingresa solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
    while True:
      try:
        pVenta = float(input('Precio de venta: '))
        break
      except ValueError:
        print("Ingresa solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
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
      while True:
        try:
          opc = int(input('Elige un número de opción a modificar: '))
          if 1<=opc<=6:
            break
          else:
            print("Escribe un numero entre 1 y 6")
        except ValueError:
          print("Pon solo numeros")
        except KeyboardInterrupt:
          print("No puedes cancelar")        
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
  return datetime.date.today() # datetime.datetime.strptime(date, '%d/%m/%Y')

def getHour():
  date = datetime.datetime.today()
  return datetime.time(date.hour, date.minute, date.second) # datetime.datetime.strptime(date, '%H:%M:%S')


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
    while True:
      try:
        cantidad = float(input('Escribe la cantidad a agregar: '))
        break
      except ValueError:
        print("Ingresa solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
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
    while True:
      try:
        cantidad = int(input('Cantidad a ajustar (la cantidad puede ser positiva o negativa): '))
        break
      except ValueError:
        print("Ingresa solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
    razon = input('Motivo del ajuste: ')
    registraMovimiento(getDate(), getHour(), 'Ajuste', i, cantidad, razon)
    listaInventario[i][2] += cantidad
  else:
    print('¡Error... producto NO encontrado!')
  return

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
  return

def reporteProveedores():
  print('Nombre del proveedor\t\tNúmero de contacto\tEmpresa')
  for proveedor in listaProveedores:
    detalleProv = '{}\t\t\t{}\t\t{}'
    print(detalleProv.format(proveedor[0], proveedor[1], proveedor[2]))
  return

def registraVentas():
  global numVenta
  listaProductosxVender = []
  importe = 0
  while True:
    while True:
      update = False
      while True:
        try:
          cb = int(input('Código de barras del producto: '))
          break
        except ValueError:
          print("Introduce solo numeros")
        except KeyboardInterrupt:
          print("No puedes cancelar")
      producto = buscaProducto(cb)
      print('Código de barras:',str(listaInventario[producto][0]))
      print("Descripción:",str(listaInventario[producto][1]))
      print('Precio: $',str(listaInventario[producto][4]))
      while True:
        while True:
          try:
            cantidad = float(input('Cantidad a vender:'))
            break
          except ValueError:
            print("Ingresa solo numeros")
          except KeyboardInterrupt:
            print("No puedes cancelar")
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
    while True:
      try:
        opc = int(input('1--> Finalizar compra, 2-->Vender otro producto: '))
        if 1<=opc<=2:
          break
        else:
          print("Ingresa 1 o 2")
      except ValueError:
        print("Ingresa Solo numero")
      except KeyboardInterrupt:
        print("No puedes cancelar")
    if opc == 1:
      break
  while True:
    print('El total es $'+str(importe))
    while True:
      try:
        pagar = float(input('Con cuánto paga?'))
        break
      except ValueError:
        print("Ingresa solo numeros")
      except KeyboardInterrupt:
        print("No puedes cancelar")
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
  return

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
#   desde enero hasta marzo => 01/01/año actual hasta 30/03/año actual
#   desde 15 enero hasta el 23 marzo => 15/01/año actual hasta 23/marzo/año actual
#   desde 5 junio 2018 hasta 4 abril 2020 => 05/06/2018 hasta 04/04/2020
#   validar fechas
#
#   desde una fecha inicial hasta la fecha actual
#   desde año inicial hasta año final
#   desde una fecha inicial hasta una fecha final
#   desde mes/año inicial hasta mes/año final
#
#   periodo: 29/02/2019 hasta 04/04/2020

def reporteVentas():
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
    ventasMes(opc)
  elif opc == '3':
    while True:
      try:
        print('''
          1. Año natural
          2. Año calendario
          ''')
        opc = int(input('Elige el tipo de año: '))
        if 1 <= opc <= 2:
          ventasAnio(opc)
          break
        else:
          print('Escribe 1 o 2')
      except ValueError:
        print('¡ERROR! Escribe sólo números enteros')
      except KeyboardInterrupt:
        print('\n¡ERROR! El proceso no puede ser cancelado')

# sys.exit() <--- Finalizar un programa y salir al sistema

  elif opc == '4':
    i = 0
    while i < 2:
      msg = 'inicial' if i == 0 else 'final'
      while True:
        anio = int(input(f'Escribe el año {msg}:'))
        if 2000 < anio <= getDate().year:
          break
        else:
          print(f'Año fuera de rango, escribe un año entre 2001 y {getDate().year}')
      while True:
        mes = int(input(f'Escribe el mes {msg}:'))
        if 1 <= mes <= 12:
          break
        else:
          print('Mes fuera de rango, escribe un número entre 1 y 12')
      while True:
        dia = int(input(f'Escribe el día {msg}:'))
        if 1 <= dia <= calendar.monthrange(anio, mes)[1]:
          break
        else:
          print(f'Día fuera de rango, escribe un número entre 1 y {calendar.monthrange(anio, mes)[1]}')
      if i == 0:
        fechaInicial = datetime.date(anio, mes, dia)
      else:
        fechaFinal = datetime.date(anio, mes, dia)
      i += 1
    if fechaInicial <= fechaFinal:
      ventasPersonalizadas(fechaInicial, fechaFinal)
    else:
      ventasPersonalizadas(fechaFinal, fechaInicial)
  return

def ventasMes(opc):
  print('#Vta\tFecha\t\tHora\tDescripción\tCantidad\tPrecio\tImporte')
  fechaActual = getDate()
  if opc == '1':
    fechaMesAnterior = fechaActual - dateutil.relativedelta.relativedelta(months=1)
    # [
    #   fechaActual[0], 
    #   '12' if int(fechaActual[1])-1 == 0 else 
    #   f'0{int(fechaActual[1])-1}' if int(fechaActual[1])-1<10 and int(fechaActual[1])-1>0 else 
    #   f'{int(fechaActual[1])-1}', 
    #   f'{int(fechaActual[2])-1}' if int(fechaActual[1]) == 1 else f'{fechaActual[2]}'
    #   ]
    for ventas in listaRegistroVenta:
      fechaVenta=ventas[0]
      print(fechaVenta)
      diaVenta = fechaVenta.day #int(fechaVenta[0])
      diaActual = fechaActual.day # int(fechaActual[0])
      if fechaVenta.year == fechaMesAnterior.year or fechaMesAnterior.month == 12: # fechaVenta[2]==fechaMesAnterior[2] or fechaMesAnterior[1]=="12":
        if (fechaVenta.month == fechaActual.month and diaVenta == diaActual) or (fechaVenta.month == fechaMesAnterior.month and diaVenta >= diaActual):# (fechaVenta[1] == fechaActual[1] and diaVenta <= diaActual) or (fechaVenta[1] == fechaMesAnterior[1] and diaVenta >= diaActual):
          print(ventas)
  elif opc=="2":
    diaActual = fechaActual.day # int(fechaActual[0])
    for ventas in listaRegistroVenta:
      fechaVenta=ventas[0] #.split("/")
      diaVenta = fechaVenta.day # int(fechaVenta[0])
      if (fechaActual.year == fechaVenta.year and fechaActual.month == fechaVenta.month) and diaVenta <= diaActual: #(fechaActual[2]==fechaVenta[2] and fechaActual[1]==fechaVenta[1]) and (diaVenta<=diaActual):
          print(ventas)
  return

def bisiesto(anio):
  if (anio%4 == 0 and anio%100 != 0) or anio%400 == 0:
    return True
  else:
    return False

# def date2str(d):
#   return d.strftime('%d/%m/%Y')

# def date2list(d):
#   return d.strftime('%d/%m/%Y').split('/')

# def hour2str(h):
#   return h.strftime('%H:%M:%S')

def ventasAnio(opc):
  fechaActual = getDate()
  ventas = False
  if opc == 1:
    d = 366 if bisiesto(fechaActual.year) and fechaActual.month > 2 else 365
    fechaAnioAnterior = fechaActual - datetime.timedelta(days=d)
    for venta in listaRegistroVenta:
      if fechaAnioAnterior <= venta[0] <= fechaActual:
        ventas = True
        print(venta)
  elif opc == 2:
    fechaInicial = datetime.date(fechaActual.year, 1, 1)
    for venta in listaRegistroVenta:
      if fechaInicial <= venta[0] <= fechaActual:
        ventas = True
        print(venta)
  if not ventas:
    print('No hay ventas para mostrar...')
  return

def ventasPersonalizadas(inicio, fin):
  for venta in listaRegistroVenta:
    if inicio <= venta[0] <= fin:
      print(venta)
  return

# registraVentas()
# ventasAnio('2')
# ventaMes('1')
# reporteVentas()

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
  return

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
  return

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
  return
