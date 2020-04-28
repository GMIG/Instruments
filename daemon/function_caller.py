
import functools
import logging
import typing
import inspect
from types import MappingProxyType
from typing import Callable, List, NoReturn, Mapping, FrozenSet, Any, TypeVar

def compose(*functions: Callable):
    E = TypeVar('E')

    def compose2(f: Callable[[Any], E], g: Callable[[E], Any]):
        return lambda x: f(g(x))
    return functools.reduce(compose2, functions, lambda x: x)

class FunctionCaller:
    
    def __init__(self, name: str, functions: typing.Dict[str, Callable] = None):
        self.name = name
        if functions is None:
            self.__functions = {}
        else:
            self.__functions = functions
            
    def __getFunctionFullName(self,functionName: str):
        return 'function ' + self.name + '.' + str(functionName)

    def runFunction(self, functionName: str, *args, **kwargs) -> [NoReturn,str]:
        if functionName not in self.__functions:
            logging.debug(self.__getFunctionFullName(functionName) + ' not found - skipping')
        else:
            try:
                logging.debug('running ' + self.__getFunctionFullName(functionName) + " args " + str(args).strip("(,)") + str(kwargs).strip("{}"))
                logging.debug(inspect.signature(self.__functions[functionName]).parameters)
                if len(inspect.signature(self.__functions[functionName]).parameters) > 0:
                    return self.__functions[functionName](*args, **kwargs)
                else:
                    return self.__functions[functionName]()
            except Exception as e:
                logging.debug(self.__getFunctionFullName(functionName) + ' returned exception \'' + str(e) + '\'')
                        
    def addFunction(self, functionName: str, function: Callable) -> NoReturn:
        logging.debug(self.__getFunctionFullName(functionName) + ' added')
        self.__functions[functionName] = function

    def removeFunction(self, functionName: str) -> NoReturn:
        self.__functions.pop(functionName)

    def getFunction(self) -> Mapping[str, Callable]:
        return MappingProxyType(self.__function)

    # if on_NAME(Listener) is accessed, under NAME listener is added
    # If no class attribute is found, and the object’s class has a __getattr__() method, that is called to satisfy the lookup.
    def __getattr__(self, name: str):
        if name[0:3] == "on_":
            def function_name(function: Callable) -> NoReturn:
                self.addFunction(name[3:], function)
            return function_name
        else:
            raise AttributeError
