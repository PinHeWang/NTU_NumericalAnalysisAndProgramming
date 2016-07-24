class Vector3D(object):
### START YOUR CLASS IMPLEMENTATION HERE ###

    def __init__(self,x=0.,y=0.,z=0.):
        self.x,self.y,self.z = x,y,z;
        pass

    def __str__(self):
        return '(%g,%g,%g)' % (self.x,self.y,self.z);

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
print 'converting v1 to string:', v1

v2 = Vector3D(5.2,7.4,-2.5)
print 'converting v2 to string:', v2

