from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1  = Point(-6,   3)
in2  = Point(-6,  -3)
v1   = Vertex(-4,  2, mark=CIRCLE)
v2   = Vertex(-4, -2, mark=CIRCLE)
v3   = Vertex(-2,  0, mark=CIRCLE)
out1 = Point(0,    3)
out2 = Point(0,   -3)
higgsout = Point(0,0)
out_vtx2 = Vertex(2,  2, mark=CIRCLE)
out_vtx3 = Vertex(2,  -2, mark=CIRCLE)
out3 = Point(4,  4)
out4 = Point(4,  0.25)
out5 = Point(4, -0.25)
out6 = Point(4, -4)


#l1 = Label("ttH(125)", x=0, y=5)

g1 = Gluon(in1, v1).set3D().addLabel("\Pgluon")
g2 = Gluon(in2, v2).set3D().addLabel("\Pgluon",displace=0.25)
t1 = Fermion(v3, v1).addArrow().addLabel("\APtop",displace=0.15)
t2 = Fermion(v2, v3).addArrow().addLabel("\Ptop",displace=0.15)
higgs = Higgs(v3, higgsout).addLabel(r"\PHz")
t3 = Fermion(v1, out1).addArrow().addLabel("\Ptop",displace=0.15)
t4 = Fermion(out2, v2).addArrow().addLabel("\APtop",displace=0.15)

bos2 = Vector(higgsout, out_vtx2).addLabel(r"\PWp")
bos3 = Vector(out_vtx3, higgsout).addLabel(r"\PWm",displace=-0.30)

fb1  = Fermion(out_vtx2, out3).addArrow().addLabel("\Pq")
fb2  = Fermion(out4, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)
fb3  = Fermion(out_vtx3, out5).addArrow().addLabel("\Plm")
fb4  = Fermion(out6, out_vtx3).addArrow().addLabel("\Pagnl",displace=-0.25)


fd.draw("ttH_WW_lvjj.pdf")
#Example Command:
#python ttH_WW_lvjj.py
