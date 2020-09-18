class local:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def mover(selfa,deltax,deltay):
        return local(self.x+deltax,self.y+deltay)
    def qualx(self):
        return self.x
    def qualy(self):
        return self.y
    def distde(self,other):
        ox, oy = other.x, other.y
        xdist, ydist = self.x - ox, self.y - oy
        return (xdist**2 + ydist**2)**0.5
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
class campo:
    def __init__(self):
        self.bebados={}
    def addbebado(self,bebado,loc):
        if bebado in self.bebados:
            raise ValueError('Bêbado duplicado')
        else:
            self.bebados[bebado]=loc
    def moverbebado(self,drunk):
        if bebado not in self.bebados:
            raise ValueError('Bebado inexistente')
        xdist,ydist=bebado.darpasso()
        locatual=self.bebados[bebado]
        self.bebados[bebado]=locatual.mover(xdist,ydist)
    def qualloc(self,bebado):
        if bebado not in self.bebados:
            raise ValueError('Bebado inexistente')
        return self.bebados[bebado]
        
        
