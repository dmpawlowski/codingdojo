class ConvertNumbers(object):

  O = { 1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX" }
  T = { 1 : "X", 2 : "XX", 3 : "XXX", 4 : "XL", 5 : "L", 6 : "LX", 7 : "LXX", 8 : "LXXX", 9 : "XC" }
  H = { 1 : "C", 2 : "CC", 3 : "CCC", 4 : "CD", 5 : "D", 6 : "DC", 7 : "DCC", 8 : "DCCC", 9 : "CM" }
  Th = { 1 : "M", 2 : "MM", 3 : "MMM" }

  def __init__(self, num):
    self.num = num
    self.romannum = ""

  def romannumerals(self):
    if self.num >= 1000:
      x = self.num / 1000
      self.num -= x * 1000
      self.romannum += ConvertNumbers.Th[x]
    else:
      pass

    if self.num >= 100:
      x = self.num / 100
      self.num -= x * 100
      self.romannum += ConvertNumbers.H[x]
    else:
      pass

    if self.num >= 10:
      x = self.num / 10
      self.num -= x * 10
      self.romannum += ConvertNumbers.T[x]
    else:
      pass

    if self.num:
      x = self.num
      self.romannum += ConvertNumbers.O[x]
    else:
      pass

    return self.romannum

  # def _thousands(num):
  #   if self.num> 1000:
  #     thousands = self.num/ 1000
  #     self.num-= thousands * 1000
  #     return (num, "M" * thousands)

  # def _hundreds(num, string):
  #   return (num, string)



