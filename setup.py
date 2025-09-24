from setuptools import setup, find_packages

setup(
    name="my-python-app",
    version="0.1.0",
    #package_data=find_packages(),
    include_package_data=True,

    install_requires=[
        "Flask==2.3.3",
        "pytest==7.4.2",
        "coverage"
    ],
    entry_points={                        # 🔹 Optional: Create CLI commands
        "console_scripts": [
            "my-app = my_app.main:main",  # my-app CLI runs main() from my_app/main.py
        ]
    },

    author="Ankit Sahni",                 # 🔹 Metadata for PyPI
    description="A sample Python web app",
    long_description=open("README.md").read(),          # Long description shown on PyPI
    long_description_content_type="text/markdown",      # Format of README file

    classifiers=[                         # 🔹 Trove classifiers (for PyPI, optional but useful)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.8',              # 🔹 Minimum Python version required

)