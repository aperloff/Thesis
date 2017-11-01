from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  1.5)
in2 = Point(-4, -1.5)
out1 = Point(5,  0.25)
out2 = Point(5, -0.25)
out3 = Point(8,  5)
out4 = Point(8,  1)
out5 = Point(8, -1)
out6 = Point(8, -5)

in_vtx1 = Vertex(-2,   0, mark=CIRCLE)
out_vtx1 = Vertex(0,   0, mark=CIRCLE)
out_vtx2 = Vertex(2,   1, mark=CIRCLE)
out_vtx3 = Vertex(2,  -1, mark=CIRCLE)
out_vtx4 = Vertex(5,   3, mark=CIRCLE)
out_vtx5 = Vertex(5,  -3, mark=CIRCLE)

#l1 = Label("TTbar", x=0, y=5)

fa1  = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2  = Fermion(in_vtx1, in2).addArrow().addLabel("\Paq")
glu1 = Gluon(in_vtx1, out_vtx1).set3D().addLabel("\Pgluon")
fb1  = Fermion(out_vtx1, out_vtx2).addArrow().addLabel("\Ptop")
fb2  = Fermion(out_vtx3, out_vtx1).addArrow().addLabel("\APtop")
bos1 = Vector(out_vtx2, out_vtx4).addLabel(r"\PWp")
bos2 = Vector(out_vtx3, out_vtx5).addLabel(r"\PWm",displace=0.25)
b1  = Fermion(out1, out_vtx2).addArrow().addLabel("\Pbottom",displace=-0.25)
b1.setStyles([GREY])
b2  = Fermion(out_vtx3, out2).addArrow().addLabel("\APbottom",displace=-0.25)
b2.setStyles([GREY])
fc1  = Fermion(out_vtx4, out4).addArrow().addLabel("\Pq",displace=0.25)
fc2  = Fermion(out3, out_vtx4).addArrow().addLabel("\Paq",displace=0.25)
fc3  = Fermion(out_vtx5, out5).addArrow().addLabel("\Plm")
fc4  = Fermion(out6, out_vtx5).addArrow().addLabel("\Pagnl",displace=-0.25)

fd.draw("TTbar.pdf")
#Example Command:
#python TTbar.py
