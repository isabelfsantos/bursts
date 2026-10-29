import schemdraw
import schemdraw.elements as elements

with schemdraw.Drawing() as d:
    d += elements.Battery().right().label("V")
    d += elements.Resistor().down().label("R")
    d += elements.Ground()
    d += elements.Line().left()
    d += elements.Capacitor().left().label("C")
    d += elements.Switch().up()
    d += elements.Line().right()
    d.save("electric_circuit_sample.png")