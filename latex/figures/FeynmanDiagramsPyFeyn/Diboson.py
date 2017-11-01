from pyfeyn.user import *

bosonPairs = [("Wp","Wm"),("Z","Z"),("Wp","Z")]

for pair in bosonPairs:
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
    bos1 = Vector(in_vtx1, out_vtx1).addLabel("\P"+pair[0])
    bos2 = Vector(in_vtx2, out_vtx2).addLabel("\P"+pair[1])
    if pair[0]=="Wp":
        fb1  = Fermion(out1, out_vtx1).addArrow().addLabel("\Plp",displace=0.25)
        fb2  = Fermion(out_vtx1, out2).addArrow().addLabel("\Pgnl",displace=0.25)
    elif pair[0]=="Wm":
        fb1  = Fermion(out_vtx1, out1).addArrow().addLabel("\Plm",displace=0.25)
        fb2  = Fermion(out2, out_vtx1).addArrow().addLabel("\Pagnl",displace=0.25)
    else:
        fb1  = Fermion(out1, out_vtx1).addArrow().addLabel("\Plp",displace=0.25)
        fb2  = Fermion(out_vtx1, out2).addArrow().addLabel("\Plm",displace=0.25)
        fb2.setStyles([GREY])
    if pair[1]=="Wp":
        fb3  = Fermion(out_vtx2, out3).addArrow().addLabel("\Pq")
        fb4  = Fermion(out4, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)
    elif pair[1]=="Wm":
        fb3  = Fermion(out_vtx2, out3).addArrow().addLabel("\Pq")
        fb4  = Fermion(out4, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)
    else:
        fb3  = Fermion(out_vtx2, out3).addArrow().addLabel("\Pq")
        fb4  = Fermion(out4, out_vtx2).addArrow().addLabel("\Paq",displace=-0.25)

    fd.draw(pair[0][0]+pair[1][0]+".pdf")

#Example Command:
#python Diboson.py
