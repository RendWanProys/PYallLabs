# -*- coding: utf-8 -*-
"""
Мастер-файл всех работ по Python из GitHub (RendWanProys).
Объединяет проекты PyLab1, PyLab2, PY, Py3, Pandas, Py6, PyLab6-8, py7-8.
Каждый проект запускается со своей рабочей директорией (os.chdir),
поэтому все относительные пути к .csv/.txt/.npy/.pkl и пакетам работают без поломок.
"""

import argparse
import builtins
import contextlib
import json
import os
import sys
from pathlib import Path

PYTHON_WORKS_ROOT = Path(__file__).resolve().parent

if 'display' not in globals():
    def display(*objs):
        for obj in objs:
            print(obj)


@contextlib.contextmanager
def project_cwd(folder_name: str):
    prev_cwd = os.getcwd()
    proj_dir = (PYTHON_WORKS_ROOT / folder_name).resolve()
    os.chdir(proj_dir)
    added = False
    if str(proj_dir) not in sys.path:
        sys.path.insert(0, str(proj_dir))
        added = True
    try:
        yield proj_dir
    finally:
        os.chdir(prev_cwd)
        if added and str(proj_dir) in sys.path:
            sys.path.remove(str(proj_dir))


def _exec_ipynb(folder_name: str, nb_filename: str, default_inputs=None, pre_ns=None):
    nb_path = PYTHON_WORKS_ROOT / folder_name / nb_filename
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    ns = {'__name__': '__main__', 'display': display}
    if pre_ns:
        ns.update(pre_ns)
    orig_input = builtins.input
    inputs_iter = iter(default_inputs or [])
    if default_inputs is not None:
        def _mock_input(prompt=''):
            try:
                val = next(inputs_iter)
            except StopIteration:
                val = ''
            print(f'{prompt}{val}')
            return val
        builtins.input = _mock_input
    try:
        with project_cwd(folder_name):
            for i, cell in enumerate(nb.get('cells', [])):
                if cell.get('cell_type') != 'code':
                    continue
                code = ''.join(cell.get('source', [])).strip()
                if not code:
                    continue
                exec(compile(code, f'{folder_name}/{nb_filename}#cell_{i}', 'exec'), ns)
    finally:
        builtins.input = orig_input


def _exec_py(folder_name: str, rel_py: str, default_inputs=None):
    py_path = (PYTHON_WORKS_ROOT / folder_name / rel_py).resolve()
    code = py_path.read_text(encoding='utf-8')
    ns = {'__name__': '__main__', '__file__': str(py_path), 'display': display}
    orig_input = builtins.input
    inputs_iter = iter(default_inputs or [])
    if default_inputs is not None:
        def _mock_input(prompt=''):
            try:
                val = next(inputs_iter)
            except StopIteration:
                val = ''
            print(f'{prompt}{val}')
            return val
        builtins.input = _mock_input
    try:
        with project_cwd(folder_name):
            exec(compile(code, str(py_path), 'exec'), ns)
    finally:
        builtins.input = orig_input

