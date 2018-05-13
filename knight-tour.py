# The knight is placed on the first block of an empty board and, moving
# according to the rules of chess, must visit each square exactly once.

# this is based on the backtracking approach


MoveX = [2, 1, -1, -2, -2, -1,  1,  2]
MoveY = [1, 2,  2,  1, -1, -2, -2, -1]


def is_valid_move(i, j, N):

    return i < N and i >= 0 and j < N and j >= 0 and chess[i][j] == -1


def knight_tour(chess, N, x, y, moves):

    if moves == N*N:
        # print(chess)
        return True

    # as there are max 8 possible moves for a knight at a specific location
    # print(chess)
    for k in range(8):
        newx = x + MoveX[k]
        newy = y + MoveY[k]

        if is_valid_move(newx, newy, N):
            # print(x, y)
            chess[newx][newy] = moves + 1
            # print(moves)

            if knight_tour(chess, N, newx, newy, moves+1):
                return True
            else:
                chess[x][y] = -1

    return False


if __name__ == "__main__":
    input = int(input("Enter Chess Matrix size: "))
    chess = [[-1] * input for i in range(input)]
    chess[0][0] = 1

    if knight_tour(chess, input, 0, 0, 1):
        print(chess)


