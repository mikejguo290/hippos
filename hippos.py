#hippos = 3

# Pablo Escobar's zoo started with 3 hippos in 1983 but there may have been more hippos
# in 1989 at time of Escobar's death.
#year = 1989
# Females takes 6 years to mature and reproduce.
# Hippos have a gestation period of eight months.
# after gestation. females will not reproduce for another 17 months - 1.5 years
# Each mother produces just one baby at one time normally.
# males take around 7.5 years to mature. although model can exclude this.

# assume 47:53 male to female ratios
# assume a lifespan of 45 - 50 years. more like 50 years in captivity or really good conditions

import time
import xlwt

from random import random
class hippo(object):
""" 
defines a hippo for this model.
"""
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender
        self.conceptionAge = 0 # conceptionAge is age when last conceived.
        
    def getOlder(self):
        self.age +=1
        
    def babyGenderGenerator(self):
    """
    randomly selects the sex of a baby hippo.
    """
        if(random()>0.53):
            return 'Male'
        else:
            return 'Female'
            
    def fertile(self):
    """
    Tests if a mother hippo is fertile. A female hippo can only give birth if it is >= 6 years old.
    A female hippo needs more than roughly 2 year between being able to reproduce. 
    """
        yearsSinceLastConceive = self.age - self.conceptionAge
        print "the hippo has had %d years since it last gave birth" % yearsSinceLastConceive # scaffold
        return (self.age>= 6) and (self.gender =='Female' and yearsSinceLastConceive > 2.0) 

        # 8 months pregnancy + 17 months with the baby = 25 months , roughly 2 years for a hippo to conceive again.  
    
    def reproduce(self):
    """
    generates a baby hippo.
    """          
        if self.fertile():
            print 'hippo is fertile'
            self.conceptionAge = self.age
            return hippo(-0.66,self.babyGenderGenerator())
        # baby hippo's ages is set to -0.66 at conception because gestation takes 8 months, which is 2/3 of 1 year.
        else:
            print 'no baby'

def liveOneYear(hippoPopulation):
    """
    takes in one herd. allow reproduction, ageing and death to occur. return that herd for next year.
    """
    for animal in hippoPopulation:
        baby = animal.reproduce()
        if isinstance(baby,hippo):
            # check baby is a hippo object rather noneType object. 
            hippoPopulation.append(baby) #the baby at time of conception os -8 months or -0.66 years old. 
        animal.getOlder()
        #print "hippo is %d years old."% animal.age
        #print "hippo is a %s." %animal.gender
        
        if animal.age > 45.0:
            print 'too old! leave the herd and this mortal coil'
            # remove the animal from the population. actually. all those hippos might be alive! since 1983.
            # DO NOTHING?###
    print "year over! \n"
    return hippoPopulation

#hippoPopulation= liveOneYear(hippoPopulation) #sometimes print and print destroys each other! whereas save to var + print is good.

def simulateOneRun(hippoPopulation, duration):
""" 
runs liveOnYear on hippoPopulation for duration in years. returns the size of hippoPopulation.
"""
    for i in range(duration): # 31 years!  1983 - 2014
        hippoPopulation= liveOneYear(hippoPopulation)
    return len(hippoPopulation) # hippoPopulationSize
        #time.sleep(10)
        
def outputToExcel(array,filename):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('pop dist 2014',cell_overwrite_ok=True)

    row = 0
    sheet.write(row,0,'population size')
    #sheet.write(row,1,'Index')

    row = 1
    for i in array:
        sheet.write(row,0,i)#names.decode('utf-8')
        #sheet.write(row,1,ind)
        row+=1
    
    workbook.save('%s.xls'% filename)


simRuns = 0 
dist = [] # records the outcomes of each simulation run in terms of hippos numbers. 
while simRuns < 10: # Max number of simulations runs
    hippoPopulation =[]
    #initialise the population in 1984, with three females and a male.
    for i in range(0,3):
        hippoPopulation.append(hippo(6.0,'Female')) 
    a= simulateOneRun(hippoPopulation, 31)
    dist.append(a)
    simRuns +=1
filename = "hippo's population dist 2014 6 years to maturity"
outputToExcel(dist, filename)

#print len(hippoPopulation)
#print " "

"""
herd = hippoPopulation[:10]
for animal in herd:
    print "animal is %d." % animal.age
    print "animal is a %s." % animal.gender
    print "animal is fertile? %s." % animal.fertile()
    print "animal 's ovulation time is %d." % (animal.age - animal.birthAge)
    print "next \n"
"""
