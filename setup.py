from setuptools import setup, find_packages

setup(
    name="order_management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.1.0",
        "langgraph>=0.0.15",
        "langchain-openai>=0.0.2.post1",
        "pandas",
        "python-dotenv",
        "ipython",
        "streamlit"
    ]
) 