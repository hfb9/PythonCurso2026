#│-▀▄■▄■▄▀-├─────────────────────────────────────────────────┤-▀▄■▄■▄▀-│
#│  ▀▄▀▄▀  │ Alumno: Hernán Biglieri | 2026 2do cuatrimestre │  ▀▄┴▄▀  │
#│─ ▀ ─ ▀ ─├───────────────────────────────────┤ v.26.10.09b ┤-▄▼\▀/▼▄-│

#___Inclusiones___ __________________________________________________

import os



#___Provisorios___ __________________________________________________

#_Provisorio, para etapa desarrollo, revisando_
def func_limpiaPantalla():
	os.system("cls" if os.name == "nt" else "clear")
#}
#Esto busca 'datos.txt' en la misma carpeta que el '.py'.
from pathlib import Path
import json
BASE = Path(__file__).resolve().parent
#
def archivo_save(archivo, datos):
	with open(archivo, 'w', encoding='utf-8') as f:
		json.dump(datos, f, ensure_ascii=False, indent=2)
	#}
	#[!] Falta que verifique si guardó bien.
#}
def archivo_load(archivo):
	archivo = Path(archivo)
	#print('archivo: '+str(archivo))
	if not archivo.exists() or archivo.stat().st_size == 0:
		#if not archivo.exists(): motivo = 'no existe'
		#elif archivo.stat().st_size == 0: motivo = 'está vacío'
		return None
	#}
	with open(archivo, 'r', encoding='utf-8') as f:
		return json.load(f)
	#}
#}



#___Configuración___ __________________________________________________

tablaAnchoCol_gd = 40
tablaAnchoCol_md = 16
tablaAnchoCol_ch = 10
caracteresAlphanumExtra = ' _.,@'
ARCHIVO_NOMBRE = 'datos.txt'



#___Constantes Globales___ __________________________________________________

#_Color y estilo_
#•Comun
COLOR_PREFIJO = "\033["
COLOR_SUFIJO =  "m"
COLOR_RESET =   COLOR_PREFIJO+"0"+COLOR_SUFIJO
#•Simples
BLANCO = '37'
ROJO =  "31"
CIAN =  "36"
#•RGB
COLOR_RGB_PREFIJO   = '38;2;'
COLOR_RGB_FONDO_PREFIJO  = '48;2;'
#_
COLOR_RGB_YELLOW_1  = '255;255;0'
COLOR_RGB_YELLOW_2  = '255;255;40'
COLOR_RGB_RED_1     = '255;0;0'
COLOR_RGB_RED_2     = '255;140;140'
COLOR_RGB_MAGENTA_1 = '255;0;255'
COLOR_RGB_MAGENTA_2 = '255;140;255'
COLOR_RGB_CIAN_1		= '0;255;255'
COLOR_RGB_CIAN_2		= '200;255;255'
COLOR_RGB_CIAN_3		= '130;180;200'
COLOR_RGB_GREEN_1		= '100;255;100'
COLOR_RGB_ORANGE_1  = '255;165;0'
COLOR_RGB_ORANGE_2  = '255;200;40'
COLOR_RGB_BLUE_1    = '100;100;255'
COLOR_RGB_GREY_1    = '100;100;100' #Para Notas.
COLOR_RGB_GREY_2    = '50;50;50'
COLOR_RGB_BLACK_1   = '0;0;0'
COLOR_RGB_WHITE_1   = '255;255;255'
#•Estilo
BOLD								= '1;'
UNDERLINE						= '4;'
INVERT							= '7;'
NORMAL							= '0;'

#___
#_Strings varios_
#PROMPT_INV = (
#	(COLOR_PREFIJO +        COLOR_RGB_FONDO_PREFIJO + COLOR_RGB_YELLOW_1 + COLOR_SUFIJO) +
#	(COLOR_PREFIJO + BOLD + COLOR_RGB_PREFIJO + COLOR_RGB_GREY_1 + COLOR_SUFIJO) +
#	'>' +
#	COLOR_RESET
#)
PROMPT = (
	(COLOR_PREFIJO + BOLD + COLOR_RGB_PREFIJO + COLOR_RGB_YELLOW_1 + COLOR_SUFIJO) +
	'>' +
	COLOR_RESET
)
#[Uso]: f"{COLOR_PREFIJO}{estilo}{COLOR_RGB_PREFIJO}{codigoColor}{COLOR_SUFIJO}{texto}{COLOR_RESET}"



#___Funciones___ __________________________________________________

def func_header():
	texto = 'Alumno: Hernán Biglieri | 2026 2do cuatrimestre'
		#•Opcion (a)
		#ancho = len(texto)
		#cuadro = (
		#	f'┌{'─'*(ancho+2)}┐\n'
		#	f'│ {texto} |\n'
		#	f'└{'─'*(ancho+2)}┘'
		#)
		#f'| {'Alumno: Hernán Biglieri | 2026 2do cuatrimestre':<{ancho-4}} |\n'
		#print(func_color_rgb(cuadro,COLOR_RGB_GREY_1,None))
	#•Opcion (b)
	textoColor = (
		COLOR_PREFIJO +		 COLOR_RGB_PREFIJO				+ COLOR_RGB_BLACK_1 + COLOR_SUFIJO + 
		COLOR_PREFIJO +			COLOR_RGB_FONDO_PREFIJO	+ COLOR_RGB_CIAN_3	+ COLOR_SUFIJO + 
		' ' + texto + ' ' + COLOR_RESET
	)
	print(textoColor)
