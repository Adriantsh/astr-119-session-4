import numpy as np 


x = 1.0
y = 2.0

#exponents and logarthms
print(np.exp(x)) 		#e^x
print(np.log(x)) 		#lnx
print(np.log10(x)) 		#log_10 x
print(np.log2(x)) 		#log_2 x

#min/max/misc
print(np.fabs(x)) 		#absolute value
print(np.fmin(x,y)) 	#min
print(np.fmax(x,y))		#max

#populate arrays
n = 100
z = np.arange(n,dtype=float)
z *= 2.0*np.pi/float(n-1)
sin_z = np.sin(z)


#interpolation
print(np.interp(0.75,z,sin_z))
print(np.sin(0.75))


