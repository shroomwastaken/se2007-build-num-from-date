# based on https://github.com/VSES/SourceEngine2007/blob/master/se2007/engine/buildnum.cpp

print(int(input("day: ")) - 1 + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:(m := int(input("month: ")) - 1)]) +  int((((y := int(input("year: ")) - 1900) - 1) * 365.25) - (35738 if y % 4 == 0 and m > 1 else 35739)))