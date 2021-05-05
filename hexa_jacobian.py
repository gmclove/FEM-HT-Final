# function [N, J1, J] = Hexa_Jacobian(xi,Xe,Ye,Ze)
def hexa_jacobian(xi, Xe, Ye, Ze):
    # note Xe Ye should be column vectors
    # shape function
    r = xi(1)
    s = xi(2)
    t = xi(3)

    N1 = 1 / 8 * (1 - r) * (1 - s) * (1 - t)  # shape function node 1
    N2 = 1 / 8 * (1 + r) * (1 - s) * (1 - t)  # node 2
    N3 = 1 / 8 * (1 + r) * (1 + s) * (1 - t)  # node 3
    N4 = 1 / 8 * (1 - r) * (1 + s) * (1 - t)  # node 4
    N5 = 1 / 8 * (1 - r) * (1 - s) * (1 + t)  # node 5
    N6 = 1 / 8 * (1 + r) * (1 - s) * (1 + t)  # node 6
    N7 = 1 / 8 * (1 + r) * (1 + s) * (1 + t)  # node 7
    N8 = 1 / 8 * (1 - r) * (1 + s) * (1 + t)  # node 8
    N = [N1, N2, N3, N4, N5, N6, N7, N8]

    # differentials with respect to r
    N1r = -1 / 8 * (1 - s) * (1 - t)
    N2r = 1 / 8 * (1 - s) * (1 - t)
    N3r = 1 / 8 * (1 + s) * (1 - t)
    N4r = -1 / 8 * (1 + s) * (1 - t)
    N5r = -1 / 8 * (1 - s) * (1 + t)
    N6r = 1 / 8 * (1 - s) * (1 + t)
    N7r = 1 / 8 * (1 + s) * (1 + t)
    N8r = -1 / 8 * (1 + s) * (1 + t)

    # differentials with respect to s
    N1s = -1 / 8 * (1 - r) * (1 - t)
    N2s = -1 / 8 * (1 + r) * (1 - t)
    N3s = 1 / 8 * (1 + r) * (1 - t)
    N4s = 1 / 8 * (1 - r) * (1 - t)
    N5s = -1 / 8 * (1 - r) * (1 + t)
    N6s = -1 / 8 * (1 + r) * (1 + t)
    N7s = 1 / 8 * (1 + r) * (1 + t)
    N8s = 1 / 8 * (1 - r) * (1 + t)

    # differentials with respect to t
    N1t = -1 / 8 * (1 - r) * (1 - s)
    N2t = -1 / 8 * (1 + r) * (1 - s)
    N3t = -1 / 8 * (1 + r) * (1 + s)
    N4t = -1 / 8 * (1 - r) * (1 + s)
    N5t = 1 / 8 * (1 - r) * (1 - s)
    N6t = 1 / 8 * (1 + r) * (1 - s)
    N7t = 1 / 8 * (1 + r) * (1 + s)
    N8t = 1 / 8 * (1 - r) * (1 + s)

    # note:Jacobian Matrix J=J1*X
    J1 = [[N1r, N2r, N3r, N4r, N5r, N6r, N7r, N8r],
          [N1s, N2s, N3s, N4s, N5s, N6s, N7s, N8s],
          [N1t, N2t, N3t, N4t, N5t, N6t, N7t, N8t]]
    J = J1 * [Xe, Ye, Ze]

    return [N, J1, J]
