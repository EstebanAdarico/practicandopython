B) Ventor de escritorio (Windows + pywinauto)
1) Instalar
pip install pandas pywinauto


Tip: instala Windows 10/11 SDK “Inspect.exe” para ver AutomationId, Name, ClassName de cada control.

2) Script ventor_desktop_rpa.py
import time
import logging
import pandas as pd
from pathlib import Path
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import timings

# ========= CONFIG =========
EXCEL_PATH = "datos.xlsx"
HOJA = "Hoja1"

# Ruta al ejecutable de Ventor (ajusta)
VENTOR_EXE = r"C:\Program Files\Ventor\ventor.exe"

# Título de la ventana principal (ajusta exactamente)
MAIN_WINDOW_TITLE = "Ventor - Inventario"

# Mapeo: columna_excel -> dict con tipo de localización
# Puedes usar "automation_id", "title" (name), o "class_name"
FIELD_MAP = {
    "codigo":      {"automation_id": "txtCode"},
    "descripcion": {"automation_id": "txtDescription"},
    "cantidad":    {"automation_id": "txtQty"},
    "precio":      {"automation_id": "txtPrice"},
}

# Botón guardar/enviar
BTN_SAVE = {"automation_id": "btnSave"}

# Si necesitas ir a “Nuevo”
BTN_NEW  = {"automation_id": "btnNew"}

TIMEOUT = 10
# ==========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s"
)
timings.after_clickinput_wait = 0.3

def connect_app():
    try:
        app = Application(backend="uia").connect(title=MAIN_WINDOW_TITLE, timeout=5)
    except Exception:
        app = Application(backend="uia").start(VENTOR_EXE)
        app.connect(title=MAIN_WINDOW_TITLE, timeout=20)
    return app

def find_ctrl(dlg, spec: dict):
    if "automation_id" in spec:
        return dlg.child_window(auto_id=spec["automation_id"], control_type="Edit").wrapper_object()
    if "title" in spec:
        return dlg.child_window(title=spec["title"]).wrapper_object()
    if "class_name" in spec:
        return dlg.child_window(class_name=spec["class_name"]).wrapper_object()
    raise ValueError("Especifica automation_id/title/class_name")

def click_btn(dlg, spec: dict):
    if "automation_id" in spec:
        return dlg.child_window(auto_id=spec["automation_id"], control_type="Button").wrapper_object().click_input()
    if "title" in spec:
        return dlg.child_window(title=spec["title"], control_type="Button").wrapper_object().click_input()
    if "class_name" in spec:
        return dlg.child_window(class_name=spec["class_name"], control_type="Button").wrapper_object().click_input()
    raise ValueError("Especifica automation_id/title/class_name")

def crear_registro(dlg, fila: dict):
    # Ir a “Nuevo” si aplica
    try:
        click_btn(dlg, BTN_NEW)
        time.sleep(0.5)
    except Exception:
        pass

    for col_excel, locator in FIELD_MAP.items():
        value = str(fila.get(col_excel, ""))
        try:
            edit = find_ctrl(dlg, locator)
            edit.click_input()
            edit.type_keys("^a{BACKSPACE}")  # limpiar
            if value:
                edit.type_keys(value, with_spaces=True, set_foreground=True)
        except Exception as e:
            logging.error(f"No pude escribir {col_excel}: {e}")

    # Guardar
    click_btn(dlg, BTN_SAVE)
    time.sleep(0.7)  # espera breve; ajusta si hay toast/diálogo

def main():
    df = pd.read_excel(EXCEL_PATH, sheet_name=HOJA).fillna("")
    logging.info(f"Cargando {len(df)} filas desde {Path(EXCEL_PATH).resolve()}")

    app = connect_app()
    dlg = app.window(title=MAIN_WINDOW_TITLE)
    dlg.set_focus()

    for i, row in df.iterrows():
        logging.info(f"Procesando fila {i+1}: {row.to_dict()}")
        try:
            crear_registro(dlg, row.to_dict())
        except Exception as e:
            logging.error(f"Error en fila {i+1}: {e}")
            continue

    logging.info("¡Proceso completado!")

if __name__ == "__main__":
    main()


Cómo hallar los IDs de los campos:

Abre Inspect.exe (Windows SDK).

Pasa el cursor sobre cada campo en Ventor y copia su AutomationId.

Pon esos IDs en FIELD_MAP y los botones en BTN_SAVE, BTN_NEW.

Si no hay AutomationId, usa title (Name) o class_name.

Buenas prácticas para que no falle en producción

Validación previa del Excel: antes de iterar, valida columnas y tipos (por ejemplo, cantidad numérica).

Idempotencia: si el registro existe, decide si “actualizas” o “saltas” (puedes buscar por codigo primero).

Logs + CSV de errores: guarda filas con error en errores.csv para reintentar.

Pausas y esperas explícitas: en web usa WebDriverWait; en desktop, time.sleep y wrapper_object() con cuidado.

Dry-run: agrega un flag --dry-run para simular sin guardar.

Reanudación: guarda el último índice procesado en un .state para continuar si se corta.