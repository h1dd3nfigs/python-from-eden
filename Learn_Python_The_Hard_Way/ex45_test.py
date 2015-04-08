'''
#SO suggestion on how to instantiate an object using string as object name

class idClasses:
    pass
    #class ID12345:pass
    #class ID01234:pass
# could also be: import idClasses

class ProcessDirector:
    def __init__(self):
        self.allClasses = []

    def construct(self, builderName):
        targetClass = getattr(idClasses, builderName)
        instance = targetClass()
        self.allClasses.append(instance)
 
IDS = ["ID12345", "ID01234"]

director = ProcessDirector()
for id in IDS:
    director.construct(id)

print director.allClasses
'''
