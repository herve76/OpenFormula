import unittest

from objects import Number, CellReference, RangeReference
from maths import of_abs, of_acos, of_acosh, of_acot, of_acoth, of_asin
from maths import of_asinh, of_atan, of_atan2, of_atanh, of_ceiling
from maths import of_combin, of_combina, of_cos, of_cosh, of_cot, of_coth
from maths import of_countblank, of_countif, of_degrees, of_even, of_exp
from maths import of_fact, of_floor, of_gcd, of_gcd_add, of_int, of_iseven
from maths import of_isodd, of_lcm, of_lcm_add, of_ln, of_log, of_log10, of_mod
from maths import of_mround, of_multinomial, of_odd, of_pi, of_power, of_product
from maths import of_quotient, of_radians, of_rand, of_randbetween, of_round
from maths import of_rounddown, of_roundup, of_seriessum, of_sign, of_sin, of_sinh
from maths import of_sqrt, of_sqrtpi, of_sum, of_sumif, of_sumsq, of_tan
from maths import of_tanh, of_trunc


class TestOpenFormulaMaths(unittest.TestCase):

#Mathematicals functions
    def test_of_abs(self):
        self.assertEqual(of_abs(Number("2")), "ABS(2)")
        self.assertEqual(of_abs("A1"), "ABS([.A1])")
        self.assertRaises(TypeError, of_abs, 2)

    def test_of_acos(self):
        self.assertEqual(of_acos(Number("2")), "ACOS(2)")
        self.assertEqual(of_acos("A1"), "ACOS([.A1])")
        self.assertRaises(TypeError, of_acos, 2)

    def test_of_acosh(self):
        self.assertEqual(of_acosh(Number("2")), "ACOSH(2)")
        self.assertEqual(of_acosh("A1"), "ACOSH([.A1])")
        self.assertRaises(TypeError, of_acosh, 2)

    def test_of_acot(self):
        self.assertEqual(of_acot(Number("2")), "ACOT(2)")
        self.assertEqual(of_acot("A1"), "ACOT([.A1])")
        self.assertRaises(TypeError, of_acot, 2) 

    def test_of_acoth(self):
        self.assertEqual(of_acoth(Number("2")), "ACOTH(2)")
        self.assertEqual(of_acoth("A1"), "ACOTH([.A1])")
        self.assertRaises(TypeError, of_acoth, 2)    

    def test_of_asin(self):
        self.assertEqual(of_asin(Number("2")), "ASIN(2)")
        self.assertEqual(of_asin("A1"), "ASIN([.A1])")
        self.assertRaises(TypeError, of_asin, 2)  

    def test_of_asinh(self):
        self.assertEqual(of_asinh(Number("2")), "ASINH(2)")
        self.assertEqual(of_asinh("A1"), "ASINH([.A1])")
        self.assertRaises(TypeError, of_asinh, 2)  

    def test_of_atan(self):
        self.assertEqual(of_atan(Number("2")), "ATAN(2)")
        self.assertEqual(of_atan("A1"), "ATAN([.A1])")
        self.assertRaises(TypeError, of_atan, 2)  

    def test_of_atan2(self):
        self.assertEqual(of_atan2(Number("1"), "A1"), "ATAN2(1 ; [.A1])")
        self.assertRaises(TypeError, of_atan2, 2, 2)

    def test_of_atanh(self):
        self.assertEqual(of_atanh(Number("2")), "ATANH(2)")
        self.assertEqual(of_atanh("A1"), "ATANH([.A1])")
        self.assertRaises(TypeError, of_atanh, 2) 

    def test_of_ceiling(self):
        self.assertEqual(of_ceiling(Number(2), Number(4)), "CEILING(2 ; 4)")
        self.assertEqual(of_ceiling(Number(1), Number(2), Number(3)), "CEILING(1 ; 2 ; 3)")
        self.assertEqual(of_ceiling(Number(1), Number(2), "A1"), "CEILING(1 ; 2 ; [.A1])")
        self.assertRaises(TypeError, of_ceiling, 2, 3)

    def test_of_combin(self):
        self.assertEqual(of_combin(Number("1"), "A1"), "COMBIN(1 ; [.A1])")
        self.assertRaises(TypeError, of_combin, 2, 3)

    def test_of_combina(self):
        self.assertEqual(of_combina(Number("1"), "A1"), "COMBINA(1 ; [.A1])")
        self.assertRaises(TypeError, of_combina, 2, 3)

    def test_of_cos(self):
        self.assertEqual(of_cos(Number("2")), "COS(2)")
        self.assertEqual(of_cos("A1"), "COS([.A1])")
        self.assertRaises(TypeError, of_cos, 2)

    def test_of_cosh(self):
        self.assertEqual(of_cosh(Number("2")), "COSH(2)")
        self.assertEqual(of_cosh("A1"), "COSH([.A1])")
        self.assertRaises(TypeError, of_cosh, 2)

    def test_of_cot(self):
        self.assertEqual(of_cot(Number("2")), "COT(2)")
        self.assertEqual(of_cot("A1"), "COT([.A1])")
        self.assertRaises(TypeError, of_cot, 2)

    def test_of_coth(self):
        self.assertEqual(of_coth(Number("2")), "COTH(2)")
        self.assertEqual(of_coth("A1"), "COTH([.A1])")
        self.assertRaises(TypeError, of_coth, 2)

    def test_of_countblank(self):
        self.assertEqual(of_countblank("A1:B2"), "COUNTBLANK([.A1:.B2])")
        self.assertRaises(TypeError, of_countblank, 2)

    def test_of_countif(self):
        self.assertEqual(of_countif("A1:B2", Number("3")), "COUNTIF([.A1:.B2];3)")
        self.assertRaises(TypeError, of_countif, 2)

    def test_of_degrees(self):
        self.assertEqual(of_degrees(Number("2")), "DEGREES(2)")
        self.assertEqual(of_degrees("A1"), "DEGREES([.A1])")
        self.assertRaises(TypeError, of_degrees, 2)

    def test_of_even(self):
        self.assertEqual(of_even(Number("2")), "EVEN(2)")
        self.assertEqual(of_even("A1"), "EVEN([.A1])")
        self.assertRaises(TypeError, of_even, 2)

    def test_of_exp(self):
        self.assertEqual(of_exp(Number("2")), "EXP(2)")
        self.assertEqual(of_exp("A1"), "EXP([.A1])")
        self.assertRaises(TypeError, of_exp, 2)

    def test_of_fact(self):
        self.assertEqual(of_fact(Number("2")), "FACT(2)")
        self.assertEqual(of_fact("A1"), "FACT([.A1])")
        self.assertRaises(TypeError, of_fact, 2)

    def test_of_floor(self):
        self.assertEqual(of_floor(Number(2), Number(4)), "FLOOR(2 ; 4)")
        self.assertEqual(of_floor(Number(1), Number(2), Number(3)), "FLOOR(1 ; 2 ; 3)")
        self.assertEqual(of_floor(Number(1), Number(2), "A1"), "FLOOR(1 ; 2 ; [.A1])")
        self.assertRaises(TypeError, of_floor, 2, 3)

    def test_of_gcd(self):
        self.assertEqual(of_gcd("A1:B2"), "GCD([.A1:.B2])")
        self.assertEqual(of_gcd("A1:B2", "C3:D4"), "GCD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_gcd, 2)

    def test_of_gcd_add(self):
        self.assertEqual(of_gcd_add("A1:B2"), "GCD_ADD([.A1:.B2])")
        self.assertEqual(of_gcd_add("A1:B2", "C3:D4"), "GCD_ADD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_gcd_add, 2)

    def test_of_int(self):
        self.assertEqual(of_int(Number("2")), "INT(2)")
        self.assertEqual(of_int("A1"), "INT([.A1])")
        self.assertRaises(TypeError, of_int, 2)

    def test_of_iseven(self):
        self.assertEqual(of_iseven(Number("2")), "ISEVEN(2)")
        self.assertEqual(of_iseven("A1"), "ISEVEN([.A1])")
        self.assertRaises(TypeError, of_iseven, 2)

    def test_of_isodd(self):
        self.assertEqual(of_isodd(Number("2")), "ISODD(2)")
        self.assertEqual(of_isodd("A1"), "ISODD([.A1])")
        self.assertRaises(TypeError, of_isodd, 2)

    def test_of_lcm(self):
        self.assertEqual(of_lcm("A1:B2"), "LCM([.A1:.B2])")
        self.assertEqual(of_lcm("A1:B2", "C3:D4"), "LCM([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_lcm, 2)

    def test_of_lcm_add(self):
        self.assertEqual(of_lcm_add("A1:B2"), "LCM_ADD([.A1:.B2])")
        self.assertEqual(of_lcm_add("A1:B2", "C3:D4"), "LCM_ADD([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_lcm_add, 2)

    def test_of_ln(self):
        self.assertEqual(of_ln(Number("2")), "LN(2)")
        self.assertEqual(of_ln("A1"), "LN([.A1])")
        self.assertRaises(TypeError, of_ln, 2)

    def test_of_log(self):
        self.assertEqual(of_log("B2",Number("3")), "LOG([.B2] ; 3)")
        self.assertRaises(TypeError, of_log, 2)

    def test_of_log10(self):
        self.assertEqual(of_log10(Number("2")), "LOG10(2)")
        self.assertEqual(of_log10("A1"), "LOG10([.A1])")
        self.assertRaises(TypeError, of_log10, 2)

    def test_of_mod(self):
        self.assertEqual(of_mod("B2",Number("3")), "MOD([.B2] ; 3)")
        self.assertRaises(TypeError, of_mod, 2, 3)

    def test_of_mround(self):
        self.assertEqual(of_mround("B2",Number("3")), "MROUND([.B2] ; 3)")
        self.assertRaises(TypeError, of_mround, 2, 3)

    def test_of_multinomial(self):
        self.assertEqual(of_multinomial("A1:B2"), "MULTINOMIAL([.A1:.B2])")
        self.assertEqual(of_multinomial("A1:B2", "C3:D4"), "MULTINOMIAL([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_multinomial, 2)

    def test_of_odd(self):
        self.assertEqual(of_odd(Number("2")), "ODD(2)")
        self.assertEqual(of_odd("A1"), "ODD([.A1])")
        self.assertRaises(TypeError, of_odd, 2)
        
    def test_of_pi(self):
        self.assertEqual(of_pi(), "PI()")

    def test_of_power(self):
        self.assertEqual(of_power("B2",Number("3")), "POWER([.B2] ; 3)")
        self.assertRaises(TypeError, of_power, 2, 3)

    def test_of_product(self):
        self.assertEqual(of_product("A1:B2"), "PRODUCT([.A1:.B2])")
        self.assertEqual(of_product("A1:B2", "C3:D4"), "PRODUCT([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_product, 2)

    def test_of_quotient(self):
        self.assertEqual(of_quotient("B2",Number("3")), "QUOTIENT([.B2] ; 3)")
        self.assertRaises(TypeError, of_quotient, 2, 3)

    def test_of_radians(self):
        self.assertEqual(of_radians(Number("2")), "RADIANS(2)")
        self.assertEqual(of_radians("A1"), "RADIANS([.A1])")
        self.assertRaises(TypeError, of_radians, 2)
        
    def test_of_rand(self):
        self.assertEqual(of_rand(), "RAND()")
        
    def test_of_randbetween(self):
        self.assertEqual(of_randbetween("B2",Number("3")), "RANDBETWEEN([.B2] ; 3)")
        self.assertRaises(TypeError, of_randbetween, 2, 3)

    def test_of_round(self):
        self.assertEqual(of_round(Number("1")), "ROUND(1)")
        self.assertEqual(of_round(Number("1"), "A1"), "ROUND(1 ; [.A1])")
        self.assertRaises(TypeError, of_round, 2)

    def test_of_rounddown(self):
        self.assertEqual(of_rounddown(Number("1")), "ROUNDDOWN(1)")
        self.assertEqual(of_rounddown(Number("1"), "A1"), "ROUNDDOWN(1 ; [.A1])")
        self.assertRaises(TypeError, of_rounddown, 2)

    def test_of_roundup(self):
        self.assertEqual(of_roundup(Number("1")), "ROUNDUP(1)")
        self.assertEqual(of_roundup(Number("1"), "A1"), "ROUNDUP(1 ; [.A1])")
        self.assertRaises(TypeError, of_roundup, 2)

    def test_of_seriessum(self):
        self.assertEqual(of_seriessum(Number("1"),"A1", Number("3"), "A1:B2" ), "SERIESSUM(1 ; [.A1] ; 3 ; [.A1:.B2])")
        self.assertRaises(TypeError, of_seriessum, 2, 3, 4, 5)

    def test_of_sign(self):
        self.assertEqual(of_sign(Number("2")), "SIGN(2)")
        self.assertEqual(of_sign("A1"), "SIGN([.A1])")
        self.assertRaises(TypeError, of_sign, 2)

    def test_of_sin(self):
        self.assertEqual(of_sin(Number("2")), "SIN(2)")
        self.assertEqual(of_sin("A1"), "SIN([.A1])")
        self.assertRaises(TypeError, of_sin, 2)

    def test_of_sinh(self):
        self.assertEqual(of_sinh(Number("2")), "SINH(2)")
        self.assertEqual(of_sinh("A1"), "SINH([.A1])")
        self.assertRaises(TypeError, of_sinh, 2)

    def test_of_sqrt(self):
        self.assertEqual(of_sqrt(Number("2")), "SQRT(2)")
        self.assertEqual(of_sqrt("A1"), "SQRT([.A1])")
        self.assertRaises(TypeError, of_sqrt, 2)

    def test_of_sqrtpi(self):
        self.assertEqual(of_sqrtpi(Number("2")), "SQRTPI(2)")
        self.assertEqual(of_sqrtpi("A1"), "SQRTPI([.A1])")
        self.assertRaises(TypeError, of_sqrtpi, 2)

    def test_of_sum(self):
        self.assertEqual(of_sum("A1:B2"), "SUM([.A1:.B2])")
        self.assertEqual(of_sum("A1:B2", "C3:D4"), "SUM([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_sum, 2)

    def test_of_sumif(self):
        self.assertEqual(of_sumif("A1:B2", Number("3")), "SUMIF([.A1:.B2];3)")
        self.assertEqual(of_sumif("A1:B2", Number("3") ,"C3:D4"), "SUMIF([.A1:.B2];3;[.C3:.D4])")
        self.assertRaises(TypeError, of_sumif, 2, 3)

    def test_of_sumsq(self):
        self.assertEqual(of_sumsq("A1:B2"), "SUMSQ([.A1:.B2])")
        self.assertEqual(of_sumsq("A1:B2", "C3:D4"), "SUMSQ([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, of_sumsq, 2)

    def test_of_tan(self):
        self.assertEqual(of_tan(Number("2")), "TAN(2)")
        self.assertEqual(of_tan("A1"), "TAN([.A1])")
        self.assertRaises(TypeError, of_tan, 2)

    def test_of_tanh(self):
        self.assertEqual(of_tanh(Number("2")), "TANH(2)")
        self.assertEqual(of_tanh("A1"), "TANH([.A1])")
        self.assertRaises(TypeError, of_tanh, 2)

    def test_of_trunc(self):
        self.assertEqual(of_trunc("B2",Number("3")), "TRUNC([.B2] ; 3)")
        self.assertRaises(TypeError, of_trunc, 2, 3)





if __name__ == '__main__':
    unittest.main()


                          


                          
