from setuptools import setup, find_packages

setup(
    name="etl_pipeline",
    version="0.1.0",
    description="End-to-End Data Pipeline with ETL and Machine Learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=1.0.0",
        "pandas>=2.0.3",
        "numpy>=1.24.3",
        "psycopg2-binary>=2.9.6",
        "scikit-learn>=1.3.0",
        "fastapi>=0.95.2",
        "uvicorn>=0.22.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
        "console_scripts": [
            "run-pipeline=etl.run_pipeline:main",
            "train-model=ml.train:main",
            "run-api=api.main:main"
        ]
    }
)
