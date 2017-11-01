from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Point(-4,  3)
in2 = Point(-4, -3)
out1 = Point(4,  1.75)
out2 = Point(4,  0.25)
out3 = Point(4, -0.25)
out4 = Point(4, -1.75)

in_vtx1 = Vertex(-2, 1, mark=CIRCLE)
in_vtx2 = Vertex(-2,-1, mark=CIRCLE)
out_vtx1 = Vertex(1, 1, mark=CIRCLE)
out_vtx2 = Vertex(1,-1, mark=CIRCLE)

#l1 = Label("ggH(125)", x=0, y=5)

fa1  = Fermion(in1, in_vtx1).addArrow().addLabel("\Pq")
fa2  = Fermion(in_vtx1, in_vtx2).addArrow()#.addLabel("\Pq",displace=0.25)
fa3  = Fermion(in_vtx2, in2).addArrow().addLabel("\Paq",displace=0.15)
bos1 = Vector(in_vtx1, out_vtx1).addLabel("\PWp")
glu1 = Gluon(in_vtx2, out_vtx2).set3D().addLabel("\Pgluon")
fb1  = Fermion(out1, out_vtx1).addArrow().addLabel("\Plp",displace=0.25)
fb2  = Fermion(out_vtx1, out2).addArrow().addLabel("\Pgnl",displace=0.25)
fb3  = Fermion(out_vtx2, out3).addArrow().addLabel("\Pq")
fb4  = Fermion(out4, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)

fd.draw("WJets.pdf")
#Example Command:
#python WJets.py
