import numpy as np
from numba import njit



@njit  # 中心がindexであるときの, 角度をdegrees配列に入れて返す
def make_degrees(index, pos):
    ox, oy = pos[index]
    degrees = np.empty(len(pos))
    for j in range(len(pos)):
        if index == j:
            degrees[j] = 1000.0
            continue
        value = np.degrees(np.arctan2(pos[j][1]-oy, pos[j][0] - ox))
        degrees[j] = value if value >= 0 else 360+value
    return degrees



@njit  # i番目の頂点を中心としたときの角度をdegreesに入れて, binary search
def solve(degrees):
    near_180_value = 1000
    for deg in degrees:
        value = 1000
        contract_deg = deg+180
        if contract_deg > 360:
            contract_deg -= 360
        right = np.searchsorted(degrees, contract_deg)
        left = right - 1
        if right < len(degrees):
            value = abs(deg - degrees[right])
        if abs(180 - value) > abs(180 - abs(deg - degrees[left])):
            value = abs(deg - degrees[left])
        if abs(180 - near_180_value) > abs(180 - value):
            near_180_value = value
    return near_180_value


def main():
    # data load
    N = int(input())
    pos = []
    for _ in range(N):
        x, y = map(int, input().split())
        pos.append((x, y))
    pos = np.array(pos)

    # 各頂点を原点に見立てる
    res = 1000
    for i in range(N):
        degrees = make_degrees(i, pos)
        degrees = np.sort(degrees)
        near_180_value = solve(degrees)
        if abs(180-res) > abs(180-near_180_value):
            if near_180_value > 180:
                near_180_value = 360 - near_180_value
            res = near_180_value

    # output
    print(res)
    return


if __name__ == '__main__':
    main()
