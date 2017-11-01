from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  1.5)
in2 = Point(-4, -1.5)
out0 = Point(2,  -1)
out1 = Point(6,  3)
out2 = Point(6,  1.15)
out3 = Point(6,  0.85)
out4 = Point(6, -1)

in_vtx1 = Vertex(-2,   0, mark=CIRCLE)
out_vtx1 = Vertex(0,   0, mark=CIRCLE)
out_vtx2 = Vertex(2,   1, mark=CIRCLE)
#out_vtx3 = Vertex(2,  -1, mark=CIRCLE)
out_vtx4 = Vertex(4,   2, mark=CIRCLE)
out_vtx5 = Vertex(4,   0, mark=CIRCLE)

#l1 = Label("TTbar", x=0, y=5)

fa1  = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2  = Fermion(in_vtx1, in2).addArrow().addLabel("\Paq")
bos0 = Vector(in_vtx1, out_vtx1).addLabel("$W^\pm$")
bos1 = Higgs(out_vtx1, out_vtx2).addLabel("\PHz")
bos2 = Vector(out0, out_vtx1).addLabel("$W^\pm$")

bos3 = Vector(out_vtx2, out_vtx4).addLabel(r"\PWp")
bos4 = Vector(out_vtx2, out_vtx5).addLabel(r"\PWm",displace=0.25)
fc1  = Fermion(out_vtx4, out1).addArrow().addLabel("\Pq")
fc2  = Fermion(out2, out_vtx4).addArrow().addLabel("\Paq")
fc3  = Fermion(out_vtx5, out3).addArrow().addLabel("\Plm")
fc4  = Fermion(out4, out_vtx5).addArrow().addLabel("\Pagnl",displace=-0.25)

fd.draw("WH_WW_lvjj.pdf")
#Example Command:
#python WH_WW_lvjj.py
