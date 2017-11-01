from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  1.5)
in2 = Point(-4, -1.5)
out0 = Point(2,  -1.5)

in_vtx1 = Vertex(-2,   0, mark=CIRCLE)
out_vtx1 = Vertex(0,   0, mark=CIRCLE)
out_vtx2 = Point(2,   1.5)

#l1 = Label("TTbar", x=0, y=5)

fa1  = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2  = Fermion(in_vtx1, in2).addArrow().addLabel("\Paq")
bos0 = Vector(in_vtx1, out_vtx1).setAmplitude(0.15).addLabel("$W^\pm$")
bos1 = Higgs(out_vtx1, out_vtx2).addLabel("\PHz")
bos2 = Vector(out0, out_vtx1).setAmplitude(0.15).addLabel("$W^\pm$",displace=-0.35)

fd.draw("WH.pdf")
#Example Command:
#python WH.py
