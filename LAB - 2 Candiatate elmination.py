import pandas as pd

data = pd.read_csv("data.csv")
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

S = list(X[0])
G = [["?"] * len(S)]

for i, x in enumerate(X):
    if Y[i] == "Yes":
        for j in range(len(S)):
            if S[j] != x[j]:
                S[j] = "?"
    else:
        for j in range(len(S)):
            if x[j] != S[j]:
                G.append(["?"] * j + [S[j]] + ["?"] * (len(S)-j-1))

print("Specific:", S)
print("General:", G)
