from pkgutil import iter_modules
from inspect import getmembers
import importlib

public_functions = []
for _, module_name, _ in iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    public_functions.extend([f"{module_name}.{m_name}" 
                             for m_name, _ in getmembers(module) 
                             if m_name.startswith('part_') or m_name == 'DAY'])

__all__ = public_functions
