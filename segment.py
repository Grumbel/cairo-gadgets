def segment(a, b, r):
    def loop(a, b, r):
        if r == 0:
            return [a]
        else:
            m = (a + b)/2.0
            return loop(a, m, r-1) + loop(m, b, r-1)

    return loop(a, b, r) + [b]

# EOF #
