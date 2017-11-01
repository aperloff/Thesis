from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1  = Point(-6,   2)
in2  = Point(-6,  -2)
v1   = Vertex(-4,  1, mark=CIRCLE)
v2   = Vertex(-4, -1, mark=CIRCLE)
v3   = Vertex(-2,  0, mark=CIRCLE)
out1 = Point(0,    2)
out2 = Point(0,   -2)
higgsout = Point(0,0)

#l1 = Label("ttH(125)", x=0, y=5)

g1 = Gluon(in1, v1).set3D().addLabel("\Pgluon")
g2 = Gluon(in2, v2).set3D().addLabel("\Pgluon",displace=0.25)
t1 = Fermion(v3, v1).addArrow().addLabel("\APtop",displace=0.15)
t2 = Fermion(v2, v3).addArrow().addLabel("\Ptop",displace=0.15)
higgs = Higgs(v3, higgsout).addLabel(r"\PHz")
t3 = Fermion(v1, out1).addArrow().addLabel("\Ptop",displace=0.15)
t4 = Fermion(out2, v2).addArrow().addLabel("\APtop",displace=0.15)

fd.draw("ttH.pdf")
#Example Command:
#python ttH.py
