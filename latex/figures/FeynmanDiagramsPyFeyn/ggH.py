from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  1)
in2 = Point(-4, -1)
higgsout = Point(1,  0)

in_vtx1 = Vertex(-2, 1, mark=CIRCLE)
in_vtx2 = Vertex(-2,-1, mark=CIRCLE)
in_vtx3 = Vertex(-1, 0, mark=CIRCLE)

#l1 = Label("ggH(125)", x=0, y=5)

glu1 = Gluon(in1, in_vtx1).set3D().addLabel("\Pgluon")
glu2 = Gluon(in_vtx2, in2).set3D().addLabel("\Pgluon")
fa1  = Fermion(in_vtx1, in_vtx2).addArrow().addLabel("\Pfermion",displace=0.15)
fa2  = Fermion(in_vtx2, in_vtx3).addArrow().addLabel("\Pfermion",displace=0.15)
fa3  = Fermion(in_vtx3, in_vtx1).addArrow().addLabel("\Pfermion",displace=0.15)
bos1 = Higgs(in_vtx3, higgsout).addLabel(r"\PHz")

fd.draw("ggH.pdf")
#Example Command:
#python ggH.py
