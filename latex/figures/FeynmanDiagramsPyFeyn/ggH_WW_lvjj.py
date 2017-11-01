from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  1)
in2 = Point(-4, -1)
out1 = Point(6,  3)
out2 = Point(6,  0.25)
out3 = Point(6, -0.25)
out4 = Point(6, -3)

in_vtx1 = Vertex(-2, 1, mark=CIRCLE)
in_vtx2 = Vertex(-2,-1, mark=CIRCLE)
in_vtx3 = Vertex(-1, 0, mark=CIRCLE)
out_vtx1 = Vertex(1,  0, mark=CIRCLE)
out_vtx2 = Vertex(3,  1, mark=CIRCLE)
out_vtx3 = Vertex(3,  -1, mark=CIRCLE)

#l1 = Label("ggH(125)", x=0, y=5)

glu1 = Gluon(in1, in_vtx1).set3D().addLabel("\Pgluon")
glu2 = Gluon(in_vtx2, in2).set3D().addLabel("\Pgluon")
fa1  = Fermion(in_vtx1, in_vtx2).addArrow().addLabel("\Pfermion",displace=0.15)
fa2  = Fermion(in_vtx2, in_vtx3).addArrow().addLabel("\Pfermion",displace=0.15)
fa3  = Fermion(in_vtx3, in_vtx1).addArrow().addLabel("\Pfermion",displace=0.15)
bos1 = Higgs(in_vtx3, out_vtx1).addLabel(r"\PHz")
bos2 = Vector(out_vtx1, out_vtx2).addLabel(r"\PWp")
bos3 = Vector(out_vtx3, out_vtx1).addLabel(r"\PWm",displace=-0.30)

fb1  = Fermion(out_vtx2, out1).addArrow().addLabel("\Pq")
fb2  = Fermion(out2, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)
fb3  = Fermion(out_vtx3, out3).addArrow().addLabel("\Plm")
fb4  = Fermion(out4, out_vtx3).addArrow().addLabel("\Pagnl",displace=-0.25)

fd.draw("ggH_WW_lvjj.pdf")
#Example Command:
#python ggH_WW_lvjj.py
