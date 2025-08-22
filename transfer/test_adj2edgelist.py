import numpy as np
import torch

def adjacency_matrix_to_edge_list(adj_matrix):
    edge_list = []
    edge_features_list_one_dimension = []


    # 获取邻接矩阵的行数和列数
    num_rows, num_cols = len(adj_matrix), len(adj_matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            # 如果邻接矩阵中存在边（非零元素），则将其加入边列表
            if adj_matrix[i][j] != 0:
                edge_list.append((i, j))
                edge_features_list_one_dimension.append(adj_matrix[i][j])
    edge_features_list = [[x] for x in edge_features_list_one_dimension]
    return edge_list, edge_features_list

# 示例邻接矩阵
adjacency_matrix = [
    [0, 1., 0, 1.5],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# 转换为边列表
edges_list, edge_features_list = adjacency_matrix_to_edge_list(adjacency_matrix)

# 打印结果
print("Edge List:")
print(edges_list)
print(edge_features_list)


edge_index = torch.tensor(np.array(edges_list).T, dtype=torch.long)
edge_attr = torch.tensor(np.array(edge_features_list),
                         dtype=torch.long)
print(edge_index)
print(edge_index.shape)
print(edge_attr)
print(edge_attr.shape)