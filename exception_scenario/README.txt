Run access.py

This is a highly specific code example which is hacked down as much as possible from the original code.
The System.AccessViolationException on the exit (alternatively pythonnet.unload()) is hard to reproduce because the reason of it most certainly is some memory access/reclaims by the Python process which are not directly controllable.
Multiple factors could influence the occurence of an exception. E.g. in the original code, it did not matter whether netcore or netframework was loaded. The exception was thrown anyway. But here, it matters again.

The DLL in piweb_formplots folder is from this project: https://github.com/ZEISS-PiWeb/PiWeb-Formplots

This code example crashed reliably on my machine at least. However, any changes like Python 3.10 or higher did not throw the exception. But this does not mean there is an issue with Python 3.9.

Windows 11
Python 3.9

The conda environment used:
ca-certificates           2024.3.11            haa95532_0
cffi                      1.16.0                   pypi_0    pypi
clr-loader                0.2.6                    pypi_0    pypi
openssl                   3.0.13               h2bbff1b_1
pip                       24.0             py39haa95532_0
pycparser                 2.22                     pypi_0    pypi
python                    3.9.19               h1aa4202_1
pythonnet                 3.0.3                    pypi_0    pypi
setuptools                69.5.1           py39haa95532_0
sqlite                    3.45.3               h2bbff1b_0
tzdata                    2024a                h04d1e81_0
vc                        14.2                 h2eaa2aa_1
vs2015_runtime            14.29.30133          h43f2093_3
wheel                     0.43.0           py39haa95532_0
