from Fan import Fan

#fan1 객체 생성
fan1 = Fan()
fan1.setSpeed(Fan.FAST)
fan1.setRadius(10)
fan1.setColor("yellow")
fan1.setOn(True)


print("fan1\nspeed : %d\ncolor : %s\nradius : %d\nfan : %s"\
      %(fan1.getSpeed(), fan1.getColor(), fan1.getRadius(),\
        "fan is on" if fan1.isOn() else "fan is off"))

print()
#fan2 객체 생성
fan2 = Fan()
fan2.setSpeed(Fan.MEDIUM)
fan2.setRadius(5)
fan2.setColor("blue")
fan2.setOn(False)
print("fan2\nspeed : %d\ncolor : %s\nradius : %d\nfan : %s"\
      %(fan2.getSpeed(), fan2.getColor(), fan2.getRadius(),\
        "fan is on" if fan2.isOn() else "fan is off"))
