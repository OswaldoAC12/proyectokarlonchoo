import streamlit as st
from datetime import datetime

# Inicializar datos
if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

if "pagos" not in st.session_state:
    st.session_state.pagos = []

st.set_page_config(page_title="Restaurante", layout="wide")
precios = {
    "Ají de gallina": 18.0,
    "Lomo saltado": 22.0,
    "Arroz con pollo": 16.0,
    "Carapulcra": 17.0,
    "Papa a la huancaína": 10.0,
    "Pollo a la brasa": 20.0,
    "Tacu tacu": 15.0,
    "Anticuchos": 12.0,
    "Cau cau": 14.0,
    "Ceviche clásico": 25.0,
    "Chupe de camarones": 28.0,
    "Escabeche": 16.0,
    "Seco de cordero": 24.0,
    "Chanfainita": 13.0,
    "Causa limeña": 11.0,
    "Rocoto relleno": 14.0,
    "Tamales": 9.0,
    "Chicharrón": 18.0,
    "Sopa seca": 15.0,
    "Mondonguito": 14.0
}

rol = st.sidebar.selectbox("Selecciona tu rol", ["Mesero", "Cocinero", "Cajero", "Administrador"])

# ---------------- MESERO ----------------
if rol == "Mesero":
    st.title("👨‍🍳 Panel del Mesero")
    opcion = st.sidebar.radio("Secciones", ["Registrar Pedido", "Ver Pedidos", "Estado de Pedidos", "Pedidos en Cocina"])

    # Lista de platos y sus imágenes
    platos_criollos = [
        "Ají de gallina", "Lomo saltado", "Arroz con pollo", "Carapulcra",
        "Papa a la huancaína", "Pollo a la brasa", "Tacu tacu", "Anticuchos",
        "Cau cau", "Ceviche clásico", "Chupe de camarones", "Escabeche",
        "Seco de cordero", "Chanfainita", "Causa limeña", "Rocoto relleno",
        "Tamales", "Chicharrón", "Sopa seca", "Mondonguito"
    ]

    imagenes = {
        "Ají de gallina": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp9eo6aWObF19p9pQl_Jr9yjmiFDhR3xLVRQ&s",
        "Lomo saltado": "https://assets.afcdn.com/recipe/20210416/119490_w1024h1024c1cx363cy240cxt0cyt0cxb726cyb480.webp",
        "Arroz con pollo": "https://imgmedia.buenazo.pe/1200x660/buenazo/original/2022/10/24/60d89da6913c240e6725db08.jpg",
        "Carapulcra": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHJ6-cPvM7rmL9YvaefnntQ-U22tA4nhMdGQ&s",
        "Papa a la huancaína": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMt-wTgx87RaNMkaNKNpJ4yCNk11eCtw2_dw&s",
        "Pollo a la brasa": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRKYPExrScezZ9yqUYPZRzVOQWVUjJnoLijA&s",
        "Tacu tacu": "https://comedera.com/wp-content/uploads/sites/9/2022/03/Tacu-tacu-shutterstock_1604013508.jpg",
        "Anticuchos": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz1xOWmqZVAM9Xnm9ekNTpzkK3uXsLOVlfkg&s",
        "Cau cau": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzbuMem2a1B8F-7XDQHkn9DRADtUOPCS6iyQ&s",
        "Ceviche clásico": "https://www.elespectador.com/resizer/v2/2AVD5Z6Y2ZFWHETPQGCPLMNK4A.jpg?auth=82394bc07906097860918c7a77b6320dbba80a4b67cc293a909e810ae6941229&width=920&height=613&smart=true&quality=60",
        "Chupe de camarones": "https://www.comida-peruana.com/base/stock/Recipe/chupe-de-camarones/chupe-de-camarones_web.jpg.webp",
        "Escabeche": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSvyi_SbkGQFGUGhuVNLN5MHLNi_-YCQFdmA&s",
        "Seco de cordero": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn4bly9EUf2yj9R8_ELapZQhtXhc1KlTY30Q&s",
        "Chanfainita": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTONILZGS3lYDal_0g5Eb7GlQByg2Z0LeDJ3Q&s",
        "Causa limeña": "https://via.placeholder.com/400x300.png?text=Causa+lime%C3%B1a",
        "Rocoto relleno": "https://perudelights.com/wp-content/uploads/2012/04/r4.jpg",
        "Tamales": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNQuEGWwnf1u2yxxFjWuHkKSSTglIglL7Zxw&s",
        "Chicharrón": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT8X3XJZFWZY0YBi5UtyM2Gj2Yi_94MYTTHA&s",
        "Sopa seca": "https://via.placeholder.com/400x300.png?text=Sopa+seca",
        "Mondonguito": "https://i.ytimg.com/vi/0K3SVByhoDc/maxresdefault.jpg"
    }

    if opcion == "Registrar Pedido":
        st.subheader("📝 Nuevo Pedido")

        # Selectbox e imagen FUERA del formulario para actualizar en tiempo real
        plato = st.selectbox("Selecciona un platillo", platos_criollos, key="plato_seleccionado")
        if plato in imagenes:
            st.image(imagenes[plato], caption=plato, use_container_width=True)

        # Formulario para cantidad y mesa
        with st.form("form_pedido"):
            col1, col2 = st.columns(2)
            with col1:
                cantidad = st.number_input("Cantidad", min_value=1, key="cantidad_pedido")
            with col2:
                mesa = st.text_input("Número de mesa", key="mesa_pedido")

            if st.form_submit_button("Agregar pedido"):
                if plato and mesa:
                    st.session_state.pedidos.append({
                        "plato": plato,
                        "cantidad": cantidad,
                        "mesa": mesa,
                        "estado": "Pendiente"
                    })
                    st.success(f"Pedido agregado: {cantidad} x {plato} (Mesa {mesa})")
                else:
                    st.warning("Completa todos los campos.")


    elif opcion == "Ver Pedidos":
        st.subheader("📋 Lista de Pedidos")
        if st.session_state.pedidos:
            for p in st.session_state.pedidos:
                st.markdown(f"**Mesa {p['mesa']}** - {p['cantidad']} x {p['plato']} | Estado: `{p['estado']}`")
                st.divider()
        else:
            st.info("No hay pedidos registrados.")

    elif opcion == "Estado de Pedidos":
        st.subheader("🔄 Cambiar Estado de Pedidos")
        for i, pedido in enumerate(st.session_state.pedidos):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(f"**Mesa {pedido['mesa']}** - {pedido['cantidad']} x {pedido['plato']}")
                st.markdown(f"`Estado actual:` **{pedido['estado']}**")
            with col2:
                if st.button("➡️ Enviar a Cocina", key=f"cocina_{i}"):
                    pedido["estado"] = "Enviado a cocina"
                    st.toast("Enviado a cocina", icon="🍳")
                if st.button("✅ Marcar como Servido", key=f"servido_{i}"):
                    pedido["estado"] = "Servido"
                    st.toast("Pedido servido", icon="✅")
            st.divider()

    elif opcion == "Pedidos en Cocina":
        st.subheader("👨‍🍳 Pedidos Enviados a Cocina")
        enviados = [p for p in st.session_state.pedidos if p["estado"] == "Enviado a cocina"]
        if enviados:
            for p in enviados:
                st.success(f"Mesa {p['mesa']}: {p['cantidad']} x {p['plato']}")
        else:
            st.info("No hay pedidos en cocina.")

