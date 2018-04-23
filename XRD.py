import numpy as np

#input
print("enter unit cell dimensions in angstroms")
dimensions = [float(input("a=")),float(input("b=")),float(input("c="))]
bravaisType = float(input("1. Simple cubic, 2. Body-centered cubic, 3. Face-centered cubic, 4. Diamond face-centered cubic, 5. Triangular lattice"))
WAVELENGTH = 1.5406 #CuKα wavelength in angstroms
MAX_INDEX = 5 #maximum hkl index to try

i = [0,0,0]             #tries every reflection as 3 integers
reflections = []        #output valid reflections as a string

#find h,k,l reflections
for i[0] in range (0, MAX_INDEX):
    for i[1] in range (0, MAX_INDEX):
        for i[2] in range (0, MAX_INDEX):
            if (bravaisType == 1):                                      #simple cubic: no restrictions.
                reflections += [[i[0],i[1],i[2]]]
            elif(bravaisType == 2):                                     #body-centered cubic: add to even.
                if ((i[0]+i[1]+i[2]) % 2 == 0):                         
                    reflections += [[i[0],i[1],i[2]]]
            elif(bravaisType == 3):                                     #Face-centered cubic: unmixed odd and even.
                if i[0]%2 == 0:
                    if (i[1]%2 == 0) and (i[2]%2 == 0):
                        reflections += [[i[0],i[1],i[2]]]
                else:
                    if (i[1]%2 == 1) and (i[2]%2 == 1):
                        reflections += [[i[0],i[1],i[2]]]
            elif(bravaisType == 4):                                     #Diamond face-centered cubic: all odd or even & add to multiple of 4.
                if i[0]%2 == 0:
                    if (i[1]%2 == 0) and (i[2]%2 == 0) and ((i[0]+i[1]+i[3])%4 == 0):
                        reflections += [[i[0],i[1],i[2]]]
                else:
                    if (i[1]%2 == 1) and (i[2]%2 == 1):
                        reflections += [[i[0],i[1],i[2]]]
            elif(bravaisType == 5):                                     #Triangular: all even or odd and don't add to multiple of 3
                if i[0]%2 == 0:
                    if (i[1]%2 == 0) and (i[2]%2 == 0):
                        reflections += [[i[0],i[1],i[2]]]
                else:
                    if (i[1]%2 == 1) and (i[2]%2 == 1) and ((i[0]+i[1]+i[3])%3 != 0):
                        reflections += [[i[0],i[1],i[2]]]


n=1                 #placeholder for higher order reflections

d = [0] * len(reflections)
twoTheta = [0] * len (reflections)
#print("length is ",len(reflections))

#convert reflection to atomic plane spacing
if bravaisType == 1:
    for j in range (1, len(reflections)):                                 #start from element 1 to prevent division by zero
        d[j] = dimensions[0]/np.sqrt(np.power(reflections[j][0], 2) + np.power(reflections[j][1], 2) + np.power(reflections[j][2], 2))     #simple cubic: d = a/sqrt(h^2+k^2+l^2)

#convert atomic plane spacing to reflection angle
for j in range (1, len(reflections)):
    if (n*WAVELENGTH/(2*d[j]) <= 1):
        twoTheta[j] = 2*np.arcsin(n*WAVELENGTH/(2*d[j])) * 180/ 3.14159 #final 2-theta in degrees

#display output
for j in range (1, len(reflections)):
    print("For hkl=",reflections[j],", theta =",twoTheta[j])