#}

def func_color_rgb( texto, codigoColor=None, estilo=None ) :
	#[Invocación]
	#	[Ej] print(func_color_rgb("texto", '255;255;0', 1))
	#_/
	if codigoColor is None:
		codigoColor = '255;255;255' #BLANCO
	if estilo is not None :
		estilo = str(estilo) + ';'
	else :
		estilo = ''
	#}
	codigoColor = str(codigoColor)
	#Visualización de codigos: print( f"| {COLOR_PREFIJO} | {estilo} | {COLOR_RGB_PREFIJO} | {codigoColor} | {COLOR_SUFIJO} | {texto} | {COLOR_RESET} | " )
	return f"{COLOR_PREFIJO}{estilo}{COLOR_RGB_PREFIJO}{codigoColor}{COLOR_SUFIJO}{texto}{COLOR_RESET}"
#}

def func_detieneHastaPulsarEnter():
	#Solo detiene hasta pulsar [Enter].
	input('\n'+ func_color_rgb(str_mensaje_detieneHastaEnterVaAMenu,COLOR_RGB_GREY_1,None))	
#}

def func_imprimeTituloOpcionActual( k ):
	#k: menu key; v: menu value
	#_/
	v = menu.get(k)
	print('\n'+'______________________________\n'+'Opción \''+func_color_rgb(k+'. '+v,None,1)+'\'')
#}

def func_imprimeMenu( menu ):
	ancho = 30
	print('_'*ancho + '\n' + func_color_rgb('Opciones:',None,1))
	for k, v in menu.items():
		print(k+'. '+v,end='\n')
	#}
	print('¯'*ancho)
#}

#_

def inicializa_Lista():
	return []
#}

def func_imprime_tablaProductos_header():
	texto = (
		#[z]func_color_rgb('(↓ or: posición original)',COLOR_RGB_GREY_1,None)+'\n'+
		f"{'or':<2} | {'Nombre':<{tablaAnchoCol_gd}} | {'Categoría':<{tablaAnchoCol_md}} | {'Precio ($)':<{tablaAnchoCol_ch}}"+
		'\n'+
		'-'*(2+(3*3)+(1*tablaAnchoCol_gd)+(1*tablaAnchoCol_md)+(1*tablaAnchoCol_ch))
	) 
	print(func_color_rgb(texto,COLOR_RGB_CIAN_2,None),end='')
	print()
#}
def func_imprime_tablaProductos_unRegistro(i,p):
	n = i + 1 #i: indiceEnQueGenero → n: i+1 para que muestre iniciando desde 1.
	texto = f'{n:>2} | {p[0]:<{tablaAnchoCol_gd}} | {p[1]:<{tablaAnchoCol_md}} | {p[2]:>{tablaAnchoCol_ch}}'
	print(func_color_rgb(texto,COLOR_RGB_CIAN_2,None))
#}
def func_imprime_tablaProductos():
	print()
	if len(Productos) <= 0:
		print(func_color_rgb(str_mensaje_ErrorListaSinProductos, COLOR_RGB_RED_2, None))
	else:
		print('» Lista de Productos:')
		func_imprime_tablaProductos_header()
		for i,p in enumerate(Productos):
			func_imprime_tablaProductos_unRegistro(i,p)
		#}
	#}
#}
def func_busqueda_imprime_tablaProductos_header():
	texto = (
		func_color_rgb('(↓ or: posición original)',COLOR_RGB_GREY_1,None)+'\n'+
		f"{'or':<2} | {'Nombre':<{tablaAnchoCol_gd}} | {'Categoría':<{tablaAnchoCol_md}} | {'Precio ($)':<{tablaAnchoCol_ch}}"
		'\n'+
		'-'*(2+(3*3)+(1*tablaAnchoCol_gd)+(1*tablaAnchoCol_md)+(1*tablaAnchoCol_ch))
	)
	print(func_color_rgb(texto,COLOR_RGB_CIAN_2,None),end='')
	print()
#}
def func_busqueda_imprime_tablaProductos_unRegistro(p):
	posicionEnOriginal =  p[0] + 1 #i: indiceEnQueGenero → n: i+1 para que muestre iniciando desde 1.
	texto = f'{posicionEnOriginal:>2} | {p[1]:<{tablaAnchoCol_gd}} | {p[2]:<{tablaAnchoCol_md}} | {p[3]:>{tablaAnchoCol_ch}}'
	print(func_color_rgb(texto,COLOR_RGB_CIAN_2,None))
#}

