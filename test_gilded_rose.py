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
    def test_quality_degrades_twice_as_fast_after_sell_in(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9, "FAIL: Expected quality to decrease by 2 but it decreased by 1")

    # Logical Test 2
    def test_quality_never_negative(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, -1, "FAIL: Expected quality to be non-negative but found negative")

    # Logical Test 3
    def test_backstage_passes_quality_increase_and_drop(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21, "FAIL: Expected +2 increase but found different value")
        self.assertEqual(items[1].quality, 22, "FAIL: Expected +3 increase but found different value")
        self.assertEqual(items[2].quality, 1, "FAIL: Expected quality to drop to 0 but found different value")

    # Syntax Error Test
    def test_calling_non_existent_method(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        self.assertTrue(hasattr(gilded_rose, "non_existent_method"), "FAIL: Expected method to exist but it doesn't")

if __name__ == '__main__':
    unittest.main()
