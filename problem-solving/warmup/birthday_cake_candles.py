def count_tallest_candles(candles: list) -> int:
    return candles.count(max(candles))


candles_count = int(input().strip())
candles = list(map(int, input().strip().split()))
print(count_tallest_candles(candles))
