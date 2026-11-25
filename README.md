# PythonWorks — Единое собрание всех Python-проектов с GitHub (`RendWanProys`)

Все работы разложены по исходным папкам проектов со всеми файлами данных (`.csv`, `.txt`, `.npy`, `.pkl`, пакеты, подпапки `data/`), а также объединены в общие мастер-файлы.

## Содержимое папок
- `PyLab1/` — `Main.py` (одномерные и двумерные массивы, NumPy, множества, словари)
- `PyLab2/` — `OOP.py` (классы, наследование, полиморфизм)
- `PY/` — `notebook.ipynb` (класс `Date`, работа с `calendar`)
- `Py3/` — `main.ipynb`, `my_package/` (`module1.py`, `module2.py`), `VTB.csv`, `vtb_merged_prices.npy`, `text_input.txt`, `tovar_input.txt`
- `Pandas/` — `1.3-3.2.ipynb`, `boooooks.ipynb`, `VTB.csv`, `VTB_dirty.csv`, `stocks.csv`, `vtb_merged_prices.npy`
- `Py6/` — `notebook.ipynb` (расчёт стажа, оплата больничного, графики `matplotlib`)
- `PyLab6-8/` — `Math.ipynb`, `Lab8_v4.ipynb`, `data.csv`, `cluster_mpg.csv`, `cluster_mpg_results.csv`, `regions_clusters.csv`
- `py7-8/` — `py7.ipynb`, `py8.ipynb`, `task10.py`, `main.py`, `heart.csv`, `best_model.pkl`, `data/olist_*.csv`

## Мастер-файлы
- `Master_All_Python_Works.ipynb` — единый Jupyter-ноутбук со всеми проектами и автоматическим переключением рабочей директории (`use_project(...)`), чтобы относительные пути к файлам не ломались.
- `master.py` — единый Python-скрипт (с `# %%`-ячейками и CLI-запуском):
  - Запустить все работы: `python master.py`
  - Запустить конкретный проект: `python master.py --project py7-8`
  - Запустить с ручным вводом (`input()`): `python master.py --project Py6 --interactive`
