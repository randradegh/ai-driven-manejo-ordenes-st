# Sistema de Gestión de Pedidos con IA

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/🦜_LangChain-0.1.0-blue.svg)
![LangGraph](https://img.shields.io/badge/🔄_LangGraph-0.0.15-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI_GPT--4-turbo-orange.svg)

Un sistema de gestión de pedidos basado en LangGraph que puede manejar la creación y cancelación de pedidos utilizando agentes de IA. Este sistema demuestra cómo construir flujos de trabajo complejos y de múltiples pasos con Modelos de Lenguaje Grande (LLMs) usando LangGraph.

Basado en el artículo de Kshitij Kutumbe [LangGraph AI agents : Building a Dynamic Order Management System : A Step-by-Step Tutorial](https://ai.gopubby.com/langgraph-building-a-dynamic-order-management-system-a-step-by-step-tutorial-0be56854fc91).

## Casos de Uso

- Categorización inteligente de consultas (Nuevo Pedido vs Cancelación)
- Verificación de disponibilidad de inventario
- Cálculo dinámico de costos de envío basado en ubicación y peso
- Simulación de procesamiento de pagos
- Gestión de cancelaciones de pedidos
- Gestión de estado a través del flujo de trabajo
- Ramificación condicional basada en la intención del usuario

## Requisitos Previos

- Python 3.8+
- Clave API de OpenAI (se requiere acceso a GPT-4 Turbo)

## Estructura del Proyecto

```
ai-driven-order-management-st/
├── data/
│   ├── inventory.csv      # Datos de muestra del inventario
│   └── customers.csv      # Datos de muestra de clientes
├── src/
│   ├── __init__.py
│   ├── config.py         # Configuración compartida y configuración de LLM
│   ├── tools.py          # Herramientas de LangChain
│   ├── nodes.py          # Nodos del flujo de trabajo
│   ├── state.py          # Definiciones de estado
│   └── workflow.py       # Definición del grafo de flujo de trabajo
├── main.py               # Punto de entrada (Streamlit)
├── requirements.txt
├── setup.py
└── README.md
```

## Configuración

1. Iniciar un nuevo proyecto:
```bash
# Opción 1: Clonar el repositorio
git clone https://github.com/randradegh/ai-driven-manejo-ordenes-st.git
cd ai-driven-manejo-ordenes-st

# Opción 2: Iniciar desde cero
git init
git add .
git commit -m "Commit inicial"
git remote add origin https://github.com/randradegh/ai-driven-manejo-ordenes-st.git
git push -u origin main
```

2. Crear y activar un entorno virtual:
```