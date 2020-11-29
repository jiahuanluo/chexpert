import os

two_view_train_file = open("CheXpert-v1.0-small/two_view_train.csv").readlines()[1:]
two_view_test_file = open("CheXpert-v1.0-small/two_view_test.csv").readlines()[1:]
train_file = open("train.csv")[1:]
with open("CheXpert-v1.0-small/two_train.csv", "w") as f:
    for line in two_view_train_file:
        for t_line in train_file:
            if line.strip().split(",")[0] in t_line:
                f.write(t_line)
                continue

with open("CheXpert-v1.0-small/two_test.csv", "w") as f:
    for line in two_view_test_file:
        for t_line in train_file:
            if line.strip().split(",")[0] in t_line:
                f.write(t_line)
                continue