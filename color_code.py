import colorsys
def rgb_to_hex(r, g, b):
    r, g, b = int(r*255), int(g*255), int(b*255)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
f = lambda x:[x] if type(x) is int else x

#######################################
#######################################
# input hls
# h :색상, l : 명도, s : 채도
h,l,s = 0, np.linspace(220,120,5), 237
#######################################
#######################################

h, l, s = f(h), f(l), f(s)
color_ = [rgb_to_hex(*c) for c in [colorsys.hls_to_rgb(*p) for p in [(i/255, j/255, k/255) for i in h for j in l for k in s]]]

plt.bar([i+1 for i in range(5)],x1,color=color_)
plt.show()

##################################################################################
##################################################################################
##################################################################################
##################################################################################

def rgb_to_hex(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
f = lambda x:[x] if type(x) is int else x

#######################################
#######################################
# input rgb
# RGB
r,g,b = 243, np.linspace(50,220,5), 53
#######################################
#######################################

r, g, b = f(r), f(g), f(b)
color_ = [rgb_to_hex(*c) for c in [(i, j, k) for i in r for j in g for k in b]]

plt.bar([i+1 for i in range(5)],x1,color=color_)
plt.show()
