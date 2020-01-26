def get_size(w,h,d):
    v = w * h * d
    a = (w*h)*2+(w*d)*2+(h*d)*2
    return [a, v]