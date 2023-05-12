
class Mathematician:

    def square_nums(self, nums: list) -> list:
        result = [num ** 2 for num in nums]
        return result
    
    def remove_positives(self, nums: list) -> list:
        result = [num for num in nums if num >= 0]
        return result
    
    def filter_leaps(self, years: list[int]) -> list:
        result = [year for year in years if year % 4 == 0]
        return result




m = Mathematician()

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
