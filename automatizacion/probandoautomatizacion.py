# -*- coding: utf-8 -*-
"""
Simulación de ingreso a Ventor usando Excel como "formulario".
Lee tu Excel (MATRIZ), toma columnas reales y las tipea en Excel
siguiendo FIELD_ORDER con TAB entre campos y avanza a la siguiente fila.

Requisitos (en PowerShell, con venv activado):
pip install pandas openpyxl pyautogui pygetwindow keyboard
"""

import time
import sys
import pandas as pd
import pyautogui as ag
import pygetwindow as gw
import keyboard

# ------------------- CONFIGURACIÓN -------------------

# 1) TU ARCHIVO Y HOJA
EXCEL_PATH  = r"D:\COSAS DEL TRABAJO\almacen-wong\1. STOCK ANTAPACCAY MENSUAL\2022\MACROINICIO2022.xlsm"
EXCEL_SHEET = "MATRIZ"

# 2) FILA DEL ENCABEZADO (0-based). En tu captura, la fila "FECHA|MES|DOC|..." es la sexta → 5
HEADER_ROW = 5   # si no calza, cambia este número

# 3) ORDEN DE CAMPOS QUE QUIERES TIPEAR (debe existir en el Excel tras leerlo)
#    Usa los nombres EXACTOS que aparecen en la fila de encabezados: FECHA, DOC, CLIENTE, ...
FIELD_ORDER = [
	"FECHA",
	"DOC",
	"CLIENTE",
	"EQUIPO",
	"O/T",
	"RESERVA",
	"COD_WONG",
	"COD_CONSIGNACION",
	"CANJE",
	"S",          # Usamos S como Cantidad (salida)
	"DESCRIP"
]

# 4) DESDE QUÉ FILA DE DATOS EMPIEZAS (en Excel, 1-based contando la fila del encabezado como 1).
#    Si tu primer dato útil está por la fila 15880 (como dijiste), pon eso aquí.
START_EXCEL_ROW = 15880

# 5) CUÁNTAS FILAS PROCESAR (None = todas desde START_EXCEL_ROW)
MAX_ROWS = 20  # pon un número pequeño para probar; luego puedes pasarlo a None

# 6) TITULO DE VENTANA PARA ENFOCAR EXCEL (cualquiera que contenga una de estas frases)
EXCEL_WINDOW_HINTS = ["Excel", "MACROINICIO2022", "Libro1"]
USE_AUTO_FOCUS = True
# 7) TIMINGS
TYPE_DELAY   = 0.05   # delay por tecla al tipear
ACTION_DELAY = 0.35   # delay entre acciones (TAB/ENTER/ARROWS)

# 8) TECLAS DE CONTROL
PAUSE_KEY = "f8"      # Pausar/Reanudar
ABORT_KEY = "esc"     # Abortar todo

# -----------------------------------------------------


def log(msg):
	print(time.strftime("[%H:%M:%S]"), msg)
	sys.stdout.flush()


def focus_excel_window():
	"""Enfoca la ventana de Excel (por hints en el título)."""
	candidates = []
	for w in gw.getAllWindows():
		title = (w.title or "").strip()
		for h in EXCEL_WINDOW_HINTS:
			if h.lower() in title.lower():
				candidates.append(w)
				break
	if not candidates:
		raise RuntimeError("No pude encontrar la ventana de Excel. Abre el archivo y déjalo visible.")
	win = candidates[0]
	if win.isMinimized:
		win.restore()
		time.sleep(0.5)
	win.activate()
	time.sleep(0.5)
	return win


