from pyclbr import Function
from typing import Dict, List
import requests
import numpy as np

def getData(modelname):
        resp = requests.get("http://typelias.se:7575/fetch/" + modelname+ ".json")
        data = resp.json()
        return data


def getResultMap(modelData, isWer):
        dataPoint = 'commandWers' if isWer else 'commandTimes'
        return modelData[dataPoint]

def fetchResultMap(modelname, isWer):
        data = getData(modelname)
        return getResultMap(data, isWer)

def getAvg(input: Dict[str, List[float]]) -> np.ndarray:
        l = []
        for _, v in input.items():
            arr = np.array(v)
            l.append(np.mean(arr))
        l.append(l.pop(0))
        return np.array(l)

def getMin(input: Dict[str, List[float]]) -> np.ndarray:
        l = []
        for _, v in input.items():
            arr = np.array(v)
            l.append(np.min(arr))
        l.append(l.pop(0))
        return np.array(l)

def getMax(input: Dict[str, List[float]]) -> np.ndarray:
        l = []
        for _, v in input.items():
            arr = np.array(v)
            l.append(np.max(arr))
        l.append(l.pop(0))
        return np.array(l)

def getStd(input: Dict[str, List[float]]) -> np.ndarray:
        l = []
        for _, v in input.items():
            arr = np.array(v)
            l.append(np.std(arr))
        l.append(l.pop(0))
        return np.array(l)
            
def getCommandWERForModels(models: List[str], metricFunction: Function, commandIndex) -> np.ndarray:
        l = []
        for model in models:
            l.append(metricFunction(fetchResultMap(model, True))[commandIndex])
        return np.array(l)*100

