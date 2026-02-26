from setuptools import setup, find_packages

setup(
    name="reconforge",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "python-nmap",
        "requests",
        "fpdf2"
    ],
    entry_points={
        "console_scripts": [
            "reconforge=reconforge.cli:main"
        ]
    },
    author="Sanskar",
    description="Automated Recon & Vulnerability Fingerprinting CLI Tool",
)
