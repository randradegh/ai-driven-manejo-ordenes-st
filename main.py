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
    
    # Introducción
    st.markdown("""
    Esta aplicación demuestra cómo utilizar LangGraph y LangChain para crear un sistema de gestión de pedidos 
    inteligente que puede manejar tanto nuevos pedidos como cancelaciones. El sistema utiliza GPT-4 para entender 
    las solicitudes en lenguaje natural y tomar decisiones basadas en el contexto.
    """)
    
    # Explicación de las librerías
    st.markdown("### 🛠️ Librerías Principales")
    st.markdown("""
    - **LangGraph**: Framework para crear flujos de trabajo complejos con LLMs
    - **LangChain**: Biblioteca para construir aplicaciones con LLMs
    - **OpenAI GPT-4**: Modelo de lenguaje para procesamiento de lenguaje natural
    - **Streamlit**: Framework para crear interfaces web
    
    ```python
    from langgraph.graph import StateGraph, MessagesState
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    ```
    """)
    
    # Explicación del Workflow
    st.markdown("### 🔄 Flujo de Trabajo")
    st.markdown("""
    El flujo de trabajo se crea usando `create_workflow()`, que define:
    
    1. **Nodos del grafo**:
    ```python
    workflow.add_node("RouteQuery", categorize_query)      # Categoriza la consulta
    workflow.add_node("CheckInventory", check_inventory)   # Verifica inventario
    workflow.add_node("ComputeShipping", compute_shipping) # Calcula envío
    workflow.add_node("ProcessPayment", process_payment)   # Procesa pago
    ```
    
    2. **Conexiones condicionales**:
    ```python
    workflow.add_conditional_edges(
        "RouteQuery",
        route_query_1,
        {
            "PlaceOrder": "CheckInventory",    # Si es nuevo pedido
            "CancelOrder": "CancelOrder"       # Si es cancelación
        }
    )
    ```
    """)
    
    # Explicación del Agente
    st.markdown("### 🤖 El Agente IA")
    st.markdown("""
    El agente se crea compilando el flujo de trabajo:
    ```python
    agent = create_workflow()
    ```
    
    Este agente puede:
    - Entender consultas en lenguaje natural
    - Tomar decisiones basadas en el contexto
    - Manejar múltiples pasos en el proceso
    - Mantener el estado de la conversación
    """)

    st.markdown("---")
    
    # Load environment variables
    load_dotenv()
    
    # Create the workflow
    agent = create_workflow()
    
    # Explicación de las Pruebas
    st.markdown("### 🧪 Pruebas del Sistema")
    st.markdown("""
    El sistema incluye dos pruebas que demuestran sus capacidades principales:
    """)
    
    # Crear dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("1️⃣ Prueba de Cancelación")
        st.markdown("""
        Esta prueba simula la cancelación de un pedido existente:
        - Identifica la intención de cancelación
        - Extrae el ID del pedido
        - Procesa la solicitud de cancelación
        """)
        st.code('''user_query = "Deseo cancelar el pedido con order_id 223"''', language='python')
        if st.button("Ejecutar Prueba de Cancelación"):
            user_query = "Deseo cancelar el pedido con order_id 223"
            st.write("🔍 Resultado:")
            with st.spinner("Procesando..."):
                for chunk in agent.stream(
                    {"messages": [("user", user_query)]},
                    stream_mode="values",
                ):
                    st.write(chunk["messages"][-1].content)
    
    with col2:
        st.header("2️⃣ Prueba de Nuevo Pedido")
        st.markdown("""
        Esta prueba simula la creación de un nuevo pedido:
        - Identifica los detalles del pedido
        - Verifica disponibilidad
        - Calcula costos de envío
        - Procesa el pago
        """)
        st.code('''user_query = "customer_id: customer_14 : Deseo realizar un pedido del item_51 con cantidad 4 y envío nacional"''', language='python')
        if st.button("Ejecutar Prueba de Pedido"):
            user_query = "customer_id: customer_14 : Deseo realizar un pedido del item_51 con cantidad 4 y envío nacional"
            st.write("🔍 Resultado:")
            with st.spinner("Procesando..."):
                for chunk in agent.stream(
                    {"messages": [("user", user_query)]},
                    stream_mode="values",
                ):
                    st.write(chunk["messages"][-1].content)

    st.markdown("---")
    st.markdown("### 📊 Resumen del Sistema")
    st.markdown("""
    Este sistema demuestra cómo la IA puede:
    - 🔍 Categorizar consultas automáticamente
    - 📦 Verificar disponibilidad de inventario en tiempo real
    - 🚚 Calcular costos de envío dinámicamente
    - 💳 Procesar pagos de forma segura
    - ❌ Gestionar cancelaciones eficientemente
    
    Cada paso utiliza GPT-4 para entender el contexto y tomar decisiones apropiadas.
    """)

if __name__ == "__main__":
    main()