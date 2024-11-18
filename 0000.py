#!/usr/bin/env python
"""Lang Identify.

Indentifying  a system language configuration.

Usage: 

Have the LANG variable properly configured:

    export LANG=pt_BR

Execution:

    python 0000.py
    or
    ./0000.py
    or
    LANG=pt_BR.utf8 python 0000.py
"""
__version__ = "0.0.1"
__author__ = "Lcspires"
__licence__ = "Unlicense"

import os

current_language  = os.getenv("LANG", "en_US")[:5]

if current_language == ("en_US"):
    print("Hello, friend.")
elif current_language == ("pt_BR"):
    print("Olá, garoto!")
    
#Respect the PEP 8.
