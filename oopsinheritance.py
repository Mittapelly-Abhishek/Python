#inheritance #multilevel property

class G_parent:
    g_property=1000
    name='illaiah'
    initial="M"
    
class parent(G_parent):
    name="srinivas"
    p_property=100
 
class child(parent):
    name="abhisekk"
    c_property=10
    
class my_child(child):
    name="not yet decided"

c1=child()
print(c1.name)
print(c1.initial)
print(c1.c_property,"->",c1.p_property,"->",c1.g_property)
c2=my_child()
print(c2.name)
print(c2.initial)
print(c2.p_property,c2.c_property)



