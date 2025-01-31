import os
import streamlit as st
from dotenv import load_dotenv
import sys
from pathlib import Path

# Añadir el directorio raíz al path de Python
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

from src.workflow import create_workflow

def main():
    st.set_page_config(page_title="Sistema de Gestión de Pedidos", layout="wide")
    
    st.title("Sistema de Gestión de Pedidos con IA")
    st.markdown("---")

    # Load environment variables
    load_dotenv()
    
    # Create the workflow
    agent = create_workflow()
    
    # Crear dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Prueba de Cancelación de Pedido")
        st.code('''user_query = "Deseo cancelar el pedido con order_id 223"''', language='python')
        if st.button("Ejecutar Prueba de Cancelación"):
            user_query = "Deseo cancelar el pedido con order_id 223"
            st.write("Resultado:")
            with st.spinner("Procesando..."):
                for chunk in agent.stream(
                    {"messages": [("user", user_query)]},
                    stream_mode="values",
                ):
                    st.write(chunk["messages"][-1].content)
    
    with col2:
        st.header("Prueba de Nuevo Pedido")
        st.code('''user_query = "customer_id: customer_14 : Deseo realizar un pedido del item_51 con cantidad 4 y envío nacional"''', language='python')
        if st.button("Ejecutar Prueba de Pedido"):
            user_query = "customer_id: customer_14 : Deseo realizar un pedido del item_51 con cantidad 4 y envío nacional"
            st.write("Resultado:")
            with st.spinner("Procesando..."):
                for chunk in agent.stream(
                    {"messages": [("user", user_query)]},
                    stream_mode="values",
                ):
                    st.write(chunk["messages"][-1].content)

    st.markdown("---")
    st.markdown("### Información del Sistema")
    st.markdown("""
    Este sistema utiliza IA para:
    - Categorizar consultas (Nuevo Pedido vs Cancelación)
    - Verificar disponibilidad de inventario
    - Calcular costos de envío
    - Procesar pagos
    - Gestionar cancelaciones
    """)

if __name__ == "__main__":
    main()