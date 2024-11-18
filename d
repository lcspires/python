[1mdiff --git a/0000.py b/0000.py[m
[1mindex e0cbec9..c8832fa 100644[m
[1m--- a/0000.py[m
[1m+++ b/0000.py[m
[36m@@ -1,3 +1,33 @@[m
 #!/usr/bin/env python[m
[32m+[m[32m"""Lang Identify.[m
 [m
[31m-print("Hello, friend.")[m
[32m+[m[32mIndentifying  a system language configuration.[m
[32m+[m
[32m+[m[32mUsage:[m[41m [m
[32m+[m
[32m+[m[32mHave the LANG variable properly configured:[m
[32m+[m
[32m+[m[32m    export LANG=pt_BR[m
[32m+[m
[32m+[m[32mExecution:[m
[32m+[m
[32m+[m[32m    python 0000.py[m
[32m+[m[32m    or[m
[32m+[m[32m    ./0000.py[m
[32m+[m[32m    or[m
[32m+[m[32m    LANG=pt_BR.utf8 python 0000.py[m
[32m+[m[32m"""[m
[32m+[m[32m__version__ = "0.0.1"[m
[32m+[m[32m__author__ = "Lcspires"[m
[32m+[m[32m__licence__ = "Unlicense"[m
[32m+[m
[32m+[m[32mimport os[m
[32m+[m
[32m+[m[32mcurrent_language  = os.getenv("LANG", "en_US")[:5][m
[32m+[m
[32m+[m[32mif current_language == ("en_US"):[m
[32m+[m[32m    print("Hello, friend.")[m
[32m+[m[32melif current_language == ("pt_BR"):[m
[32m+[m[32m    print("Olá, garoto!")[m
[32m+[m[41m    [m
[32m+[m[32m#Respect the PEP 8.[m
