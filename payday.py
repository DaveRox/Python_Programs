def computepay(h,r):
    over = h - 40
    if over <= 0:
		return h * r
    else:
		return r * 40 + over * (r * 1.5)

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print p