def determinant(mx):
    a = len(mx[0])
    if a == 2:
        return mx[0][1]*mx[1][1]-mx[0][1]*mx[1][0]
    elif a == 3:
        return (mx[0][0]*mx[1][1]*mx[2][2]+mx[0][1]*mx[1][2]*mx[2][0]+mx[1][0]*mx[2][1]*mx[0][2])-(mx[0][2]*mx[1][1]*mx[2][0]+mx[0][0]*mx[1][2]*mx[2][1]+mx[1][0]*mx[2][2]*mx[0][1])
    else:
        return 'Sorry, for now I can solve only 2x2 and 3x3 determinants'
