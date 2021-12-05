import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from collections import Counter


def scc(N, M, edges):
    """
    有向グラフの強連結成分分解を行う. 返り値は順に連結成分数と所属グループ配列
    edgesは0-indexed.
    """
    edge = np.array(edges, dtype=np.int64).T
    weight = np.ones(M, dtype=np.int64).T
    graph = csr_matrix((weight, edge[:]), (N, N))
    connected_component, array = connected_components(graph, directed=True, connection="strong")
    return connected_component, array


def main():
    # data load
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(lambda x: int(x)-1, input().split())))

    size, array = scc(N, M, edges)
    array = Counter(array)

    ans = 0
    for key, value in array.items():
        ans += value * (value-1) // 2
    print(ans)


if __name__ == '__main__':
    main()
