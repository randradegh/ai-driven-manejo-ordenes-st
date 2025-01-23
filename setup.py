from setuptools import setup, find_packages

setup(
    name="order_management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langgraph",
        "langchain-openai",
        "pandas",
        "python-dotenv",
        "ipython"
    ]
) 