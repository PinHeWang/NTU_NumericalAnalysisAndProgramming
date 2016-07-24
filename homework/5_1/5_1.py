class Vector3D(object):
### START YOUR CLASS IMPLEMENTATION HERE ###

    def __init__(self,x=0.,y=0.,z=0.):
        self.x,self.y,self.z=x,y,z;
        pass

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
print 'attributes of v1:', v1.x, v1.y, v1.z

v2 = Vector3D(5.2,7.4,-2.5)
print 'attributes of v2:', v2.x, v2.y, v2.z

