"""
Three distinct points are plotted at random on a Cartesian plane, for which
-1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle
XYZ does not.

Using triangles.txt, find the number of triangles for which the interior
contains the origin.
"""

def intersect(ra, rb, sa, sb):
    rpx = ra[0]
    rpy = ra[1]
    rdx = rb[0] - ra[0]
    rdy = rb[1] - ra[1]

    spx = sa[0]
    spy = sa[1]
    sdx = sb[0] - sa[0]
    sdy = sb[1] - sa[1]

    rmag = (rdx*rdx + rdy*rdy)**0.5
    smag = (sdx*sdx + sdy*sdy)**0.5

    if (rdx/rmag == sdx/smag and rdy/rmag == sdy/smag):
        # No intersection
        return 0

    t2 = (rdx*(spy - rpy) + rdy*(rpx - spx)) / (sdx*rdy - sdy*rdx)
    t1 = (spx + sdx*t2 - rpx) / rdx

    if (t1 < 0):
        return 0

    if (t2 < 0 or t2 > 1):
        return 0

    # The ray and the segment intersect at some location
    return 1

def 


