class Integer(object):
        def __init__(self,number, f):
            self.number=number
            self.f=f
	def display(self):
		if f==False:
		    	print number*-1
    		else:
		      	print number
class NegativeInteger(Integer): 
	def __init__(self, number):
       		Integer.__init__(self, number, False)    
        def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"
L
if __name__=="__main__":
    test=Integer(100,true)
     test.display()
    test=NegativeNumber(9)
