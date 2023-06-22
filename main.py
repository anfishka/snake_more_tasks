# 1) Лениво заполнить матрицу от 1 до 9 и вывести квадратом разделяя значения пробелом
# 1 2 3
# 4 5 6
# 7 8 9
#
# matrix_3X3 = [[1,2,3], [4,5,6], [7,8,9]]
#
# if len(matrix_3X3) == 3:
#     for i in matrix_3X3:
#         print(i)
# else:
#     print("Check length of your matrix! ")
#
# 2) С клавы заполнить матрицу 5 х 5 и вывести
#
# matrix_5X5 = []
#
# print("Fill in a matrix 5 X 5")
# for i in range(5):
#     tmp_matrix = []
#     for j in range(5):
#         fill_in_arr = abs(int(input("Enter value -> ")))
#         tmp_matrix.append(fill_in_arr)
#     matrix_5X5.append(tmp_matrix)
#
# if len(matrix_5X5) == 5:
#     for i in matrix_5X5:
#         print(i)
# else:
#     print("Check length of your matrix!")

# 3)  С клавы заполнить матрицу пользовательского размера и вывести
#
# matrix_nXn = []
# len_matrix = abs(int(input("Enter length of matrix -> ")))
#
# print("Fill in a matrix -> ", len_matrix, " X ", len_matrix)
# for i in range(len_matrix):
#     tmp_matrix = []
#     for j in range(len_matrix):
#         fill_in_arr = abs(int(input("Enter value -> ")))
#         tmp_matrix.append(fill_in_arr)
#     matrix_nXn.append(tmp_matrix)
#
# if len(matrix_nXn) == len_matrix and len_of_matrix > 1:
#     for i in matrix_nXn:
#         print(i)
# else:
#     print("Check length of your matrix!")
#

 # 4) Принять у пользователя матрицу произвольного размера и посчитать сумму всех значений

# matrix_nXn = []
# len_of_matrix = abs(int(input("Enter length of matrix -> ")))
# sum_val = 0
#
# for i in range(len_of_matrix):
#     tmp_arr = []
#     for j in range(len_of_matrix):
#         tmp_arr_val = abs(int(input("Enter values -> ")))
#         tmp_arr.append(tmp_arr_val)
#         sum_val += tmp_arr_val
#     matrix_nXn.append(tmp_arr)
#
# if len(matrix_nXn) == len_of_matrix and len_of_matrix > 1:
#     for i in matrix_nXn:
#         print("Your matrix" + str(i))
#     print("Sum of all values in you matrix -> " + str(sum_val))
# else:
#     print("Check length of your matrix!")
#
# 5) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждому столбцу
#
# matrix_nXn = []
# len_of_matrix = abs(int(input("Enter length of matrix -> ")))
# sum_val_col = 0
# 
# for i in range(len_of_matrix):
#     tmp_arr = []
#     for j in range(len_of_matrix):
#         tmp_arr_val = abs(int(input("Enter values -> ")))
#         tmp_arr.append(tmp_arr_val)
#     matrix_nXn.append(tmp_arr)
# 
# print("Your matrix -> ")
# for i in matrix_nXn:
#     print(i)
# print("Your sum of each col in matrix -> ")
# for i in range(len(matrix_nXn)):
#     col_sum = 0
#     for j in range(len(matrix_nXn)):
#         col_sum += matrix_nXn[j][i]
#     if matrix_nXn == len_of_matrix and len_of_matrix > 1:
#         print([col_sum], end=" ")
#
#
# # 6) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждой строке
#
# # matrix = [[1,2],[3,4]]
# #
# # print("Your matrix -> ")
# # for i in matrix:
# #     print(i)
# # print("Your sum of each row in matrix -> ")
# # for col in range(len(matrix)):
# #     col_sum = 0
# #     for row in range(len(matrix)):
# #         col_sum += matrix[col][row]
# #
# #     print([col_sum], end=" ")
#
# # 7) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждой из диагоналей
# # matrix = [[1,2],[3,4]]
#
# # print("Your matrix -> ")
# # for i in matrix:
# #     print(i)
# # print("Your sum of each row in matrix -> ")
# # for col in range(len(matrix)):
# #     col_sum = 0
# #     for row in range(len(matrix)):
# #         col_sum += matrix[col][row]
# #
# #     print([col_sum], end=" ")
#
# matrix = [[1,2,5],[2,3,4],[6,8,9]]
# sum_val_diagonal_m = 0
# sum_val_diagonal_s = 0
# sum_val_diagonal_h = 0
# sum_val_diagonal_v = 0
#
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if j == i :
#             sum_val_diagonal_m += matrix[i][j]
#         if  i == len(matrix) - j - 1:
#             sum_val_diagonal_s += matrix[i][j]
#         if i == len(matrix) // 2:
#             sum_val_diagonal_h += matrix[i][j]
#         if j == len(matrix) // 2:
#            sum_val_diagonal_v += matrix[i][j]
#
# print("Your matrix -> ")
# for i in matrix:
#     print(i)
# print("Sum of values in main diagonal -> " + str(sum_val_diagonal_m) + "\nSum of values in main diagonal -> " + str(sum_val_diagonal_s) + "\nSum of values in horizontal diagonal -> " + str(sum_val_diagonal_h)+ "\nSum of values in vertical diagonal -> " + str(sum_val_diagonal_v))
#

