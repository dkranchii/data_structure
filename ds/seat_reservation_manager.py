import heapq

class SeatManager:
    def __init__(self, n: int):
        """
        Initialize the SeatManager with a heap of seats.
        Each seat is initially unreserved and the seats are numbered from 1 to n.
        """
        # Create a min-heap of available seats
        self.unres = [i for i in range(1, n + 1)]
        heapq.heapify(self.unres)
        
    def reserve(self) -> int:
        """
        Reserve the lowest numbered seat available.
        
        Returns:
            int: The number of the reserved seat.
        """
        return heapq.heappop(self.unres)
        
    def unreserve(self, seatNumber: int) -> None:
        """
        Unreserve a seat, making it available again.
        
        Args:
            seatNumber (int): The number of the seat to unreserve.
        """
        heapq.heappush(self.unres, seatNumber)