def func_ingresoYValidacion( tipo, nombreDeCampoACargar, comentario='') :
	#·while flag_repetirValidacion: #sin 'break' o 'continue'
	#·flag_ComandoNavegacion_aDevolver:
	# ·Ingreso:''       → flag_ComandoNavegacion_aDevolver:1	 → fuera de la función se puede usar para retroceder 1 niveles o ir a Menú;
	# ·Ingreso:'0'     	→ flag_ComandoNavegacion_aDevolver:0	 → fuera de la función se puede usar para retroceder 2 niveles o ir a Menú;
	# ·Ingreso:'-(etc)' → flag_ComandoNavegacion_aDevolver:-1 → fuera de la función se puede usar para evaluar si se paso un 'Comandos de navegacíon de menu' ('-list', etc), y si no, repetir pedido de ingreso.
	#_/
	nombreDeCampoACargar = func_color_rgb(nombreDeCampoACargar, COLOR_RGB_CIAN_1) #nombreDeCampoACargar = color(nombreDeCampoACargar, CIAN, BOLD)
	comentario = func_color_rgb(comentario, COLOR_RGB_GREY_1, None)
	flag_ComandoNavegacion_aDevolver = None
	while True : #←flag_repetirValidacion == True
		flag_repetirValidacion = False
		acum_error_validacion = []
		campoACargar = input(f'\nIngrese "{nombreDeCampoACargar}":\n{comentario}\n{PROMPT}')
		campoACargar = campoACargar.strip()
		#
		#•1) Captura 'Comandos de navegacíon de menu' ('': para volver atras; '-0': para volver a Menú; '-list': Para pre-visualizar lista; etc):
		if campoACargar == "" : #[~] if not s.strip(): #not comprueba si Falsy, strip() devuelve string, y el único String Falsy es "", de modo que es lo mismo
			if input(f'[?] ¿Seguro desea abandonar este proceso y volver atrás? {func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None)}: ') == 's' :
				flag_ComandoNavegacion_aDevolver = 1
				return [flag_ComandoNavegacion_aDevolver, None]
			else :
				#[z]acum_error_validacion.append('·Ingreso inválido: Dato vacío.')
				flag_repetirValidacion = True
			#}
		#}
		elif campoACargar == "-0":
			if input(f'[?] ¿Seguro desea abandonar este proceso y volver a Menú? {func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None)}: ') == 's' :
				flag_ComandoNavegacion_aDevolver = 0
				return [flag_ComandoNavegacion_aDevolver, None]
			else :
				#[z]acum_error_validacion.append('·Ingreso inválido: Dato vacío.')
				flag_repetirValidacion = True
			#}
		#}
		#•2) Validaciones según tipo de dato:
		if not flag_repetirValidacion :
			match( tipo ):
				case 'int':
					if not campoACargar.isdigit(): #Si es decimal también devolverá que no es digito.
						acum_error_validacion.append( str_mensaje_ErrorIngresoNumerico )
						flag_repetirValidacion = True
				case 'alphanum':
					#•Detecta si se pasó palabra clave con prefijno '-' para uso como 'Comandos de navegacíon de menu' ([Ej] '-list').
					if campoACargar[:1]=='-' :
						campoACargar = campoACargar[1:] #Limpia string quitandole 1er '-'
						if campoACargar == '':
							acum_error_validacion.append('·Ingreso inválido: \'-\'.') #No admite que solo sea '-' ya que luego de filtrado quedaría en '' y sería String vacío.
							flag_repetirValidacion = True
						else:
							flag_ComandoNavegacion_aDevolver = -1 #Devuelve parametro para avisar que el texto debe evaluarse como 'Comandos de navegacíon de menu' y no como dato o contenido.
						#}
					#}
					#•Revisa que el texto: si vino con prefijo '-' haya sido limpiado, o que ya haya venido limpio (sin prefijo).
					if not flag_repetirValidacion:
						#[Global] caracteresAlphanumExtra = ' _.,@'
						#Condiciones:
						#	·a) Es Alfanumerico pero admitiendo algunos caracteres extra.
						#	·b) Además 1er caracter debe ser Alfanumerico estricto, o bien '-' que uso como caracter especial para pasar 'Comandos de navegacíon de menu' ('-0', '-list', etc).
						if not(
							all(c.isalnum() or c in caracteresAlphanumExtra for c in campoACargar)
							and (campoACargar[:1].isalnum() or campoACargar[:1]=='-')
						):
							acum_error_validacion.append( str_mensaje_ErrorIngresoAlfanumerico )
							flag_repetirValidacion = True
						#}					
				case '_':
					print('[x] Error: func_ingresoYValidacion(): Tipo no admitido')	
			#}
		#}
		#•3)
		if not flag_repetirValidacion : #repite if con misma variable, porque que dentro de bloque de if previo puede cambiar/actualizarse el valor de esta.
			return [flag_ComandoNavegacion_aDevolver, campoACargar]
		#•4) Muestra errores y repite bucle.
		#[~]else: #flag_repetirValidacion = algo
		if len(acum_error_validacion) != 0 :
			print(func_color_rgb('[x] Error:', COLOR_RGB_RED_1, BOLD),end=' ') #Anula '\n' final (default) para que 1er Error salga en misma línea (cuando existe solo 1 queda más prolijo).
			for cadaError in acum_error_validacion: print(cadaError)
			print('Vuelva a intentar')
		#}
		#Si no hay mensaje, solo repite bucle (sería casos en que ingresé '' o '-0' y al pedir confirmación cancelé con !='s').
	#}
#}

def func_comparacion_2Textos_siExacto_caseInsensitive( texto1, texto2 ):
	flag_coinciden = texto1.strip().lower() == texto2.strip().lower()
	return flag_coinciden
#}
def func_comparacion_2Textos_siIncluido_caseInsensitive( texto1, texto2 ):
	flag_coinciden = texto1.strip().lower() in texto2.strip().lower()
	return flag_coinciden