# 8) Вывести матрицу 10 на 10 заполненую символом * по границам

# MATRIX_SIZE = 10
#
# for i in range(MATRIX_SIZE):
#     for j in range(MATRIX_SIZE):
#         if i == 0 or j == 0 or i == MATRIX_SIZE - 1 and j < MATRIX_SIZE or j == MATRIX_SIZE - 1 and i < MATRIX_SIZE :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 9-12 Написать игру
# Суть в том, что появляется игровое поле 10 на 10 символов заполненное внутри пробелом, а внешне - *
# Появляется игрок в виде символа @
# Появляется враги в виде символа + (с каждым уровнем +1 )
# Суть игры в том, чтобы за минимальное количество шагов сьесть всех врагов
# Изначально есть 5 ходов
# За каждого врага +5 ходов
# Враги появляются по случайным координатам
#
#
#
# import random
#
# BATTLE_FIELD_SIZE = 10
# BATTLE_FIELD = []
# STAR = "*"
# EMPTY = " "
# ENEMY = "+"
# PLAYER = "@"
# LEVEL = 1
# PLAYER_MOVES = 5
# TOTAL_ENEMIES = 2
# DIRECTIONS = ["W", "A", "D", "S"]
#
# for i in range(BATTLE_FIELD_SIZE):
#     tmp_field = []
#     for j in range(BATTLE_FIELD_SIZE):
#         if i == 0 or j == 0 or (i == BATTLE_FIELD_SIZE - 1 and j < BATTLE_FIELD_SIZE) or (
#                 j == BATTLE_FIELD_SIZE - 1 and i < BATTLE_FIELD_SIZE):
#             tmp_field.append(STAR)
#         else:
#             tmp_field.append(EMPTY)
#     BATTLE_FIELD.append(tmp_field)
#
# player_pos_h = random.randrange(1, BATTLE_FIELD_SIZE - 1)
# player_pos_v = random.randrange(1, BATTLE_FIELD_SIZE - 1)
# BATTLE_FIELD[player_pos_h][player_pos_v] = PLAYER
#
#
# def random_pos():
#     rand_pos_h = random.randrange(1, BATTLE_FIELD_SIZE - 1)
#     rand_pos_v = random.randrange(1, BATTLE_FIELD_SIZE - 1)
#     return rand_pos_h, rand_pos_v
#
#
# def create_enemies():
#     for i in range(TOTAL_ENEMIES):
#         enemy_pos_h, enemy_pos_v = random_pos()
#         while BATTLE_FIELD[enemy_pos_h][enemy_pos_v] != EMPTY:
#             enemy_pos_h, enemy_pos_v = random_pos()
#         BATTLE_FIELD[enemy_pos_h][enemy_pos_v] = ENEMY
#
# create_enemies()
#
# DEFEATED_ENEMIES = 0
#
# while True:
#     if PLAYER_MOVES == 0:
#         print("Game over! You ran out of moves.")
#         break
#
#     print("Level: ",LEVEL)
#     print("Player moves left: ", PLAYER_MOVES)
#     print("Defeated enemies: ", DEFEATED_ENEMIES , "/", TOTAL_ENEMIES)
#
#     for i in BATTLE_FIELD:
#         print(i)
#
#     direction = input("Choose direction -> D - go to the right, A - go to the left, W - go up, S - go down -> ")
#     if direction not in DIRECTIONS:
#         print("Invalid direction! Try again!")
#         continue
#
#     for i in range(BATTLE_FIELD_SIZE):
#         for j in range(BATTLE_FIELD_SIZE):
#             if BATTLE_FIELD[i][j] == PLAYER:
#                 player_pos_h, player_pos_v = i, j
#                 break
#
#     new_player_pos_h, new_player_pos_v = player_pos_h, player_pos_v
#
#     if direction == DIRECTIONS[0]:
#         new_player_pos_h -= 1
#     elif direction == DIRECTIONS[1]:
#         new_player_pos_v -= 1
#     elif direction == DIRECTIONS[2]:
#         new_player_pos_v += 1
#     elif direction == DIRECTIONS[3]:
#         new_player_pos_h += 1
#
#     if not (1 <= new_player_pos_h < BATTLE_FIELD_SIZE - 1) or not (1 <= new_player_pos_v < BATTLE_FIELD_SIZE - 1):
#         print("Invalid move! You can't go outside the battlefield!")
#         continue
#
#     if BATTLE_FIELD[new_player_pos_h][new_player_pos_v] == EMPTY:
#         BATTLE_FIELD[player_pos_h][player_pos_v] = EMPTY
#         BATTLE_FIELD[new_player_pos_h][new_player_pos_v] = PLAYER
#         player_pos_h, player_pos_v = new_player_pos_h, new_player_pos_v
#         PLAYER_MOVES -= 1
#
#     elif BATTLE_FIELD[new_player_pos_h][new_player_pos_v] == ENEMY:
#         BATTLE_FIELD[new_player_pos_h][new_player_pos_v] = EMPTY
#         DEFEATED_ENEMIES += 1
#         PLAYER_MOVES += 5
#         print("You defeated an enemy!")
#
#     if DEFEATED_ENEMIES >= TOTAL_ENEMIES:
#         print("Congratulations! You defeated all the enemies.")
#         LEVEL += 1
#         TOTAL_ENEMIES += 1
#         DEFEATED_ENEMIES = 0
#         PLAYER_MOVES = 5
#         create_enemies()

