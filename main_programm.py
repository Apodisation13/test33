from summ_def import summ
from minus_def import minus
from mul_def import mul
from div_def import div


if __name__ == "__main__":
    print(summ(*(4, 5, -3)))
    print(minus([4, 5, -2]))
    print(mul(range(1, 5)))
    print(div(*(36, 6, 3, -2, -1)))