# %% [PyLab1] PyLab1 — Основы Python и NumPy (кортежи, матрицы, списки, множества, словари)
def run_pylab1(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: PyLab1")
    print("=" * 60)
    _exec_py("PyLab1", "Main.py")


# %% [PyLab2] PyLab2 — Объектно-ориентированное программирование (ООП)
def run_pylab2(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: PyLab2")
    print("=" * 60)
    _exec_py("PyLab2", "OOP.py")


# %% [PY] PY — Работа с классами и модулем calendar
def run_py(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: PY")
    print("=" * 60)
    _exec_ipynb("PY", "notebook.ipynb")


# %% [Py3] Py3 — NumPy, файлы, пакет my_package и анализ VTB.csv
def run_py3(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: Py3")
    print("=" * 60)
    _exec_ipynb("Py3", "main.ipynb")
    _exec_py("Py3", "my_package/module1.py", default_inputs=None if interactive else ["Нефть"])
    _exec_py("Py3", "my_package/module2.py")


# %% [Pandas] Pandas — Работа с Series, DataFrame, очистка данных (VTB.csv, stocks.csv)
def run_pandas(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: Pandas")
    print("=" * 60)
    _exec_ipynb("Pandas", "1.3-3.2.ipynb")
    _exec_ipynb("Pandas", "boooooks.ipynb")


# %% [Py6] Py6 — Даты, расчёт стажа/зарплаты и графики matplotlib
def run_py6(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: Py6")
    print("=" * 60)
    _exec_ipynb("Py6", "notebook.ipynb", default_inputs=None if interactive else ["15.05.2019", "2", "10.01.2020", "01.06.2023"])


# %% [PyLab6-8] PyLab6-8 — Расчёты и кластеризация регионов (KMeans, Agglomerative, PCA)
def run_pylab6_8(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: PyLab6-8")
    print("=" * 60)
    _exec_ipynb("PyLab6-8", "Math.ipynb")
    from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
    from sklearn.metrics import silhouette_score
    import pandas as _pd
    _lab8_ns = {"KMeans": KMeans, "AgglomerativeClustering": AgglomerativeClustering, "DBSCAN": DBSCAN}
    # В исходном ноутбуке на GitHub отсутствовал блок вычисления results между ячейками 4 и 5
    nb_path = PYTHON_WORKS_ROOT / "PyLab6-8" / "Lab8_v4.ipynb"
    nb_cells = json.loads(nb_path.read_text(encoding="utf-8")).get("cells", [])
    with project_cwd("PyLab6-8"):
        _lab8_ns.update({"__name__": "__main__", "display": display})
        for _ci, _c in enumerate(nb_cells):
            if _c.get("cell_type") != "code": continue
            _code = "".join(_c.get("source", [])).strip()
            if not _code: continue
            if _ci == 5 and "results" not in _lab8_ns and "X_scaled" in _lab8_ns:
                _Xs = _lab8_ns["X_scaled"]
                _lab8_ns["results"] = _pd.DataFrame([
                    {"Метод": "KMeans", "Silhouette": silhouette_score(_Xs, _lab8_ns["labels_kmeans"])},
                    {"Метод": "Agglomerative", "Silhouette": silhouette_score(_Xs, _lab8_ns["labels_hierarchical"])},
                    {"Метод": "DBSCAN", "Silhouette": None},
                ])
            exec(compile(_code, f"PyLab6-8/Lab8_v4.ipynb#cell_{_ci}", "exec"), _lab8_ns)


# %% [py7-8] py7-8 — Доставка Olist (data/olist_*.csv) и классификация heart.csv
def run_py7_8(interactive: bool = False):
    print("\n" + "=" * 60)
    print("ПРОЕКТ: py7-8")
    print("=" * 60)
    _exec_ipynb("py7-8", "py7.ipynb")
    _exec_ipynb("py7-8", "py8.ipynb")
    _exec_py("py7-8", "task10.py")
    _exec_py("py7-8", "main.py")


# %% Запуск всех проектов или выбранного проекта по имени
PROJECTS_MAP = {
    "PyLab1": run_pylab1,
    "PyLab2": run_pylab2,
    "PY": run_py,
    "Py3": run_py3,
    "Pandas": run_pandas,
    "Py6": run_py6,
    "PyLab6-8": run_pylab6_8,
    "py7-8": run_py7_8,
}


def run_all(interactive: bool = False):
    for name, fn in PROJECTS_MAP.items():
        fn(interactive=interactive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Мастер-запуск всех Python-работ из GitHub")
    parser.add_argument("--project", choices=list(PROJECTS_MAP.keys()), help="Запустить только выбранный проект")
    parser.add_argument("--interactive", action="store_true", help="Разрешить ручной ввод input()")
    args = parser.parse_args()
    if args.project:
        PROJECTS_MAP[args.project](interactive=args.interactive)
    else:
        run_all(interactive=args.interactive)
