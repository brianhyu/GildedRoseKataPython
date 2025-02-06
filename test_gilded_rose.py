# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # My own tests:
    # Logical Test 1
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item(name="ConjuredItem", sell_in=2, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6, "Conjured items should degrade twice as fast")

    # Logical Test 2
    def test_quality_never_negative(self):
        items = [Item(name="ABC", sell_in=5, quality=0.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "FAIL: Expected quality to be non-negative")

    # LogicalTest 3
    def test_quality_never_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=49.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLess(items[0].quality, 50, "FAIL: Expected quality to not exceed 50")

    # Syntax Error Test
    def test_calling_non_existent_method(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        self.assertTrue(hasattr(gilded_rose, "non_existent_method"), "FAIL: Expected method to exist but it doesn't")

if __name__ == '__main__':
    unittest.main()
