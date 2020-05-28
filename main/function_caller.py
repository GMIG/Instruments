
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
        def nulProcesor(name:str , *args, **kwargs):
            pass
        self.unknownFunctionProcessor:Callable = nulProcesor
        self.functionErrorProcessor:Callable = nulProcesor
        
    def __getFunctionFullName(self,functionName: str):
        return self.name + '.' + str(functionName)

    def __formatArgs(self,*args, **kwargs):
        return '(' + str(args).strip("(,)") + str(kwargs).strip("{}") + ')'

    def __getFunctionCallWithArgs(self,functionName: str,*args, **kwargs):
        return self.__getFunctionFullName(functionName) + self.__formatArgs(*args, **kwargs)

    def runFunction(self, functionName: str, *args, **kwargs) :
        if functionName not in self.__functions:
            logging.debug(self.__getFunctionCallWithArgs(functionName,*args, **kwargs) + ' run but not processed')
            try:
                self.unknownFunctionProcessor(functionName,*args, **kwargs)
            except Exception as e:
                logging.debug(self.name + ' unknown function processor ' + ' returned error ' + str(e))
        else:
            try:
                logging.debug(self.__getFunctionCallWithArgs(functionName,*args, **kwargs) + ' running')
                if len(inspect.signature(self.__functions[functionName]).parameters) > 0:
                    res = self.__functions[functionName](*args, **kwargs)
                else:
                    res = self.__functions[functionName]()
                if res!=None:
                    logging.debug(self.__getFunctionCallWithArgs(functionName,*args, **kwargs) + ' returned ' + str(res))
                return res
            except Exception as e:
                logging.debug(self.__getFunctionCallWithArgs(functionName,*args, **kwargs) + ' returned exception \'' + str(e) + '\'')
                try:
                    self.functionErrorProcessor(functionName,e, *args, **kwargs)
                except Exception as e:
                    logging.debug(self.name + ' function error processor ' + ' returned error ' + str(e))
        
    def addFunction(self, functionName: str, function: Callable) -> NoReturn:
        if not(isinstance(functionName, str) and callable(function)):
            raise TypeError(self.name + ' error in types of added function arguments')
        logging.debug(self.__getFunctionFullName(functionName) + ' added')
        self.__functions[functionName] = function

    def removeFunction(self, functionName: str) -> NoReturn:
        self.__functions.pop(functionName)
        logging.debug(self.__getFunctionFullName(functionName) + ' removed')

    def getFunctionDict(self) -> Mapping[str, Callable]:
        return MappingProxyType(self.__functions)

    # if on_NAME(Listener) is accessed, under NAME listener is added
    # If no class attribute is found, and the object’s class has a __getattr__() method, that is called to satisfy the lookup.
    def __getattr__(self, name: str):
        if name[0:3] == "on_":
            def function_name(function: Callable) -> NoReturn:
                self.addFunction(name[3:], function)
            return function_name
        else:
            raise AttributeError
