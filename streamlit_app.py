import streamlit as st
from datetime import datetime

# Inicializar datos
if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

if "pagos" not in st.session_state:
    st.session_state.pagos = []

# Iniciar las reservas predeterminadas
if "reservas" not in st.session_state:
    st.session_state.reservas = [
        {"nombre": "Reserva 1", "fecha": "2025-07-03 12:30", "mesa": 1},
        {"nombre": "Reserva 2", "fecha": "2025-07-03 12:30", "mesa": 2}
    ]

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
# Enlaces de las imágenes
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
# Selección de rol
rol = st.sidebar.selectbox("Selecciona tu rol", ["Mesero", "Cocinero", "Cajero", "Administrador"])

# ---------------- MESERO ----------------
if rol == "Mesero":
    st.title("👨‍🍳 Panel del Mesero")
    opcion = st.sidebar.radio("Secciones", ["Registrar Pedido", "Ver Pedidos", "Estado de Pedidos", "Pedidos en Cocina"])

    # Registrar Pedido
    if opcion == "Registrar Pedido":
        st.subheader("📝 Nuevo Pedido")
        platos_seleccionados = st.multiselect("Selecciona los platillos", precios.keys(), key="platos_seleccionados")
        cantidades = {plato: st.number_input(f"Cantidad de {plato}", min_value=1, key=f"cantidad_{plato}") for plato in platos_seleccionados}

        mesas_input = st.text_input("Número(s) de mesa(s) (separadas por coma)", key="mesas_pedido")

        with st.form("form_pedido"):
            if st.form_submit_button("Agregar pedido"):
                if not mesas_input.strip() or len(platos_seleccionados) == 0 or any(cantidad <= 0 for cantidad in cantidades.values()):
                    st.warning("Por favor, ingresa los datos correctamente.")
                else:
                    mesas = [mesa.strip() for mesa in mesas_input.split(",")]
                    for mesa in mesas:
                        pedido = {"mesa": mesa, "platos": [], "estado": "Pendiente"}
                        for plato in platos_seleccionados:
                            pedido["platos"].append({"nombre": plato, "cantidad": cantidades[plato], "estado": "Pendiente"})
                        st.session_state.pedidos.append(pedido)
                    st.success(f"Pedido(s) agregado(s) para las mesas: {', '.join(mesas)}")

    # Ver Pedidos
    elif opcion == "Ver Pedidos":
        st.subheader("📋 Lista de Pedidos")
        if st.session_state.pedidos:
            for p in st.session_state.pedidos:
                for plato in p["platos"]:
                    st.markdown(f"**Mesa {p['mesa']}** - {plato['cantidad']} x {plato['nombre']} | Estado: {plato['estado']}")
        else:
            st.info("No hay pedidos registrados.")

    # Estado de Pedidos
    elif opcion == "Estado de Pedidos":
        st.subheader("🔄 Cambiar Estado de Pedidos")
        for i, pedido in enumerate(st.session_state.pedidos):
            for plato in pedido["platos"]:
                st.markdown(f"**Mesa {pedido['mesa']}** - {plato['cantidad']} x {plato['nombre']} | Estado: {plato['estado']}")
            if st.button(f"➡️ Enviar a Cocina para Mesa {pedido['mesa']}", key=f"cocina_{i}"):
                for plato in pedido["platos"]:
                    plato["estado"] = "Enviado a cocina"
                st.success(f"Pedido de Mesa {pedido['mesa']} enviado a cocina.")
            if st.button(f"✅ Marcar como Servido para Mesa {pedido['mesa']}", key=f"servido_{i}"):
                for plato in pedido["platos"]:
                    plato["estado"] = "Servido"
                st.success(f"Pedido de Mesa {pedido['mesa']} marcado como servido.")

    # Pedidos en Cocina
    elif opcion == "Pedidos en Cocina":
        st.subheader("👨‍🍳 Pedidos Enviados a Cocina")
        enviados = [p for p in st.session_state.pedidos if any(plato["estado"] == "Enviado a cocina" for plato in p["platos"])]
        if enviados:
            for p in enviados:
                for plato in p["platos"]:
                    if plato["estado"] == "Enviado a cocina":
                        st.success(f"Mesa {p['mesa']}: {plato['cantidad']} x {plato['nombre']}")
        else:
            st.info("No hay pedidos en cocina.")

# ---------------- COCINERO ----------------
elif rol == "Cocinero":
    st.title("👨‍🍳 Panel del Cocinero")
    opcion = st.sidebar.radio("Secciones", ["Ver Pedidos", "Actualizar Estado de Pedidos"])

    if opcion == "Ver Pedidos":
        st.subheader("📋 Lista de Pedidos")
        for p in st.session_state.pedidos:
            for plato in p["platos"]:
                st.markdown(f"**Mesa {p['mesa']}** - {plato['cantidad']} x {plato['nombre']} | Estado: {plato['estado']}")

    elif opcion == "Actualizar Estado de Pedidos":
        st.subheader("🔄 Cambiar Estado de Pedidos")
        for i, pedido in enumerate(st.session_state.pedidos):
            col1, col2 = st.columns([3, 2])
            with col1:
                for plato in pedido["platos"]:
                    st.markdown(f"**Mesa {pedido['mesa']}** - {plato['cantidad']} x {plato['nombre']}")
                    st.markdown(f"Estado actual: **{plato['estado']}**")
            with col2:
                if st.button("➡️ En preparación", key=f"preparacion_{i}"):
                    for plato in pedido["platos"]:
                        plato["estado"] = "En preparación"
                    st.toast("Pedido en preparación", icon="🍳")
                if st.button("✅ Listo para servir", key=f"servido_{i}"):
                    for plato in pedido["platos"]:
                        plato["estado"] = "Listo para servir"
                    st.toast("Pedido listo para servir", icon="✅")
            st.divider()

