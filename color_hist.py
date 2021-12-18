
import cv2
#import matplotlib.pyplot as plt


#image = cv2.imread('mid.jpg')
for i, col in enumerate(['b', 'g', 'r']):
    #hist = cv2.calcHist([image], [i], None, [256], [0, 256])
 	print ("i  = ",i)
 	print ("col= ",col)

    #plt.plot(hist, color = col)
    #plt.xlim([0, 256])
    
#plt.show()

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. T
#This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.