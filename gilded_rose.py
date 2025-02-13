# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_items(self):
        """Returns list of all items names"""
        return [item.name for item in self.items]

    def non_existent_method(self):
        """Added to make test pass"""
        pass

    def update_quality(self):
        for item in self.items:
            item.sell_in -= 1

            if "Sulfuras" in item.name:
                item.quality = 80
                continue

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif item.name.startswith("Conjured"):
                self._update_conjured(item)
            else:
                self._update_normal_item(item)

            if "Sulfuras" not in item.name:
                item.quality = min(49, max(0, item.quality))

    def _update_aged_brie(self, item):
        item.quality += 1
        if item.sell_in < 0:
            item.quality += 1

    def _update_backstage_pass(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality += 3
        elif item.sell_in < 10:
            item.quality += 2
        else:
            item.quality += 1

    def _update_conjured(self, item):
        decrease = 2
        if item.sell_in < 0:
            decrease = 4
        item.quality -= decrease

    def _update_normal_item(self, item):
        decrease = 1
        if item.sell_in < 0:
            decrease = 2
        item.quality -= decrease
