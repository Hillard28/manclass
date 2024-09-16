#!/bin/bash
sudo rm -R code/env
python -m venv code/env
source code/env/bin/activate
python -m pip install --upgrade pip
python -m pip install numba scipy numpy pandas matplotlib statsmodels openpyxl pyarrow black