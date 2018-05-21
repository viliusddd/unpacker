import os
import re
import shutil
from sys import argv
#import pprint

class Unpack():
    def __init__(self):
        self.path = argv[1]
        self._tmp = "_tmp"
        self._new = "_zip"
        self.objectsList = []
        self.exceptionsList = {}

    def __deep_folder(self):
        b = [os.path.join(self.path,p) for p in os.listdir(self.path)]
        return b

    def __deepest_folder(self):
        fldr_lst = []
        for folder in self.__deep_folder():
            for item in os.listdir(folder):
                fldr_lst.append(os.path.join(folder,item))
        return fldr_lst

    def items(self):
        items = []
        for folder in self.__deepest_folder():
            for item in os.listdir(folder):
                items.append(os.path.join(folder, item))
        return items

    def aPath(self, path):
        a = []
        for i in os.listdir(self.path):
            a.append(os.path.join(self.path, i))
        if path == "abs":
            return a
        else:
            return os.listdir(self.path)

    def subPath(self, path):
        a = []
        b = []
        for i in self.aPath(path="abs"):
            for f in os.listdir(os.path.join(self.path, i)):
                a.append(os.path.join(self.path,i, f))
                b.append(f)
        if path == "abs":
            return a
        else:
            return b

    def subSubPath(self, path):
        a = []
        b = []
        for i in self.subPath(path="abs"):
            for f in os.listdir(os.path.join(self.path, i)): 
                    a.append(os.path.join(self.path, i, f))
                    print(os.path.join(self.path, i, f))
                    b.append(f)
        if path == "abs":
            return a
        else:
            return b

    def subSubPathTmp(self, path):
        a = []
        b = []
        for i in self.subPath(path="abs"):
            for f in os.listdir(os.path.join(self.path + self._tmp, i)): 
                    a.append(os.path.join(self.path, i, f))
                    print(os.path.join(self.path, i, f))
                    b.append(f)
        if path == "abs":
            return a
        else:
            return b

    def ifDoesNotExist(self, pathA, pathZ):
        if not os.path.exists(pathZ):
            os.makedirs(pathZ)
            shutil.copy2(pathA, pathZ)
        return(pathA, pathZ)

    def ifExists(self, pathA, pathZ):
        if os.path.exists(pathZ):
            if not os.path.isfile(os.path.join(pathZ, os.path.basename(pathA))):
                shutil.copy2(pathA, pathZ)
        return(pathA, pathZ)

    def remRep(self, item):
        # removes duplicates in a list
        item = list(set(item))
        item = list(item)
        return item

    def oneDeep(self):
        return os.listdir(self.path)

    def twoDeep(self, path):
        for subPath in (os.listdir(os.path.join(self.path, path))):    
            for subSubPath in os.listdir(os.path.join(self.path, path, subPath)):
                fullPath = os.path.join(self.path, path, subPath, subSubPath)
                
                self.__checkRules(fullPath, subPath)
                #self.__rename(path, name)

    def __checkRules(self, fullPath, subPath):
        rule = self.regex(fullPath) 
        if rule:
            self.objectsList.append(rule)
            endPath = os.path.join(self.path + self._tmp, path, rule, subPath)
            self.ifDoesNotExist(fullPath, endPath)
            self.ifExists(fullPath, endPath)

        if not rule:
            if fullPath not in self.exceptionsList.keys():
                self.exceptionsList[fullPath] = [subPath]    
            if fullPath in self.exceptionsList.keys():
                pass
                #print("wtf", fullPath)

    def exceptions(self, subPath):
        for exception, subSubPath in self.exceptionsList.items():
            objectsList = self.remRep(self.objectsList)
            for obj in objectsList:
                    print(os.path.join(self.path+self._tmp, subPath, obj, subSubPath[0]))
                    shutil.copy2(exception, os.path.join(self.path + self._tmp, subPath, obj, subSubPath[0]))

    def archive(self, path):
        items = os.path.join(self.path + self._tmp, path)
        for item in os.listdir(items):
            archivePath = os.path.join(self.path + self._new, path, item)
            if not os.path.exists(archivePath):
                os.makedirs(archivePath)
            else:
                pass
            for subItem in os.listdir(os.path.join(self.path + self._tmp, path, item)):
                if os.path.exists(archivePath+".zip"):
                    pass
                if not os.path.exists(archivePath+".zip"):
                    pass
                    shutil.make_archive(archivePath+"/"+subItem, "zip", os.path.join(self.path + self._tmp, path, item), subItem)

    def deleteTemp(self):
        shutil.rmtree(self.path+self._tmp)

    def rename(self, path, name):
        items = os.path.join(self.path + self._tmp, path)
        for item in os.listdir(items):
            archivePath = os.path.join(self.path + self._tmp, path, item)
            if not os.path.exists(os.path.join(self.path + self._tmp, path, name+item)):
                shutil.move(archivePath, os.path.join(self.path + self._tmp, path, name+item))
            else:
                pass

    def rename2(self, path, name):
        items = os.path.join(self.path + self._tmp, path)
        for item in os.listdir(items):
            for subItem in os.listdir(os.path.join(self.path + self._tmp, path,item)):    
                archivePath = os.path.join(self.path + self._tmp, path, item, subItem)
                if not os.path.exists(os.path.join(self.path + self._tmp, path, item, name+subItem)):
                    shutil.move(archivePath, os.path.join(self.path + self._tmp, path, item, name+subItem))
                else:
                    pass
                
    def regex(self, items):
        items = os.path.basename(items)
        regex = re.compile(r"D3D-P-HOS-(\d\d).*?\...*")
        a = re.search(regex, items)
        if a:
            return(a.group(1))
                    

test = Unpack()

for path in test.oneDeep():
    print(path, len(os.listdir(os.path.join(test.path, path))))
    test.twoDeep(path)
    test.exceptions(path)
    
    test.rename(path, "Test-Models-Package-Vol1-")
    test.rename2(path, "Test-Models-Package-Vol1-")
    
    test.exceptionsList = {}
    test.objectsList = []
    
    test.archive(path)

test.deleteTemp()

