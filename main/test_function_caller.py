import pytest

import logging

from function_caller import FunctionCaller

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d:\t%(message)s', datefmt='%I:%M:%S')

#pipenv run pytest

def returner():
    return True


def test_addFunction():
    caller = FunctionCaller('testCallerName')
    caller.addFunction('returnerFunctionName',returner)
    assert 'returnerFunctionName' in caller.getFunctionDict()

def test_addNonFunction():
    caller = FunctionCaller('testCallerName')
    with pytest.raises(TypeError):
        caller.addFunction('returnerFunctionName','str')

def test_addNonStrKeyFunction():
    caller = FunctionCaller('testCallerName')
    with pytest.raises(TypeError):
        caller.addFunction(1,'str')
        
def test_runNonExistantFunction(caplog):
    caller = FunctionCaller('testCallerName')
    assert caller.runFunction('returnerFunctionName') == None
    
def test_runNonExistantFunctionProcessor():
    caller = FunctionCaller('testCallerName')
    extname = ''
    def nameProcessor(name:str,arg1):
        nonlocal extname
        extname = name
        assert arg1 == 1
        assert name == 'unknownFunctionName'
    caller.unknownFunctionProcessor = nameProcessor
    caller.runFunction('unknownFunctionName',1) 
    assert extname == 'unknownFunctionName'

def test_runFunctionNoArgs():
    caller = FunctionCaller('testCallerName')
    extvar = 0
    def function():
        nonlocal extvar
        extvar = 1
    caller.addFunction('testFunction', function)
    caller.runFunction('testFunction') 
    assert extvar == 1

def test_runFunctionPositionalArgs():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2,arg3):
        nonlocal extvar1,extvar2,extvar3
        extvar1 = arg1
        extvar2 = arg2
        extvar3 = arg3        
    caller.addFunction('testFunction', function)
    caller.runFunction('testFunction',1,2,3) 
    assert extvar1 == 1 and extvar2 == 2 and extvar3==3

def test_runFunctionAndReturns():
    caller = FunctionCaller('testCallerName')
    def function():
        return 1
    caller.addFunction('testFunction', function)
    assert caller.runFunction('testFunction') == 1

def test_runFunctionException():
    caller = FunctionCaller('testCallerName')
    def function():
        a=1/0
    caller.addFunction('testFunction', function)
    assert caller.runFunction('testFunction') == None

def test_runFunctionExceptionProcessor():
    caller = FunctionCaller('testCallerName')
    def function():
        a=1/0
    caller.addFunction('testFunction', function)
    extName = ''
    extException = ''
    def checkException(name, exc):
        nonlocal extName,extException
        extName = name
        extException = str(exc)
    caller.functionErrorProcessor=checkException
    caller.runFunction('testFunction') 
    assert extName == 'testFunction' and extException == 'division by zero'


def test_runFunctionPositionalArgsTooManyArgs():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2):
        nonlocal extvar1
        extvar1 = 1
        assert False
        return 1
    caller.addFunction('testFunction', function)
    res = caller.runFunction('testFunction',1,2,3) 
    assert res == None
    assert extvar1 == 0

def test_runFunctionNamedArgs():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2,arg3):
        nonlocal extvar1,extvar2,extvar3
        extvar1 = arg1
        extvar2 = arg2
        extvar3 = arg3        
    caller.addFunction('testFunction', function)
    caller.runFunction('testFunction',arg2=2,arg1=1,arg3=3) 
    assert extvar1 == 1 and extvar2 == 2 and extvar3==3

def test_runFunctionNamedArgsUnknown():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2):
        nonlocal extvar1,extvar2,extvar3
        extvar1 = arg1
        extvar2 = arg2
        assert False
    caller.addFunction('testFunction', function)
    res = caller.runFunction('testFunction',arg2=2,arg1=1,arg3=3) 
    assert res == None
    assert extvar1 == 0 and extvar2 == 0 and extvar3==0


def test_runFunctionNamedArgsUnknown():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2):
        nonlocal extvar1,extvar2,extvar3
        extvar1 = arg1
        extvar2 = arg2
        assert False
    caller.addFunction('testFunction', function)
    res = caller.runFunction('testFunction',arg2=2,arg1=1,arg3=3) 
    assert res == None
    assert extvar1 == 0 and extvar2 == 0 and extvar3==0

def test_runFunctionErrorProcessor():
    caller = FunctionCaller('testCallerName')
    extvar1 = 0
    extvar2 = 0
    extvar3 = 0
    def function(arg1,arg2):
        nonlocal extvar1,extvar2,extvar3
        extvar1 = arg1
        extvar2 = arg2
        assert False
    caller.addFunction('testFunction', function)
    res = caller.runFunction('testFunction',arg2=2,arg1=1,arg3=3) 
    assert res == None
    assert extvar1 == 0 and extvar2 == 0 and extvar3==0


def test_removeFunction():
    caller = FunctionCaller('testCallerName')
    def empty():
        pass
    caller.addFunction('emptyFunctionName',empty)
    caller.removeFunction('emptyFunctionName')
    assert 'emptyFunctionName' not in caller.getFunctionDict()

def test_removeNonExistantFunction():
    caller = FunctionCaller('testCallerName')
    with pytest.raises(KeyError):
        caller.removeFunction('function')


