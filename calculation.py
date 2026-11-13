# EMI=(P X R X (1+R)**months) /((1+R)**months-1)
#R=Annual Rate /(12 x 100)

class LoanEMICalculator:
    
    def __init__(self,principal,annual_rate,months):
        self.principal =principal
        self.annual_rate = annual_rate
        self.months = months

        

    def validate(self):
        if self.principal <= 0:
            return "value of principal should be positive number"

        if self.annual_rate < 0:
            return "value of annual rate should be non-negative number"

        if self.months <= 0:
            return "value of months should be greater than zero"

        return True

    def calculate_EMI(self):
     
       R=self.annual_rate/(12*100)

       if R==0:
            return self.principal/self.months
       return self.principal * R *(1+R)**self.months / ((1+R)**self.months-1)

    
    

