# %% [markdown]
# Вариант 1

# %%

def n_i(i):
    return 1 + (i + m - 2) % n

# %%

n, m = map(int, input().split())
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()

# %% [markdown]
# Вариант 2

# %%
def seq(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield v

print(list(seq(n,m)))