# ---------------- CAJERO ----------------
elif rol == "Cajero":
    st.title("💳 Panel del Cajero")
    opcion = st.sidebar.radio("Secciones", ["Ver Pedidos", "Registrar Pago", "Ver Reportes de Pagos", "Reservas"])

    if opcion == "Reservas":
        st.subheader("📝 Reservas para el 3 de Julio a las 12:30")
        
        # Mostrar las reservas predeterminadas
        if st.session_state.reservas:
            for reserva in st.session_state.reservas:
                st.markdown(f"**{reserva['nombre']}** - Mesa: {reserva['mesa']} - Fecha: {reserva['fecha']}")

        # Agregar nueva reserva
        st.subheader("📅 Registrar Nueva Reserva")
        
        # Campos para registrar la nueva reserva
        nombre_reserva = st.text_input("Nombre de la persona", key="nombre_reserva")
        mesa_reserva = st.number_input("Número de mesa", min_value=1, max_value=20, key="mesa_reserva")  # Cambia el límite según sea necesario
        fecha_reserva = st.text_input("Fecha y Hora (formato YYYY-MM-DD HH:MM)", key="fecha_reserva")

        # Pago parcial de la reserva
        pago_parcial = st.number_input("Pago Parcial", min_value=0.0, value=0.0, step=1.0, key="pago_parcial_reserva")

        if st.button("Registrar Reserva"):
            if nombre_reserva and mesa_reserva and fecha_reserva:
                nueva_reserva = {
                    "nombre": nombre_reserva,
                    "fecha": fecha_reserva,
                    "mesa": mesa_reserva,
                    "pago_parcial": pago_parcial  # Guardamos el pago parcial
                }
                st.session_state.reservas.append(nueva_reserva)
                
                # Registrar el pago parcial como parte de las ventas
                st.session_state.pagos.append({
                    "mesa": mesa_reserva,
                    "monto": pago_parcial,
                    "fecha": datetime.now(),
                    "metodo_pago": "Pago Parcial - Reserva"
                })
                
                st.success(f"Reserva registrada para {nombre_reserva} en la Mesa {mesa_reserva} a las {fecha_reserva}. Pago parcial: S/ {pago_parcial:.2f}.")
            else:
                st.warning("Por favor, completa todos los campos.")

    elif opcion == "Ver Pedidos":
        st.subheader("📋 Lista de Pedidos con Precios")
        for p in st.session_state.pedidos:
            for plato in p["platos"]:
                precio_plato = precios.get(plato['nombre'], 0)
                st.markdown(f"**Mesa {p['mesa']}** - {plato['cantidad']} x {plato['nombre']} | Precio: S/ {precio_plato} | Estado: {plato['estado']}")

    elif opcion == "Registrar Pago":
        st.subheader("💰 Registrar Pago")

        # Mostrar solo los pedidos servidos
        mesas_servidas = [pedido for pedido in st.session_state.pedidos if all(plato['estado'] == 'Servido' for plato in pedido['platos'])]
        if mesas_servidas:
            mesa_paga = st.selectbox("Selecciona la mesa para pagar", [pedido['mesa'] for pedido in mesas_servidas])
            pedido_seleccionado = next(pedido for pedido in mesas_servidas if pedido['mesa'] == mesa_paga)
            
            # Calcular el total a pagar
            total_a_pagar = sum(precios.get(plato['nombre'], 0) * plato['cantidad'] for plato in pedido_seleccionado['platos'])

            # Mostrar el total a pagar directamente en el campo de monto
            monto_pagado = st.number_input("Monto Pagado", min_value=0.01, value=total_a_pagar)

            st.write(f"**Total a pagar por la mesa {mesa_paga}: S/ {total_a_pagar:.2f}**")

            # Mostrar método de pago
            metodo_pago = st.selectbox("Método de Pago", ["Efectivo", "Yape", "Plin", "Tarjeta"])

            if st.button("Registrar Pago"):
                if monto_pagado >= total_a_pagar:
                    st.session_state.pagos.append({
                        "mesa": mesa_paga,
                        "monto": monto_pagado,
                        "fecha": datetime.now(),
                        "metodo_pago": metodo_pago
                    })
                    st.success(f"Pago registrado correctamente. Método de pago: {metodo_pago}.")
                else:
                    st.warning("El monto pagado debe ser igual o mayor al total.")
        else:
            st.info("No hay pedidos servidos para pagar.")

    elif opcion == "Ver Reportes de Pagos":
        st.subheader("📊 Reporte de Pagos")
        if st.session_state.pagos:
            for pago in st.session_state.pagos:
                st.markdown(f"Mesa #{pago['mesa']} - Monto: S/ {pago['monto']} - Fecha: {pago['fecha']} - Método de Pago: {pago['metodo_pago']}")
        else:
            st.info("No hay pagos registrados.")

# ---------------- ADMINISTRADOR ----------------
elif rol == "Administrador":
    st.title("🛠 Panel del Administrador")
    opcion = st.sidebar.radio("Secciones", ["Ver Reporte de Ventas"])

    if opcion == "Ver Reporte de Ventas":
        st.subheader("📊 Reporte de Ventas")
        
        if st.session_state.pagos:
            total_ventas = sum(pago['monto'] for pago in st.session_state.pagos)
            st.write(f"**Total de ventas: S/ {total_ventas:.2f}**")
            st.write("**Detalles de los pagos registrados:**")
            for pago in st.session_state.pagos:
                st.markdown(f"**Mesa #{pago['mesa']}** - Monto: S/ {pago['monto']} - Fecha: {pago['fecha']} - Método de Pago: {pago['metodo_pago']}")
        else:
            st.info("No hay pagos registrados aún.")
