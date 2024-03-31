cans = [['#1 Picnic',6.83,10.16,0.28],
    ['#1 Tall',7.78,11.91,0.43],
    ['#2',8.73,11.59,0.45],
    ['#2.5',10.32,11.91,0.61],
    ['#3 Cylinder',10.79,17.78,0.86],
    ['#5',13.02,14.29,0.83],
    ['#6Z',5.40,8.89,0.22],
    ['#8Z short',6.83,7.62,0.26],
    ['#10',15.72,17.78,1.53],
    ['#211',6.83,12.38,0.34],
    ['#300',7.62,11.27,0.38],
    ['#303',8.10,11.11,0.42]]

def volume(r, h):
        return 3.14*(r*r)*h

def area(r, h):
        return 3.14*r*(r+h)

def eff(v,a):
    return v/a

def main(arry):
    for item in arry:
        name = item[0]
        radius = item[1]
        height = item[2]
        cost = item[3]
        v = volume(radius, height)
        a = area(radius, height)
        e = eff(v,a)
        print(f'{name}, {v}, {a}, {e}')

main(cans)

        
