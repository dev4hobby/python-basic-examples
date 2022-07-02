from collections import defaultdict


class ItemManager:
    def __init__(self, items):
        if not isinstance(items, dict):
            raise TypeError("items must be dictionary")
            self.item_dict = defaultdict(int)
        else:
            self.item_dict = items

    def get_info_by_item(self, item):
        return self.item_dict[item]


class Kiosk:
    def __init__(self, items):
        self.items = defaultdict(int)
        self.item_manager = ItemManager(items)

    def add_item(self, item):
        self.items[item] += 1

    def remove_item(self, item):
        self.items[item] -= 0

    def show_items(self):
        print("--주문 목록--")
        item_list = list()
        for item, count in self.items.items():
            if count == 0:
                continue
            item_list.append({item: count})
        return item_list

    def get_cost(self):
        print("--영수증--")
        cost = 0
        for item, count in self.items.items():
            if count == 0:
                continue
            cost += self.item_manager.get_info_by_item(item) * count
        return cost


if __name__ == "__main__":
    kiosk = Kiosk(items={"빅맥": 4600, "1955버거": 5700, "맥치킨": 3300})
    kiosk.add_item("빅맥")
    kiosk.add_item("빅맥")
    kiosk.add_item("맥치킨")
    print(kiosk.show_items())
    print(kiosk.get_cost())

    kiosk.remove_item("빅맥")
    kiosk.add_item("1955버거")
    print(kiosk.show_items())
    print(kiosk.get_cost())
