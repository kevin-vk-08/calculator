import streamlit as st
# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("💪 Calculadora de REBAJAS")
st.markdown("Bienvenido. Introduce el precio original.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
descuento = st.sidebar.slider("Tu descuento (%)", 50, 25, 5)
precio_original = st.sidebar.slider("Coste del producto ($)", 1.00, 100.0, 50.0)
# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
   
    # Fórmula Matemática: descuento entre 100
    precio_final = precio_original * (descuento / 100)
   
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
   
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final es:", value=f"{precio_final:.2f} $")
       
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento > 50:
            st.warning("mas del 50")
            st.write("menudo chollo")
        elif descuento >=25:
            st.success(" igual o mayor de 25")
            st.balloons("buena oferta")
        elif descuento >=5:
            st.warning("igual o mayor de 5")
            st.write("oferta normalita")

    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' Precio_{final} = Precio_{original} \times \left(1 - \frac{Descuento}{100}\right)''')
