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
ai-driven-order-management/
├── data/
│   ├── inventory.csv      # Sample inventory data
│   └── customers.csv      # Sample customer data
├── src/
│   ├── __init__.py
│   ├── config.py         # Shared configuration and LLM setup
│   ├── main.py           # Entry point
│   ├── tools.py          # LangChain tools
│   ├── nodes.py          # Workflow nodes
│   ├── state.py          # State definitions
│   └── workflow.py       # Workflow graph definition
├── requirements.txt
├── setup.py
└── README.md
```

## Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/schmitech/ai-driven-order-management.git
cd ai-driven-order-management
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
pip install -e .
```

4. Crear un archivo `.env` en el directorio raíz y añadir tu clave API de OpenAI:
```
OPENAI_API_KEY=tu_clave_api_aquí
```

Nota: Asegúrate de tener acceso a GPT-4 Turbo ya que el sistema utiliza el modelo `gpt-4-turbo-preview`.

## Ejecutar la Aplicación

Ejecuta la aplicación Streamlit desde el directorio raíz del proyecto:

```bash
streamlit run main.py
```

La aplicación ejecutará dos casos de prueba:
1. Cancelación de pedido: "Deseo cancelar el pedido con order_id 223"
2. Nuevo pedido: "customer_id: customer_14 : Deseo realizar un pedido del item_51 con cantidad 4 y envío nacional"

## Cómo Funciona

El sistema utiliza un flujo de trabajo basado en grafos con varios componentes clave:

### 1. Configuración
- Configuración centralizada en `config.py`
- Gestión de variables de entorno
- Instancia LLM compartida usando GPT-4 Turbo

### 2. Gestión de Estado
- Rastrea detalles del pedido, estado del inventario, costos de envío y estado del pago
- Mantiene el historial de conversación y el progreso del flujo de trabajo

### 3. Nodos del Flujo de Trabajo
- `categorize_query`: Determina la intención del usuario (nuevo pedido/cancelación)
- `check_inventory`: Verifica la disponibilidad del artículo
- `compute_shipping`: Calcula costos de envío basados en ubicación y peso
- `process_payment`: Simula el procesamiento del pago
- `cancel_order`: Maneja las solicitudes de cancelación de pedidos

### 4. Lógica Condicional
- Dirige las solicitudes a los manejadores apropiados según la intención del usuario
- Gestiona la ramificación del flujo de trabajo para diferentes escenarios

## Datos de Muestra

### Datos de Inventario
El sistema incluye datos de muestra de inventario con:
- IDs de artículos
- Niveles de stock
- Pesos de artículos
- Precios

### Datos de Clientes
Los datos de muestra de clientes incluyen:
- IDs de clientes
- Ubicaciones (local/nacional/internacional)
- Información de contacto

## Limpieza del Proyecto

Este script asegura una instalación limpia eliminando todos los archivos compilados de Python, artefactos de construcción y el entorno virtual antes de crear una configuración nueva.

```bash
# Hacer el script ejecutable
chmod +x clean.sh

# Ejecutar el script de limpieza
./clean.sh
```

## Contribuir

Siéntete libre de enviar issues, hacer fork del repositorio y crear pull requests para cualquier mejora.

## Licencia

[Apache 2.0](LICENSE)

## Agradecimientos

Este proyecto utiliza:
- [LangGraph](https://www.langchain.com/langgraph) para la orquestación del flujo de trabajo
- [LangChain](https://www.langchain.com/) para la integración con LLM
- [Streamlit](https://streamlit.io/) para la interfaz web
- OpenAI GPT-4 Turbo para el procesamiento del lenguaje natural