#}
def func_busqueda_siExacto_caseInsensitive( texto, lista ):
	#[Parametros]
	# ·texto: String a buscar.
	# ·lista: Lista donde buscar.
	#_
	#Itera cada registro de 'lista', cada uno corresponde a un Producto con sus propiedades Nombre, Categoría, Precio,
	#en cada iteración, compara el 'texto' ingresado con la propiedad o campo 'Nombre', si hay coincidencia del texto completo, lo agrega a una Lista de resultado que devolverá.
	#(Case-Insensitive)
	#agrega registro entero, con su campo Nombre pero tambien sus otros 2 (categoria y precio).
	#[indice] Lo que no tendrá será nro ya que aqui se pierde consistencia con los indices originales.
	#_/
	lista_provisoria = [] #Guardará indice original del registro en la Lista Productos, y luego los otros campos (tendrá 1 campo mas que la Lista Productos).
	for indice,producto in enumerate(lista):
		if func_comparacion_2Textos_siExacto_caseInsensitive(texto, producto[KEY_NOMBRE]):
			registro_provisorio = [indice] #indice de registro en su Lista original (Productos)
			registro_provisorio.extend(producto)
			#[Notas] registro_provisorio = [indice, /nombre/,/categoria/,/precio/]
			lista_provisoria.append(registro_provisorio)
		#}
	#}
	return lista_provisoria
#}
def func_busqueda_siIncluido_caseInsensitive( texto, lista ):
	#[Parametros]
	# ·texto: String a buscar.
	# ·lista: Lista donde buscar.
	#_
	#Itera cada registro de 'lista', cada uno corresponde a un Producto con sus propiedades Nombre, Categoría, Precio,
	#en cada iteración, compara el 'texto' ingresado con la propiedad o campo 'Nombre', si hay coincidencia "con alguna parte" del string (no exacta), lo agrega a una Lista de resultado que devolverá.
	#(Case-Insensitive)
	#agrega entero, con su campo Nombre pero tambien sus otros 2 (categoria y precio).
	#[!] Lo que no tendrá será nro ya que aqui se pierde consistencia con los indices originales.
	#_/
	lista_provisoria = []
	for indice,producto in enumerate(lista):
		if func_comparacion_2Textos_siIncluido_caseInsensitive(texto, producto[KEY_NOMBRE]):
			registro_provisorio = [indice] #indice de registro en su Lista original (Productos)
			registro_provisorio.extend(producto)
			#[Notas] registro_provisorio = [indice, /nombre/,/categoria/,/precio/]
			lista_provisoria.append(registro_provisorio)
		#}
	#}
	return lista_provisoria
#}



#___Inicializacion___ __________________________________________________

#_Variables Globales_
#String para comentarios repetitivos en pantalla:
str_mensaje_ErrorIngresoNumerico         = '·Ingreso inválido: Dato debe ser '+func_color_rgb('Número Entero', None, BOLD)+'.'
str_mensaje_ErrorIngresoAlfanumerico     = '·Ingreso inválido: Dato debe ser '+func_color_rgb('Alfanumérico', None, BOLD) + ' ' + func_color_rgb('(A-Za-z0-9'+caracteresAlphanumExtra+')', COLOR_RGB_GREY_1, None)+'.'
str_mensaje_ErrorListaSinProductos       = '[!] No hay productos aún'
#
str_comentario_separador                 = '\n'
str_comentario_bullet                    = '└►'
str_comentario_vacio_paraAtras           = str_comentario_bullet + '[Enter](vacío): para volver Atrás'
str_comentario_vacio_paraAtrasOMenu      = str_comentario_bullet + '[Enter](vacío) o "-0": para volver Atrás/Menú'
str_comentario_guionlist_paraPreverLista = str_comentario_bullet + '"-list": para previsualizar Lista completa'
str_comentario_guion0_paraMenuRaiz       = str_comentario_bullet + '"-0": para volver a Menú'
#
str_mensaje_detieneHastaEnterVaAMenu      = str_comentario_bullet + '[Enter] para volver a Menú'
str_mensaje_detieneHastaEnterVaAProseguir = str_comentario_bullet + '[Enter] para seguir'
#[Uso]
# str_comentario_vacio_paraAtrasOMenu
# str_comentario_vacio_paraAtrasOMenu + str_comentario_separador + str_comentario_guionlist_paraPreverLista
# str_comentario_vacio_paraAtras  + str_comentario_separador + str_comentario_guion0_paraMenuRaiz
#/


#_Definiciones_
menu = {
	'1': 'Agregar producto',
	'2': 'Mostrar productos',
	'3': 'Buscar producto',
	'4': 'Eliminar producto',
	'5': 'Cargar '+func_color_rgb('desde archivo',COLOR_RGB_GREY_1,None),
	'6': 'Guardar '+func_color_rgb('en archivo',COLOR_RGB_GREY_1,None),
	'7': 'Vaciar '+func_color_rgb('Lista de Productos',COLOR_RGB_GREY_1,None),
	'0': 'Salir'
}

#	[Matriz] Principal
# Productos[][]
#	Lista de la cual 
# 	Cada Registro será un producto
# 	Formado por una Sublista
#		Con los Campos: 0:Nombre; 1:Categoria; 2:Precio
#_
#[Estructura]
# Productos = [
#		['nombre1','categoria1',10],
#		['nombre2','categoria2',20],
#		…
#	]
#_/

Productos = inicializa_Lista()

KEY_NOMBRE = 0
KEY_CATEGORIA = 1
KEY_PRECIO = 2

#_Calculos_
ARCHIVO_CON_RUTA = BASE / ARCHIVO_NOMBRE
#print('ARCHIVO_CON_RUTA: '+str(ARCHIVO_CON_RUTA))



#___Ejecucion___ __________________________________________________

#[z]func_limpiaPantalla()

