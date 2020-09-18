"""
convert files generated by Monte Carlo method in 2015 to my format
"""
from typing import TextIO


def conv(ranked: TextIO, save2: TextIO, skip_lines: int = 1, pwd_idx: int = 0, rank_idx: int = 1):
    pwd_rank = {}
    for _ in range(skip_lines):
        ranked.readline()
    for line in ranked:
        line = line.strip("\r\n")
        # comma_pos = line.rfind("8")
        # pwd = line[:comma_pos]
        # rank = float(line[comma_pos + 1:])
        items = line.split("\t")
        pwd = items[pwd_idx]
        rank = items[rank_idx]
        n, _ = pwd_rank.get(pwd, (0, .0))
        pwd_rank[pwd] = (n + 1, float(rank))
    prev_rank = 0
    cracked = 0
    total = sum([n for n, _ in pwd_rank.values()])
    for pwd, (num, rank) in sorted(pwd_rank.items(), key=lambda x: x[1][1]):
        cracked += num
        rank = round(max(rank, prev_rank + 1))
        save2.write(f"{pwd}\t{0.0}\t{num}\t{rank}\t{cracked}\t{cracked / total * 100:5.2f}\n")


def main():
    pass


if __name__ == '__main__':
    main()
