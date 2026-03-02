import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ventor Panel", layout="wide")

st.sidebar.title("Ventor Panel")
seccion = st.sidebar.radio("Secciones", ["📦 Stock", "🧾 Requerimientos", "📊 Dashboard"])

# Data demo
df = pd.DataFrame([
   {"codigo":"A01","descripcion":"Manguera 1/2","stock":3,"minimo":5},
   {"codigo":"B02","descripcion":"Adaptador","stock":10,"minimo":4},
   {"codigo":"C03","descripcion":"Conexión 3/4","stock":1,"minimo":2},
])

if seccion == "📦 Stock":
   st.title("📦 Stock")

   t1, t2, t3 = st.tabs(["Todos", "Bajos", "Buscar"])

   with t1:
      st.dataframe(df, use_container_width=True)

   with t2:
      bajos = df[df["stock"] <= df["minimo"]]
      st.dataframe(bajos, use_container_width=True)

   with t3:
      q = st.text_input("Buscar")
      if q:
            mask = df["codigo"].str.contains(q, case=False) | df["descripcion"].str.contains(q, case=False)
            st.dataframe(df[mask], use_container_width=True)
      else:
            st.info("Escribe para buscar.")

elif seccion == "🧾 Requerimientos":
   st.title("🧾 Requerimientos")
   st.write("Aquí va: generar requerimiento por mínimos, exportar Excel, etc.")
   bajos = df[df["stock"] <= df["minimo"]].copy()
   bajos["cantidad_requerida"] = (bajos["minimo"] - bajos["stock"]).clip(lower=0)
   st.dataframe(bajos, use_container_width=True)

   st.button("Generar Excel (aquí lo conectamos luego)")

else:
   st.title("📊 Dashboard")
   c1, c2, c3 = st.columns(3)
   c1.metric("Ítems", len(df))
   c2.metric("Ítems bajos", int((df["stock"] <= df["minimo"]).sum()))
   c3.metric("Stock total", int(df["stock"].sum()))