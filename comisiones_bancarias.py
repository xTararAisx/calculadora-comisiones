import streamlit as st

def calcular_comisiones(transacciones, comisiones):
    total_comisiones = 0
    for transaccion, comision in zip(transacciones, comisiones):
        total_comisiones += transaccion * comision / 100
    return total_comisiones

def verificar_cargos_indebidos(comisiones):
    comisiones_indebidas = [comision for comision in comisiones if comision > 13]
    return len(comisiones_indebidas) > 0

def main():
    st.markdown("<h1><a href='https://acead.es'>Calculadora de Comisiones Bancarias - Acead.es</a></h1>", unsafe_allow_html=True)

    num_transacciones = st.number_input("Número de transacciones", min_value=1, max_value=10, value=1, step=1)

    transacciones = []
    comisiones = []
    for i in range(num_transacciones):
        st.subheader(f"Transacción {i + 1}")
        monto = st.number_input(f"Monto de la transacción {i + 1}", min_value=0.0, value=0.0, step=0.01)
        comision = st.number_input(f"Comisión por transacción {i + 1} (%)", min_value=0.0, value=0.0, step=0.01)
        transacciones.append(monto)
        comisiones.append(comision)

    calcular = st.button("Calcular")
    if calcular:
        total_comisiones = calcular_comisiones(transacciones, comisiones)
        st.write(f"Has pagado un total de ${total_comisiones:.2f} en comisiones bancarias.")

        cargos_indebidos = verificar_cargos_indebidos(comisiones)
        if cargos_indebidos:
            st.error("Se han detectado cargos indebidos. Por favor, ponte en contacto con tu entidad bancaria para reclamar.")
        else:
            st.success("No se han detectado cargos indebidos en tus transacciones.")

if __name__ == "__main__":
    main()
