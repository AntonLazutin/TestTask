class CoinsRiddle:
    def __init__(self, N: int, w: int, d: int, P: int) -> None:
        self.num_of_baskets = N
        self.coin_w = w
        self.false_w = d
        self.picked_w = P
        self.__prog_sum = None
        self.__number_of_false_basket = None

    def count_progression_sum(self) -> None:
        self.__prog_sum = self.coin_w*self.num_of_baskets*(self.num_of_baskets-1)/2-self.picked_w

    def get_basket_number(self):
        if (self.__prog_sum > 0):
            self.__number_of_false_basket = self.__prog_sum / self.false_w
        else:
            self.__number_of_false_basket = self.num_of_baskets

    def calculate_solution(self) -> None:
        self.count_progression_sum()
        self.get_basket_number()

    def get_solution(self) -> int:
        return int(self.__number_of_false_basket)


solution = CoinsRiddle(N=10, w=25, d=8, P=1125)
solution.calculate_solution()
print(f"Фальшивые монеты находятся в корзине под номером {solution.get_solution()}")
