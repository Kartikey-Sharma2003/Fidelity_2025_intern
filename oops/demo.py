from abc import *
class Printer(ABC):
    @abstractmethod
    def  printing(self,text):
        pass
    
class HP(Printer):
    def printing(self,text):
        return "hp printing"        

    