def wait_unpaused():
	"""Permite pausar con F8 y abortar con ESC."""
	if keyboard.is_pressed(ABORT_KEY):
		raise KeyboardInterrupt("Abortado por el usuario (ESC).")
	if keyboard.is_pressed(PAUSE_KEY):
		log("Pausa (F8). Vuelve a presionar F8 para reanudar.")
		# esperar a que suelte F8
		while keyboard.is_pressed(PAUSE_KEY):
			time.sleep(0.2)
		# esperar a que vuelva a presionarla
		while not keyboard.is_pressed(PAUSE_KEY):
			if keyboard.is_pressed(ABORT_KEY):
				raise KeyboardInterrupt("Abortado por el usuario (ESC).")
			time.sleep(0.2)
		# soltar
		while keyboard.is_pressed(PAUSE_KEY):
			time.sleep(0.2)
		log("Reanudado.")


def safe_str(x):
	if x is None:
		return ""
	s = str(x)
	return "" if s.lower() == "nan" else s


def type_row_into_excel(row_values):
	"""
	Escribe los valores de una fila en Excel:
	- escribe valor
	- TAB al siguiente campo
	- al final de la fila: vuelve al primer campo y baja 1 fila
	"""
	n = len(row_values)
	for i, val in enumerate(row_values):
		wait_unpaused()
		ag.typewrite(safe_str(val), interval=TYPE_DELAY)
		time.sleep(ACTION_DELAY)
		if i < n - 1:
			ag.press("tab")  # siguiente celda
			time.sleep(ACTION_DELAY)

	# Terminado el último campo: volver a la primera columna y bajar una fila
	# Estrategia: ir a la izquierda (n-1) veces, luego flecha abajo.
	for _ in range(n - 1):
		ag.press("left")
		time.sleep(0.02)
	ag.press("down")
	time.sleep(ACTION_DELAY)


def main():
	# 1) Leer Excel con el encabezado correcto
	log(f"Leyendo Excel: {EXCEL_PATH} (hoja={EXCEL_SHEET}, header_row={HEADER_ROW})")
	df = pd.read_excel(
		EXCEL_PATH,
		sheet_name=EXCEL_SHEET,
		header=HEADER_ROW,
		dtype=str,
		engine="openpyxl"
	)

	# 2) Validar columnas
	missing = [c for c in FIELD_ORDER if c not in df.columns]
	if missing:
		raise ValueError(f"Faltan columnas en el Excel: {missing}\n"
						f"Columnas leídas: {list(df.columns)}")

	# 3) Recortar desde la fila indicada (Excel 1-based => pandas 0-based)
	start_idx = max(0, START_EXCEL_ROW - (HEADER_ROW + 1))  # ajusta índice real de pandas
	if start_idx >= len(df):
		raise ValueError(f"START_EXCEL_ROW apunta fuera del rango de datos. len(df)={len(df)}, start_idx={start_idx}")
	df = df.iloc[start_idx:].reset_index(drop=True)

	if MAX_ROWS is not None:
		df = df.iloc[:MAX_ROWS]

	log(f"Total filas a procesar: {len(df)}")
	log(f"Preview columnas: {FIELD_ORDER}")
	log("\n" + df[FIELD_ORDER].head(5).to_string(index=False))

	# 4) Enfocar Excel y pedir que pongas el cursor en la PRIMERA celda de destino (ej. A2)
	log("Enfocando Excel...")
	focus_excel_window()
	log("Coloca el cursor en la PRIMERA celda destino (correspondiente a FECHA) y no toques nada.")
	for s in range(3, 0, -1):
		log(f"Comenzando en {s}…")
		time.sleep(1)

	# 5) Tipear fila por fila
	for i, row in df.iterrows():
		wait_unpaused()
		values = [row.get(col, "") for col in FIELD_ORDER]
		log(f"Fila {i+1}/{len(df)}")
		try:
			type_row_into_excel(values)
		except KeyboardInterrupt:
			log("Abortado por el usuario.")
			break
		except Exception as e:
			log(f"Error en fila {i+1}: {e}")
			# decide si continuar o detener
			# break
			continue

	log("Proceso finalizado.")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		log(f"ERROR: {e}")
		sys.exit(1)
