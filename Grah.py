class vertex:
    def __init__(self,vertexID,x,y,label):
        self.x=x
        self.y=y
        self.ID=vertexID
        self.label=label
        self.adjacent=[]
        self.previous=None

    def __str__(self):
        print('<',str(self.x),str(self.y),'>')

class edge:
    def __init__(self,v1,v2,peso=0)
    self.v1=v1
    self.v2=v2
    self.peso=peso

    def __lt__:
        return self.weight<other.weight
    
