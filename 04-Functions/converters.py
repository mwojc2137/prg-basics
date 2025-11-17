def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return round(n*0.3937007874, 2)

def feet_to_cm(feet, inches):
    inch = feet*12 + inches
    return inch*2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'345cm = {cm_to_inch(345)}in')
    print(f'6 feet 2 inches = {feet_to_cm(6, 2)}')

