class Train:
    trainStatus = {"information": "No information yet !"}
    noOfSeats = 100

    def __init__(self, isBookTicket):
        self.bookTicket = isBookTicket

    def bookTickets(self): 
        return "Ticket booked!" if self.bookTicket else "Ticket wasn't booked."

    def trailInfo(self): 
        return self.__class__.trainStatus  # Accessing the class attribute

# Creating an instance of Train
myTicket = Train(True)

# Printing results
print(f"Book tickets status: {myTicket.bookTicket} \n"
      f"Number of seats: {Train.noOfSeats} \n"
      f"\t{myTicket.bookTickets()} \n"
      f"\t{myTicket.trailInfo()}")
