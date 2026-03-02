import time
import os
import sys
import pandas as pd
import pyautogui as ag
import pygetwindow as gw
import keyboard

# ---------------- CONFIGURACIÓN ----------------
EXCEL_PATH = r"D:\COSAS DEL TRABAJO\almacen-wong\1. STOCK ANTAPACCAY MENSUAL\2022\MACROINICIO2022.xlsm"  # <<< AJUSTA AQUÍ
EXCEL_SHEET = "MATRIZ"                     # <<< AJUSTA AQUÍ (o None si es la primera)
START_ROW = 15880                             # Primera fila de datos (1-indexed, suele ser 2 si fila 1 es encabezado)
END_ROW = None                            # Hasta dónde (None = todas)
RDP_WINDOW_TITLES = [
	"VENTOR",               # <<< AJUSTA AQUÍ (pon una palabra única del título)
	"Remote Desktop",       # Alternativas por si cambia
	"Conexión a Escritorio remoto"
]

# Campos en el orden exacto en que se navegan con TAB en la GUI de Ventor:
FIELD_ORDER = [
	"Cliente",
	"RUC",
	"FechaEmision",
	"AlmacenOrigen",
	"AlmacenDestino",
	"Producto",
	"Cantidad",
	"Unidad",
	"Descripcion",
	"Placa",
	"Conductor",
	"Observaciones"
]  # <<< AJUSTA AQUÍ: debe coincidir con tus columnas y la GUI

# Teclas y tiempos
TYPE_DELAY = 0.02       # delay entre teclas al tipear
ACTION_DELAY = 0.20     # delay entre acciones (TAB/ENTER)
SAVE_KEY = "enter"      # tecla para guardar/siguiente pantalla (ajusta si es F5, etc.)
NEXT_FIELD_KEY = "tab"  # tecla para moverte entre campos
OPEN_FORM_HOTKEY = None # ej. "ctrl+n" si abres un formulario nuevo por atajo (o deja None)

# Teclas de control del operador
PAUSE_KEY = "f8"        # Pausar/Reanudar
SKIP_ROW_KEY = "f9"     # Saltar a la siguiente fila
ABORT_KEY = "esc"       # Abortar todo
# ------------------------------------------------


def log(msg):
	print(time.strftime("[%H:%M:%S]"), msg)
	sys.stdout.flush()


def focus_rdp_window():
	# Busca una ventana por cualquiera de los títulos candidatos
	wins = []
	for w in gw.getAllWindows():
		title = (w.title or "").strip()
		for candidate in RDP_WINDOW_TITLES:
			if candidate.lower() in title.lower():
				wins.append(w)
				break
	if not wins:
		raise RuntimeError(
			"No encontré la ventana RDP. Ajusta RDP_WINDOW_TITLES para que coincida con el título."
		)
	# Toma la primera y enfócala
	win = wins[0]
	if win.isMinimized:
		win.restore()
		time.sleep(0.5)
	win.activate()
	time.sleep(0.5)
	return win


def safe_type(text):
	if text is None:
		return
	s = str(text)
	# Limpieza básica (evita 'nan' de pandas)
	if s.lower() == "nan":
		s = ""
	ag.typewrite(s, interval=TYPE_DELAY)


def wait_unpaused():
	# Pausa con F8; reanuda con F8; aborta con ESC
	while True:
		if keyboard.is_pressed(ABORT_KEY):
			raise KeyboardInterrupt("Abortado por el usuario (ESC).")
		if keyboard.is_pressed(PAUSE_KEY):
			log("Pausa activada. Vuelve a presionar F8 para reanudar.")
			# Espera hasta que suelte F8
			while keyboard.is_pressed(PAUSE_KEY):
				time.sleep(0.2)
			# Espera hasta que vuelva a presionarla para reanudar
			while not keyboard.is_pressed(PAUSE_KEY):
				time.sleep(0.2)
			# Soltar
			while keyboard.is_pressed(PAUSE_KEY):
				time.sleep(0.2)
			log("Reanudado.")
		break


def open_new_form_if_needed():
	if OPEN_FORM_HOTKEY:
		ag.hotkey(*OPEN_FORM_HOTKEY.split("+"))
		time.sleep(0.5)


def process_row(row_dict):
	"""Rellena un formulario de Ventor con la fila actual usando TAB para navegar."""
	wait_unpaused()
	open_new_form_if_needed()

	for i, field in enumerate(FIELD_ORDER):
		wait_unpaused()
		value = row_dict.get(field, "")
		safe_type(value)
		time.sleep(ACTION_DELAY)
		# Ir al siguiente campo (excepto si es el último; allí no hacemos TAB)
		if i < len(FIELD_ORDER) - 1:
			ag.press(NEXT_FIELD_KEY)
			time.sleep(ACTION_DELAY)

	# Guardar / continuar
	ag.press(SAVE_KEY)
	time.sleep(ACTION_DELAY)


def main():
	# 1) Leer Excel
	log(f"Leyendo Excel: {EXCEL_PATH} (hoja={EXCEL_SHEET})")
	df = pd.read_excel(EXCEL_PATH, sheet_name=EXCEL_SHEET, dtype=str)
	# Filtramos filas
	start_idx = START_ROW - 1 if START_ROW else 0
	end_idx = END_ROW
	df = df.iloc[start_idx:end_idx].reset_index(drop=True)

	# 2) Validaciones de columnas
	missing = [c for c in FIELD_ORDER if c not in df.columns]
	if missing:
		raise ValueError(f"Faltan columnas en el Excel: {missing}")

	# 3) Enfocar ventana RDP
	log("Buscando ventana RDP...")
	focus_rdp_window()
	log("Ventana RDP enfocada. Empiezo en 3 segundos: colócate en el primer campo del formulario.")
	time.sleep(3)

	# 4) Iterar filas
	for idx, row in df.iterrows():
		log(f"Fila {idx+1}/{len(df)}. F9=salta, F8=pausa, ESC=aborta")
		if keyboard.is_pressed(SKIP_ROW_KEY):
			log("Fila saltada por el usuario (F9).")
			# Consumimos la pulsación
			while keyboard.is_pressed(SKIP_ROW_KEY):
				time.sleep(0.2)
			continue

		data = {k: row.get(k, "") for k in FIELD_ORDER}
		try:
			process_row(data)
		except KeyboardInterrupt:
			log("Abortado por el usuario.")
			break
		except Exception as e:
			log(f"Error en fila {idx+1}: {e}")
			# Opcional: decide si quieres continuar o abortar
			# break
			continue

	log("Proceso finalizado.")


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		log(f"ERROR: {e}")
		sys.exit(1)