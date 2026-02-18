import streamlit as st



# 1. Configuración de la página

st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")



# Título y Descripción

st.title("💯 Calculadora de Rebajas")

st.markdown("Llegan las rebajas y es difícil calcular mentalmente cuánto se queda un producto. Crea una app que ayude a los compradores a saber el precio final rápidamente.")

st.write("---") # Línea separadora



# 2. Entrada de Datos (Barra Lateral)

st.sidebar.header("Tus Datos")

precio = st.sidebar.number_input("precio ($)", min_value=0, max_value=200, value=60)

rebaja = st.sidebar.slider("rebaja (%)", 0, 100, 50)



# 3. Botón de Cálculo y Lógica

if st.button("Calcular ahora"):

    

    # Fórmula Matemática: Peso entre altura al cuadrado

    ahorro = precio*(rebaja/100)

    precio_final = precio - ahorro

    

    # 4. Mostrar Resultado con Diseño

    col1, col2 = st.columns(2)

    

    with col1:

        # Usamos metric para que el número se vea grande

        st.metric(label="Precio final:", value=f"{ahorro:.2f}$")

        st.success(f"Te ahorras: {precio_final}")

    

    with col2:

        # Usamos condicionales (if/elif/else) para el diagnóstico

        if rebaja< 20:

            st.warning("No esta mal")

            st.write("La proxima vez mas suerte.")

        elif 20 <= rebaja < 60:

            st.success("✅ Good choice")

            st.balloons() # ¡Premio!

        elif 60 <= rebaja < 80:

            st.success("🟠 Loteriaaaa")

            st.write("Que suerte")

        else:

            st.success("Obesidad")

            st.write("Es importante cuidar tu salud.")
