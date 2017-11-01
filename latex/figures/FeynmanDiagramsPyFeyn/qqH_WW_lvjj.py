from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,    2)
in2 = Point(-4,   -2)
out1 = Point(0,    2)
out2 = Point(0,   -2)
out3 = Point(6,    2)
out4 = Point(6, 0.25)
out5 = Point(6,-0.25)
out6 = Point(6,   -2)

in_vtx1 = Vertex(-2, 1, mark=CIRCLE)
in_vtx2 = Vertex(-2,-1, mark=CIRCLE)
in_vtx3 = Vertex(0,  0, mark=CIRCLE)
out_vtx1 = Vertex(2,  0, mark=CIRCLE)
out_vtx2 = Vertex(4,  1, mark=CIRCLE)
out_vtx3 = Vertex(4,  -1, mark=CIRCLE)

#l1 = Label("qqH(125)", x=0, y=5)

fa1 = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2 = Fermion(in2, in_vtx2).addArrow().addLabel("\Pq'",displace=0.25)
bos1  = Vector(in_vtx1, in_vtx3).addLabel("\PW/\PZ")
bos2  = Vector(in_vtx2, in_vtx3).addLabel("\PW/\PZ",displace=0.30)
fb1 = Fermion(in_vtx1, out1).addArrow().addLabel("\Pq")
fb1.setStyles([GREY])
fb2 = Fermion(in_vtx2, out2).addArrow().addLabel("\Pq'",displace=0.25)
fb2.setStyles([GREY])
bos1 = Higgs(in_vtx3, out_vtx1).addLabel(r"\PHz")
bos2 = Vector(out_vtx1, out_vtx2).addLabel(r"\PWp")
bos3 = Vector(out_vtx1, out_vtx3).addLabel(r"\PWm",displace=0.25)
fc1  = Fermion(out3, out_vtx2).addArrow().addLabel("\Paq",displace=0.25)
fc2  = Fermion(out_vtx2, out4).addArrow().addLabel("\Pq",displace=0.25)
fc3  = Fermion(out_vtx3, out5).addArrow().addLabel("\Plm")
fc4  = Fermion(out6, out_vtx3).addArrow().addLabel("\Pagnl",displace=-0.25)

fd.draw("qqH_WW_lvjj.pdf")
#Example Command:
#python qqH_WW_lvjj.py