# ---------------- COCINERO ----------------
elif rol == "Cocinero":
    st.title("🍳 Panel del Cocinero")
    st.subheader("Pedidos en Cocina")

    pedidos_cocina = [p for p in st.session_state.pedidos if p["estado"] == "Enviado a cocina"]

    if pedidos_cocina:
        for i, pedido in enumerate(pedidos_cocina):
            st.markdown(f"**Mesa {pedido['mesa']}** - {pedido['cantidad']} x {pedido['plato']}")
            estado_actual = pedido["estado"]
            nuevo_estado = st.selectbox(
                f"Actualizar estado del pedido #{i + 1}",
                ["Enviado a cocina", "En preparación", "Listo para servir"],
                index=["Enviado a cocina", "En preparación", "Listo para servir"].index(estado_actual),
                key=f"estado_cocina_{i}"
            )
            pedido["estado"] = nuevo_estado
            st.markdown(f"`Estado actualizado:` **{nuevo_estado}**")
            st.divider()
    else:
        st.info("No hay pedidos pendientes en cocina.")

# ---------------- CAJERO ----------------
if rol == "Cajero":
    st.title("💰 Panel del Cajero")
    opcion = st.sidebar.radio("Secciones", ["Registrar Pago", "Resumen de Pagos"])

    if opcion == "Registrar Pago":
        st.subheader("💵 Pedidos Servidos Listos para Cobrar")
        servidos = [
            p for p in st.session_state.pedidos
            if p["estado"] in ["Servido", "Listo para servir"] and "pagado" not in p
        ]

        if servidos:
            for i, pedido in enumerate(servidos):
                st.markdown(f"🧾 **Mesa {pedido['mesa']}** - {pedido['cantidad']} x {pedido['plato']}")

                with st.form(f"pago_form_{i}"):
                    precio_unitario = precios.get(pedido["plato"], 0)
                    total = precio_unitario * pedido["cantidad"]
                    st.write(f"💲 Precio unitario: S/ {precio_unitario:.2f}")
                    st.write(f"💲 Total a pagar: S/ {total:.2f}")

                    metodo = st.selectbox(
                        "Método de pago", ["Efectivo", "Tarjeta", "PLIN", "YAPE"],
                        key=f"metodo_{i}"
                    )
                    confirmar = st.form_submit_button("Registrar Pago")

                    if confirmar:
                        pedido["pagado"] = True
                        st.session_state.pagos.append({
                            "mesa": pedido["mesa"],
                            "plato": pedido["plato"],
                            "cantidad": pedido["cantidad"],
                            "monto": total,
                            "metodo": metodo,
                            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

                        st.success("✅ Pago registrado correctamente")
                        st.info(f"""
                        ### 🧾 RECIBO
                        - 🪑 Mesa: {pedido['mesa']}
                        - 🍽️ Plato: {pedido['plato']} x {pedido['cantidad']}
                        - 💲 Total: S/ {total:.2f}
                        - 💳 Método: {metodo}
                        - 📅 Fecha: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
                        """)
                st.divider()
        else:
            st.info("No hay pedidos servidos pendientes de pago.")

    elif opcion == "Resumen de Pagos":
        st.subheader("📊 Resumen de Pagos Realizados")
        if st.session_state.pagos:
            total = sum(p["monto"] for p in st.session_state.pagos)
            st.metric("Total Recaudado", f"S/ {total:.2f}")

            metodos = ["Efectivo", "Tarjeta", "PLIN", "YAPE"]
            for metodo in metodos:
                subtotal = sum(p["monto"] for p in st.session_state.pagos if p["metodo"] == metodo)
                st.write(f"🔹 {metodo}: S/ {subtotal:.2f}")
        else:
            st.warning("No hay pagos aún.")


# ---------------- ADMINISTRADOR ----------------
elif rol == "Administrador":
    st.title("📈 Panel del Administrador")
    st.subheader("Reporte de Ventas")

    if st.session_state.pagos:
        fecha_filtro = st.date_input("Filtrar por fecha", value=datetime.now().date())
        pagos_filtrados = [p for p in st.session_state.pagos if p["fecha"].startswith(str(fecha_filtro))]

        if pagos_filtrados:
            st.write("### 💼 Detalle de Pagos")
            for p in pagos_filtrados:
                st.markdown(f"- Mesa {p['mesa']} | {p['plato']} | S/ {p['monto']} | {p['metodo']} | {p['fecha']}")

            total = sum(p["monto"] for p in pagos_filtrados)
            st.metric("Total del día", f"S/ {total:.2f}")

            st.download_button("📥 Descargar Reporte (CSV)",
                               data="\n".join([f"{p['mesa']},{p['plato']},{p['monto']},{p['metodo']},{p['fecha']}" for p in pagos_filtrados]),
                               file_name="reporte_ventas.csv",
                               mime="text/csv")
        else:
            st.info("No hay pagos para la fecha seleccionada.")
    else:
        st.warning("No hay ventas registradas.")
