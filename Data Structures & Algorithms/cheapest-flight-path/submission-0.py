from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_map = defaultdict(list)

        for from_i, to_i, price_i in flights:
            flight_map[from_i].append((to_i, price_i))

        seen_stops = defaultdict(int)
        heap = []
        heappush(heap, [0, k, src]) # price, stops, source

        while heap:
            price, stops, city = heappop(heap)

            if city == dst:
                return price
            elif stops < 0:
                continue
            elif city in seen_stops and seen_stops[city] >= stops:
                """
                There is no point visiting
                Because previous number of stops is larger then current stops and 
                its taking same path -
                so you had more options previously -
                No point to explore it again - 
                It will be more expensive
                So avoiding it - to optimize the solution
                """
                continue

            seen_stops[city] = stops

            for nei, neiPrice in flight_map[city]:
                heappush(heap, [price + neiPrice, stops-1, nei])

        return -1
