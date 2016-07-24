class Vector3D(object):
### START YOUR CLASS IMPLEMENTATION HERE ###

    def __init__(self,x,y,z):
        self.x, self.y, self.z = x, y, z;
        pass
        
    def __str__(self):
        return '(%g,%g,%g)' % (self.x, self.y, self.z);       

    def outer(self, input):
        return Vector3D(self.y*input.z-self.z*input.y, self.z*input.x-self.x*input.z,\
                self.x*input.y-self.y*input.x)

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
v2 = Vector3D(5.2,7.4,-2.5)
v3 = Vector3D(2.1,4.2,0.0)

print 'outer(v1,v2) =', v1.outer(v2)
print 'outer(v1,v3) =', v1.outer(v3)
print 'outer(v2,v3) =', v2.outer(v3)

