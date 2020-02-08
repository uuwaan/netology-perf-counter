import perms
import nqueens
import ourperf

NQUEENS = 8

MSG_PUREBENCH = "=== Решение задачи {0} ферзей (перестановки на Python) ==="
MSG_EXTBENCH = "=== Решение задачи {0} ферзей (перестановки на C) ==="


def run():
    print(MSG_PUREBENCH.format(NQUEENS))
    with ourperf.Counter():
        nqueens.bench(NQUEENS, perms.pure)

    print()

    print(MSG_EXTBENCH.format(NQUEENS))
    with ourperf.Counter():
        nqueens.bench(NQUEENS, perms.c_ext)
