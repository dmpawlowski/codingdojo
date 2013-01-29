from nose.tools import *
from katas.roman import *

def test_romannumerals_1():
  assert_equal(ConvertNumbers(1).romannumerals(), "I")

def test_romannumerals_13():
  assert_equal(ConvertNumbers(13).romannumerals(), "XIII")

def test_romannumerals_162():
  assert_equal(ConvertNumbers(162).romannumerals(), "CLXII")

def test_romannumerals_2000():
  assert_equal(ConvertNumbers(2000).romannumerals(), "MM")