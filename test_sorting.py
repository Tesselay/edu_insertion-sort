from unittest import TestCase
from main import insertionSort


class TestSorting(TestCase):

    def test_pinf_listsA(self):
        aa = [1, 5, 8, 2, 11, 9, 7, 14, 15]
        ab = [33, 23, 15, 8, 99, 15, 15, 12, 3]
        ac = [111, 24, 55, 63, 44, 88, 18, 1, 25]
        ad = [99, 88, 77, 65, 40, 25, 19, 17, 13]

        print("PINF LISTS A")

        aa = insertionSort(aa)
        ab = insertionSort(ab)
        ac = insertionSort(ac)
        ad = insertionSort(ad)

        aa_sorted = [1, 2, 5, 7, 8, 9, 11, 14, 15]
        ab_sorted = [3, 8, 12, 15, 15, 15, 23, 33, 99]
        ac_sorted = [1, 18, 24, 25, 44, 55, 63, 88, 111]
        ad_sorted = [13, 17, 19, 25, 40, 65, 77, 88, 99]

        self.assertEqual(aa, aa_sorted, "Should be of same order")
        self.assertEqual(ab, ab_sorted, "Should be of same order")
        self.assertEqual(ac, ac_sorted, "Should be of same order")
        self.assertEqual(ad, ad_sorted, "Should be of same order")

    def test_pinf_listsB(self):
        ba = [1, 4, 7, 8, 11, 3, 15, 16, 17]
        bb = [22, 25, 45, 3, 1, 8, 15, 1, 9, 22]
        bc = [99, 74, 55, 12, 65, 98, 8, 11, 23]
        bd = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        print("PINF LISTS B")

        ba = insertionSort(ba)
        bb = insertionSort(bb)
        bc = insertionSort(bc)
        bd = insertionSort(bd)

        ba_sorted = [1, 3, 4, 7, 8, 11, 15, 16, 17]
        bb_sorted = [1, 1, 3, 8, 9, 15, 22, 22, 25, 45]
        bc_sorted = [8, 11, 12, 23, 55, 65, 74, 98, 99]
        bd_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertEqual(ba, ba_sorted, "Should be of same order")
        self.assertEqual(bb, bb_sorted, "Should be of same order")
        self.assertEqual(bc, bc_sorted, "Should be of same order")
        self.assertEqual(bd, bd_sorted, "Should be of same order")