#_
#┌W0
flag_terminarEjecucion = False
while not flag_terminarEjecucion:
	#[#Anchor_W0]
	func_limpiaPantalla()
	func_header() #Rótulo (autor, fecha, etc)
	func_imprimeMenu( menu )
	
	menu_opcion_elegida = input('Elija una opción: ')
	menu_opcion_elegida = menu_opcion_elegida.strip()
	match(menu_opcion_elegida):
		case '1': #'1. Agregar producto'
			func_limpiaPantalla()
			#___
			#┌W0_1
			flag_va1nivelAtras = False
			flag_va2nivelesAtras = False
			#[Aca ya no pq el while menu no lo quiero saltar] flag_vaANivelRaiz = False
			while True: #[~] 'do while'
				#[#Anchor_W0_1]
				func_imprimeTituloOpcionActual('1')
				alta_provisorio = [None,None,None] #SubLista - cada Producto antes de cargarse a la Matriz definitiva. | Campos: [0] Nombre; [1] Categoría; [2] Precio.
				#•Ingreso Nombre
				#┌W0_1_1
				flag_va1nivelAtras = False
				flag_va2nivelesAtras = False
				flag_vaANivelRaiz = False
				while True: #[~] 'do while'
					#[#Anchor_W0_1_1]
					flag_ComandoNavegacion, alta_provisorio[KEY_NOMBRE] = func_ingresoYValidacion( 'alphanum', 'Nombre del Producto', str_comentario_vacio_paraAtrasOMenu ) #recibe Lista con 2 elementos.
					if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0_3]' (2 niveles atrás)
						#Directo retrocede 2 niveles - Porque aquí no sirve ir atrás solo 1 nivel porque allí se repetíria solicitud de ingreso de mismo campo actual.
						flag_va2nivelesAtras = True;
						break
					elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
						#Repite pedido de ingreso nombre producto.
						flag_vaANivelRaiz = True
						break
					#}
					#_
					#[±]««[ proceso ]»»
					#•Chequea string que comienza con '-' para 'Comandos de navegacíon de menu'.
					elif flag_ComandoNavegacion == -1:
						#aca no se espera 'Comandos de navegacíon de menu'
						print(func_color_rgb('[x] Error:', COLOR_RGB_RED_1, BOLD),end=' ')
						print( str_mensaje_ErrorIngresoAlfanumerico )
						continue #Error y vuelve a pedir Nombre.
					#}
					#si todas los validaciones previas ok: acepta ingreso y sigue adelante
					#•Valida que el registro no exista (Búsqueda exacta)
					if func_busqueda_siExacto_caseInsensitive( alta_provisorio[KEY_NOMBRE], Productos ):
						print(func_color_rgb('[!] No permitido:', COLOR_RGB_RED_1, BOLD)+' Ese producto ya figura en la lista.')
						print('Vuelva a intentar')
						continue #Repite pedido de nro de orden a eliminar
					#else:
					#si todas los validaciones previas ok: acepta ingreso y sigue adelante
					break #sigue adelante
				#}
				if flag_va1nivelAtras: continue
				if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
				if flag_vaANivelRaiz: break
				#└/W0_1_1
				#
				#•Ingreso Categoría
				flag_ComandoNavegacion, alta_provisorio[KEY_CATEGORIA] = func_ingresoYValidacion( 'alphanum', 'Categoría del Producto', str_comentario_vacio_paraAtras + ' (Nombre)' + str_comentario_separador + str_comentario_guion0_paraMenuRaiz )
				if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0_1]' (repite mismo while, Repite pedido de ingreso nombre producto)
					func_limpiaPantalla()
					continue 
				elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
					flag_vaANivelRaiz = True
					break
				#}
				#•Ingreso Precio
				flag_ComandoNavegacion, alta_provisorio[KEY_PRECIO] = func_ingresoYValidacion( 'int', 'Precio del Producto', str_comentario_vacio_paraAtras + ' (Nombre)' + str_comentario_separador + str_comentario_guion0_paraMenuRaiz )
				if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0_1]' (repite mismo while, Repite pedido de ingreso nombre producto)
					func_limpiaPantalla()
					continue 
				elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
					flag_vaANivelRaiz = True
					break
				#}
				#_
				#•Si no hay errores, procesa/limpia los campos ingresados.
				#««[ proceso ]»»
				#Ya aplicados.strip()
				alta_provisorio[KEY_NOMBRE] = alta_provisorio[KEY_NOMBRE].capitalize()
				alta_provisorio[KEY_CATEGORIA] = alta_provisorio[KEY_CATEGORIA].capitalize()
				#•Los carga en Lista definitiva
				#•Crea un registro nuevo, y lo completa a la vez
				Productos.append(alta_provisorio)
				indiceEnQueGenero = len(Productos) - 1
				print(f'\n» {func_color_rgb('[v]',COLOR_RGB_GREEN_1,BOLD)} Se agregó:') #[x]print(f'\nSe agregó: {alta_provisorio}')
				func_imprime_tablaProductos_header()
				func_imprime_tablaProductos_unRegistro(indiceEnQueGenero,Productos[indiceEnQueGenero])				
			#}
			if flag_va1nivelAtras: continue
			if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
			#[Aca ya no pq el while menu no lo quiero saltar] if flag_vaANivelRaiz: break
			#└/W0_1
		#_
		case '2': #'2. Mostrar productos'
			func_limpiaPantalla()
			func_imprimeTituloOpcionActual('2')
			func_imprime_tablaProductos()
			func_detieneHastaPulsarEnter()
		#_
		case '3': #'3. Buscar producto'
			func_limpiaPantalla()
			if len(Productos) <= 0:
				func_imprimeTituloOpcionActual('3')
				print()
				print(func_color_rgb(str_mensaje_ErrorListaSinProductos, COLOR_RGB_RED_2, None))
				func_detieneHastaPulsarEnter()
			#}
			else:
				#┌W0_2
				flag_va1nivelAtras = False
				flag_va2nivelesAtras = False
				#[Aca ya no pq el while menu no lo quiero saltar] flag_vaANivelRaiz = False
				while True: #[~] 'do while'
					#[#Anchor_W0_2]	
					func_imprimeTituloOpcionActual('3')
					#•Ingreso Nombre
					flag_ComandoNavegacion, busqueda_nombreABuscar = func_ingresoYValidacion( 'alphanum', 'Nombre del Producto', str_comentario_vacio_paraAtrasOMenu )
					if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0]' (1 nivel atrás)(Menú)
						flag_va1nivelAtras = True
						break
					elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
						flag_vaANivelRaiz = True
						break
					#}
					#•Chequea string que comienza con '-' para 'Comandos de navegacíon de menu'.
					elif flag_ComandoNavegacion == -1:
						#aca no se espera 'Comandos de navegacíon de menu'
						print(func_color_rgb('[x] Error:', COLOR_RGB_RED_1, BOLD),end=' ')
						print( str_mensaje_ErrorIngresoAlfanumerico )
						continue #Error y vuelve a pedir Nombre.
					#}
					#si todas los validaciones previas ok: acepta ingreso y sigue adelante
					#_
					#•Si no hay errores, aplica la búsqueda.
					#««[ proceso ]»»
					#Ya aplicados en el Alta: .strip(), capitalize(), etc.
					#(opcional visualizacion)
					func_limpiaPantalla()
					func_imprimeTituloOpcionActual('3')
					#
					print('\n'+'» Lista de Resultados:')
					print( func_color_rgb('Término de Búsqueda: "',COLOR_RGB_GREY_1,None) + func_color_rgb(busqueda_nombreABuscar,COLOR_RGB_ORANGE_2,BOLD) + func_color_rgb('"',COLOR_RGB_GREY_1,None) )
					#•Búsqueda Exacta
					ResultadosDeBusqueda_exacta = func_busqueda_siExacto_caseInsensitive(busqueda_nombreABuscar, Productos) #func_busca(busqueda_nombreABuscar, listaDondeBuscar) #busqueda laxa, da coincidencia si el termino buscado es parte del producto existente.
					print('\n'+func_color_rgb('a)',None,1)+' Búsqueda Exacta '+func_color_rgb('(si Texto es idéntico al Nombre completo de algún producto)(Case-Insensitive)',COLOR_RGB_GREY_1,None)+':')
					if len(ResultadosDeBusqueda_exacta) > 0:
						#•Muestra resultados
						func_busqueda_imprime_tablaProductos_header()
						for registroProv in ResultadosDeBusqueda_exacta:
							#[Notas][!] 'registroProv' tendrá 1 campo mas que Lista 'Productos', y registroProv[0] en esta Lista el registro 0 agrega un id que guarda la posición en la Lista original.
							func_busqueda_imprime_tablaProductos_unRegistro(registroProv)
						#}
					else:
						#•Muestra no hay resultados
						print(' '+func_color_rgb(f'[!] No se encontraron productos que coincidan \'exactamente\' con \033[1m"{busqueda_nombreABuscar}"\033[0m',COLOR_RGB_RED_2,None))
					#}
					#•Búsqueda Laxa
					ResultadosDeBusqueda_laxa = func_busqueda_siIncluido_caseInsensitive(busqueda_nombreABuscar, Productos) #func_busca(busqueda_nombreABuscar, listaDondeBuscar) #busqueda exacta, compara el texto ingresado completo con el nombre completo del producto existente.
					print('\n'+func_color_rgb('b)',None,1)+' Búsqueda Laxa '+func_color_rgb('(si Texto existe como \'parte de\' algún Nombre de producto)(Case-Insensitive)',COLOR_RGB_GREY_1,None)+':')
					if len(ResultadosDeBusqueda_laxa) > 0:
						#•Muestra resultados							
						func_busqueda_imprime_tablaProductos_header()
						for registroProv in ResultadosDeBusqueda_laxa:
							func_busqueda_imprime_tablaProductos_unRegistro(registroProv)
						#}
					else:
						#•Muestra no hay resultados
						print(' '+func_color_rgb(f'[!] No se encontraron productos que coincidan \'parcialmente\' con \033[1m"{busqueda_nombreABuscar}"\033[0m',COLOR_RGB_RED_2,None))
					#}
				#}
				if flag_va1nivelAtras: continue
				if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
				#[Aca ya no pq el while menu no lo quiero saltar] if flag_vaANivelRaiz: break
				#└/W0_2
			#}
		#_
		case '4': #'4. Eliminar producto'
			func_limpiaPantalla()
			if len(Productos) <= 0:
				func_imprimeTituloOpcionActual('4')
				print()
				print(func_color_rgb(str_mensaje_ErrorListaSinProductos, COLOR_RGB_RED_2, None))
				func_detieneHastaPulsarEnter()
			#}
			else:
				#┌W0_3
				flag_va1nivelAtras = False
				flag_va2nivelesAtras = False
				#[Aca ya no pq el while menu no lo quiero saltar] flag_vaANivelRaiz = False
				while True: #[~] 'do while'
					#[#Anchor_W0_3]
					func_limpiaPantalla()
					#┌W0_3_1
					flag_va1nivelAtras = False
					flag_va2nivelesAtras = False
					flag_vaANivelRaiz = False
					while True: #[~] 'do while'
						#[#Anchor_W0_3_1]
						func_imprimeTituloOpcionActual('4')
						#•Pide Nombre a Buscar para Borrar
						flag_ComandoNavegacion, busqueda_nombreABuscar = func_ingresoYValidacion( 'alphanum', 'Nombre del Producto', str_comentario_vacio_paraAtrasOMenu + str_comentario_separador + str_comentario_guionlist_paraPreverLista )
						#Directo retrocede 2 niveles
						if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0_3]' (2 niveles atrás)
							flag_va2nivelesAtras = True
							break
						elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
							#Repite pedido de ingreso nombre producto.
							flag_vaANivelRaiz = True
							break
						#[±]««[ proceso ]»»
						#•Chequea más 'Comandos de navegacíon de menu', srings que fueron ingresados como '-algo', se procesan delovliendo flag_ComandoNavegacion = -1, para avisar que se debe evaluar fuera, y el string lo devuelve sih '-'.
						elif flag_ComandoNavegacion == -1:
							if busqueda_nombreABuscar == 'list': #funcion validadora 'func_ingresoYValidacion()' recibe '-list' devuelve aviso en parametro de flag con valor -1, y limpia el '-' del string devolviendo este limpio en el parámetro de texto. ([Ej] si se ingresa de entrada 'list' sin '-', no interpreta este flag y lo pasa de como string normal saltando este bloque).
								func_imprime_tablaProductos()
								continue #muestra Lista y vuelve a pedir Nombre.
							#}
							#Si se paso algún '-algo' y no figura aquí para evaluar, emite error porque no es un comando esperado.
							print(func_color_rgb('[x] Error:', COLOR_RGB_RED_1, BOLD),end=' ')
							print( str_mensaje_ErrorIngresoAlfanumerico )
							continue #Error y vuelve a pedir Nombre.
						#}
						#Si todas los validaciones previas ok: acepta ingreso y sigue adelante.
						#««[ proceso ]»»
						break
					#}
					if flag_va1nivelAtras: continue
					if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
					if flag_vaANivelRaiz: break
					#└W0_3_1
					#_
					#•Búsqueda Laxa:
					print('\n'+'» Lista de Resultados ('+func_color_rgb('Candidatos a Eliminar',None,BOLD)+'):')
					#┌W0_3_2
					flag_va1nivelAtras = False
					flag_va2nivelesAtras = False
					flag_vaANivelRaiz = False
					while True: #[~] 'do while'
						#[#Anchor_W0_3_2]
						#•Muestra Registros coincidentes con el Nombre ingresado:
						ResultadosDeBusqueda_laxa_paraEliminar = func_busqueda_siIncluido_caseInsensitive(busqueda_nombreABuscar, Productos) #func_busca(busqueda_nombreABuscar, listaDondeBuscar) #busqueda exacta, compara el texto ingresado completo con el nombre completo del producto existente.
						print( f'Productos coincidentes con: "'+func_color_rgb(busqueda_nombreABuscar,COLOR_RGB_ORANGE_2,BOLD)+'"'+ '\n\n'+
							func_color_rgb('(Búsqueda Laxa: si Texto existe como \'parte de\' algún Nombre de producto)(Case-Insensitive)',COLOR_RGB_GREY_1,None)
						)
						if len(ResultadosDeBusqueda_laxa_paraEliminar) <= 0:
							#•Muestra no hay resultados:
							print(' '+func_color_rgb(f'[!] No se encontraron productos que coincidan con \033[1m"{busqueda_nombreABuscar}"\033[0m',COLOR_RGB_RED_2,None))
							input('\n'+ func_color_rgb(str_mensaje_detieneHastaEnterVaAProseguir,COLOR_RGB_GREY_1,None))
							flag_va1nivelAtras = True
							break
						#}
						#_
						#•Hay posibles Eliminables:	#if len(ResultadosDeBusqueda_laxa_paraEliminar) > 0:
						func_busqueda_imprime_tablaProductos_header()
						for registroProv in ResultadosDeBusqueda_laxa_paraEliminar:
							func_busqueda_imprime_tablaProductos_unRegistro(registroProv)
						#}
						#•Pide Nro para Elegir cual de los Candidatos encontrados Eliminar:
						#┌W0_3_2_1
						flag_va1nivelAtras = False
						flag_va2nivelesAtras = False
						flag_vaANivelRaiz = False
						while True: #[~] 'do while'
							#[#Anchor_W0_3_2_1]
							print(f'\nConfirme el Registro a eliminar indicando su \'Nro de orden\':')
							flag_ComandoNavegacion, nroOrden = func_ingresoYValidacion( 'int', 'Nro de orden', str_comentario_vacio_paraAtras + ' (Nombre)' + str_comentario_separador + str_comentario_guion0_paraMenuRaiz )
							if flag_ComandoNavegacion == 1: #va a '[#Anchor_W0_3]' (2 niveles atrás)
								#Directo retrocede 2 niveles - Porque aquí no sirve ir atrás solo 1 nivel porque allí Repite impresion de Lista y Solicitud de Nro de orden (registro) a eliminar.
								flag_va2nivelesAtras = True
								break
							elif flag_ComandoNavegacion == 0: #va a '[#Anchor_W0]' (nivel raiz (Menú))
								#Repite pedido de ingreso nombre producto.
								flag_vaANivelRaiz = True
								break
							#}
							#««[ proceso ]»»
							#•Valida si el registro existe
							lista_indice_cadaRegistro = [ int(n[0]) for n in ResultadosDeBusqueda_laxa_paraEliminar ] #Arma Lista con el 1er campo de cada registro de la busqueda, osea, con los nros de orden de los registros coincidentes. se usaran para validar si al elegir uno figura o se eligió uno que no corresponde.
							indice_aEliminar = int(nroOrden) - 1
							if indice_aEliminar not in lista_indice_cadaRegistro: #ambas int
								print(func_color_rgb('[!]', COLOR_RGB_RED_1, BOLD)+' Ese número de registro no corresponde con los pre-seleccionados.')
								print('Vuelva a intentar')
								continue #Repite Solicitud de Nro de orden (registro) a eliminar.
							#else:
							break #Sigue adelante.
						#}
						if flag_va1nivelAtras: continue
						if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
						if flag_vaANivelRaiz: break
						#}
						#└W0_3_2_1
						#_
						#•Elimina:
						registroProv = Productos[indice_aEliminar]
						Productos.pop(indice_aEliminar)
						func_limpiaPantalla()
						func_imprimeTituloOpcionActual('4')
						print(f"\n» {func_color_rgb('[v]',COLOR_RGB_GREEN_1,BOLD)} Se eliminó:")
						func_imprime_tablaProductos_header()
						func_imprime_tablaProductos_unRegistro(indice_aEliminar,registroProv)
						print('\n'+'Lista actualizada:')						
					#}
					if flag_va1nivelAtras: continue
					if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
					if flag_vaANivelRaiz: break
					#└W0_3_2
				#}
				if flag_va1nivelAtras: continue
				if flag_va2nivelesAtras: flag_va2nivelesAtras = False; break
				#[Aca ya no pq el while menu no lo quiero saltar] if flag_vaANivelRaiz: break
				#└/W0_3
			#}
		#_
		case '5': #'5. Cargar' (Load)
			func_imprimeTituloOpcionActual('5')
			print()
			if input('[?] ¿Seguro desea Cargar Datos desde Archivo? ' + func_color_rgb('(se sobreescribirán los Datos actuales)',COLOR_RGB_GREY_1,None) + ' ' + func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None) + ': ').strip() == 's' :
				DatosALeer = archivo_load( ARCHIVO_CON_RUTA )
				#print(str(DatosALeer))
				if DatosALeer is None:
					print(func_color_rgb(f'[x] Lectura no posible',COLOR_RGB_RED_2,None) + ' El Archivo no existe, cree uno desde "Guardar" 1ro')
				else:
					print(func_color_rgb(f'[v] Lectura ok',COLOR_RGB_BLUE_1,None))
					Productos = DatosALeer
				#}
			else:
				print(func_color_rgb(f'[x] Lectura cancelada',COLOR_RGB_RED_2,None))
			#}
			func_detieneHastaPulsarEnter()
		#_
		case '6': #'6. Guardar' (Save)
			func_imprimeTituloOpcionActual('6')
			print()
			if input('[?] ¿Seguro desea Guardar Datos actuales a Archivo? ' + func_color_rgb('(se sobreescribirá el Archivo previo)',COLOR_RGB_GREY_1,None) + ' ' + func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None) + ': ') == 's' :
				archivo_save( ARCHIVO_CON_RUTA, Productos )
				print(func_color_rgb(f'[v] Guardado ok',COLOR_RGB_BLUE_1,None))
			else:
				print(func_color_rgb(f'[x] Guardado cancelado',COLOR_RGB_RED_2,None))
			#}
			func_detieneHastaPulsarEnter()
		#_
		case '7': #'7. Vaciar Lista'
			func_imprimeTituloOpcionActual('7')
			print()
			if input('[?] ¿Seguro desea Vaciar la Lista de Productos? ' + func_color_rgb('(se perderán los datos que no haya Guardado)',COLOR_RGB_GREY_1,None) + ' ' + func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None) + ': ') == 's' :
				Productos = inicializa_Lista()
				print(func_color_rgb(f'[v] Vaciado de Datos ok',COLOR_RGB_BLUE_1,None))
			else:
				print(func_color_rgb(f'[x] Vaciado de Datos cancelado',COLOR_RGB_RED_2,None))
			#}
			func_detieneHastaPulsarEnter()
		#_
		case '0': #'0. Salir'
			func_imprimeTituloOpcionActual('0')
			print()
			if input('[?] ¿Seguro desea Salir del programa? ' + func_color_rgb('(se perderán los datos que no haya Guardado)',COLOR_RGB_GREY_1,None) + ' ' + func_color_rgb('(s/n)',COLOR_RGB_GREY_1,None) + ': ') == 's' :
				#(mensaje se imprime fuera)
				flag_terminarEjecucion = True
				continue
			else:
				print(func_color_rgb(f'[x] Salir cancelado',COLOR_RGB_RED_2,None))
				func_detieneHastaPulsarEnter()
			#}
		#_
		case _:
			if menu_opcion_elegida != '':
				print('\n'+func_color_rgb('[x] Error:', COLOR_RGB_RED_1, BOLD),end=' ')
				print('·Opción invalida, vuelva a intentar.')
				func_detieneHastaPulsarEnter()
			#else: simplemente retoma bucle, sin mensaje de error
			#sigue, y retoma bucle
	#}
	#_
#} /while

#Salto extra para separar de Menú
#print('\n'+'____________________'+'\n')
print(func_color_rgb(f'[v] Ejecución Terminada',COLOR_RGB_BLUE_1,None))
exit()