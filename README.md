# Automated Order Management System

A LangGraph-based order management system that can handle order placement and cancellation using AI agents. This system demonstrates how to build complex, multi-step workflows with Large Language Models (LLMs) using LangGraph.

Based on Kshitij Kutumbe's article [LangGraph AI agents : Building a Dynamic Order Management System : A Step-by-Step Tutorial](https://ai.gopubby.com/langgraph-building-a-dynamic-order-management-system-a-step-by-step-tutorial-0be56854fc91).

## Use Cases

- Intelligent query categorization (Place Order vs Cancel Order)
- Inventory availability checking
- Dynamic shipping cost calculation based on location and weight
- Payment processing simulation
- Order cancellation handling
- State management across the workflow
- Conditional branching based on user intent

## Prerequisites

- Python 3.8+
- OpenAI API key (GPT-4 Turbo access required)

## Project Structure

```
order_management/
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

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd order-management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key (copy template from .env.example):
```
OPENAI_API_KEY=your_api_key_here
```

Note: Make sure you have access to GPT-4 Turbo as the system uses `gpt-4-turbo-preview` model.

## Running the Application

Run the main script from the project root directory:

```bash
python -m src.main
```

This will run two test cases:
1. Canceling an order: "I wish to cancel order_id 223"
2. Placing a new order: "customer_id: customer_14 : I wish to place order for item_51 with order quantity as 4 and domestic"

## How It Works

The system uses a graph-based workflow with several key components:

### 1. Configuration
- Centralized configuration in `config.py`
- Environment variable management
- Shared LLM instance using GPT-4 Turbo

### 2. State Management
- Tracks order details, inventory status, shipping costs, and payment status
- Maintains conversation history and workflow progress

### 3. Workflow Nodes
- `categorize_query`: Determines user intent (place/cancel order)
- `check_inventory`: Verifies item availability
- `compute_shipping`: Calculates shipping costs based on location and weight
- `process_payment`: Simulates payment processing
- `cancel_order`: Handles order cancellation requests

### 4. Conditional Logic
- Routes requests to appropriate handlers based on user intent
- Manages workflow branching for different scenarios

## Sample Data

### Inventory Data
The system includes sample inventory data with:
- Item IDs
- Stock levels
- Item weights
- Prices

### Customer Data
Sample customer data includes:
- Customer IDs
- Locations (local/domestic/international)
- Contact information

## Customization

You can customize the system by:
1. Modifying the data in `data/*.csv` files
2. Adjusting shipping rates in `compute_shipping()`
3. Adding new workflow nodes in `nodes.py`
4. Extending the state definition in `state.py`

## Troubleshooting

Common issues and solutions:
1. **Import Errors**: Make sure to run the application from the project root directory using `python -m src.main`
2. **API Key Issues**: Ensure your .env file is in the root directory and contains the correct API key
3. **Model Access**: Verify you have access to GPT-4 Turbo in your OpenAI account
4. **JSON Parsing Errors**: Check the debug output if you encounter parsing issues in the cancel order flow

## Cleaning the Project

This script ensures a clean installation by removing all compiled Python files, build artifacts, and the virtual environment before creating a fresh setup.

```bash
# Make the script executable
chmod +x clean.sh

# Run the cleaning script
./clean.sh
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Apache 2.0](LICENSE)

## Acknowledgments

This project uses:
- [LangGraph](https://www.langchain.com/langgraph) for workflow orchestration
- [LangChain](https://www.langchain.com/) for LLM integration
- OpenAI's GPT-4 Turbo for natural language understanding 