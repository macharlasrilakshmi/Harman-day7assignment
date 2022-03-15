def hello(func):
    print("Execute me First")
    func() 
    
@hello
def printname():
    print("sri")
