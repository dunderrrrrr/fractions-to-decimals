from fractions import Fraction
import sys

def run():
    with open('list.csv') as f:
        l = 0
        for line in f:
            l = l+1
            # CONVERT LINE TO STR AND STRIP WHITESPACE
            fraction_str = line.strip()
            if " " in fraction_str:
                # CONTAINS "X X/X"
                parts = fraction_str.split(' ')
                f1 = Fraction(parts[0])
                f2 = Fraction(parts[1])
                sum = float(f1) + float(f2)
                print("{:.4f}".format(sum))
            elif "#" in fraction_str:
                # IF VALUE ERROR, SKIP LINE
                print("VÄRDEFEL")
            else:
                # CONTAINS "X/X"
                fraction = Fraction(fraction_str)
                f = float(fraction)
                print("{:.4f}".format(f))

if __name__ == '__main__':
    run()
