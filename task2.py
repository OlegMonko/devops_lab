import collections


def count(lst):
    c = collections.Counter()
    for i in lst:
        c[i] += 1
    x, t = c.most_common()[0]
    return x


if __name__ == "__main__":
    n = int(input())
    ll = list(map(int, input().split()))
    print(count(ll))
