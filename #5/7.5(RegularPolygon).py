from RegularPolygon import RegularPolygon

#객체 생성
Poly0 = RegularPolygon()
Poly1 = RegularPolygon(4,4)
Poly2 = RegularPolygon(10, 4, 5.6, 7.8)

print("객체Poly0의 둘레는 %.1f이고, 넓이는 %.1f이다.\n"%(Poly0.getPerimeter(), Poly0.getArea()))
print("객체Poly1의 둘레는 %.1f이고, 넓이는 %.1f이다.\n"%(Poly1.getPerimeter(), Poly1.getArea()))
print("객체Poly2의 둘레는 %.1f이고, 넓이는 %.1f이다.\n"%(Poly2.getPerimeter(), Poly2.getArea()))

print(Poly0.getx(), Poly0.gety())
print(Poly1.getx(), Poly1.gety())
print(Poly2.getx(), Poly2.gety())

