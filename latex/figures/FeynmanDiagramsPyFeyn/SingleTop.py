from pyfeyn.user import *

channels = ["STopS","STopT","STopTW"]

for channel in channels:
    processOptions()
    fd = FeynDiagram()
    
    in1 = Point(-3,  2)
    in2 = Point(-3, -2)
    out1 = Point(3,  2)
    out2 = Point(3, -2)
    
    if channel=="STopS":
        in_vtx1  = Vertex(-1, 0, mark=CIRCLE)
        out_vtx1 = Vertex( 1, 0, mark=CIRCLE)
    else:
        in_vtx1  = Vertex(0,  1, mark=CIRCLE)
        out_vtx1 = Vertex(0, -1, mark=CIRCLE)

    #l1 = Label("ggH(125)", x=0, y=5)


    if channel=="STopS":
        fa1  = Fermion(in2, in_vtx1).addArrow().addLabel("\Pq")
        fa2  = Fermion(in_vtx1, in1).addArrow().addLabel("\Pq'")
        bos1 = Vector(in_vtx1, out_vtx1).addLabel("\PW")
        fb1  = Fermion(out2, out_vtx1).addArrow().addLabel("\APbottom")
        fb2  = Fermion(out_vtx1, out1).addArrow().addLabel("\Ptop")
    elif channel=="STopT":
        fa1  = Fermion(in2, out_vtx1).addArrow().addLabel("\Pq")
        fa2  = Fermion(in1, in_vtx1).addArrow().addLabel("\Pbottom")
        bos1 = Vector(in_vtx1, out_vtx1).addLabel("\PW")
        fb1  = Fermion(out_vtx1, out2).addArrow().addLabel("\Pq'")
        fb2  = Fermion(in_vtx1, out1).addArrow().addLabel("\Ptop")
    else:
        fa1  = Fermion(in2, out_vtx1).addArrow().addLabel("\Pq")
        gl1  = Gluon(in1, in_vtx1).set3D().addLabel("\Pgluon")
        fa2  = Fermion(out_vtx1, in_vtx1).addArrow()
        bos1 = Vector(out_vtx1, out2).addLabel("\PW")
        fb2  = Fermion(in_vtx1, out1).addArrow().addLabel("\Ptop")

    fd.draw(channel+".pdf")

#Example Command:
#python SingleTop.py
