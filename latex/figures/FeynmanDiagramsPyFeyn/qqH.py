from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,    2)
in2 = Point(-4,   -2)
out1 = Point(2,    2)
out2 = Point(2,   -2)
higgsout = Point(2,  0)

in_vtx1 = Vertex(-2, 1, mark=CIRCLE)
in_vtx2 = Vertex(-2,-1, mark=CIRCLE)
in_vtx3 = Vertex(0,  0, mark=CIRCLE)


#l1 = Label("qqH(125)", x=0, y=5)

fa1 = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2 = Fermion(in2, in_vtx2).addArrow().addLabel("\Pq'",displace=0.25)
bos1  = Vector(in_vtx1, in_vtx3).setAmplitude(0.15).addLabel("$W^\pm$/\PZ")
bos2  = Vector(in_vtx2, in_vtx3).setAmplitude(0.15).addLabel("$W^\mp$/\PZ",displace=0.30)
fb1 = Fermion(in_vtx1, out1).addArrow().addLabel("\Pq")
fb1.setStyles([GREY])
fb2 = Fermion(in_vtx2, out2).addArrow().addLabel("\Pq'",displace=0.25)
fb2.setStyles([GREY])
bos1 = Higgs(in_vtx3, higgsout).addLabel(r"\PHz")

fd.draw("qqH.pdf")
#Example Command:
#python qqH.py
