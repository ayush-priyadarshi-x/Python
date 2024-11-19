from random import randint
class Train:
    trainStatus = {"information": "No information yet !"}
    noOfSeats = 100

    def __init__(harry, isBookTicket):
        harry.bookTicket = isBookTicket

    def bookTickets(ayush): 
        return "Ticket booked!" if ayush.bookTicket else "Ticket wasn't booked."

    @staticmethod
    def bookedSeat(): 
        return randint(255, 555)

    def trailInfo(ujjwal): 
        return ujjwal.__class__.trainStatus  # Accessing the class attribute

# Creating an instance of Train
myTicket = Train(True)

# Printing results
print(f"Book tickets status: {myTicket.bookTicket} \n"
      f"Number of seats: {Train.noOfSeats} \n"
      f"\t{myTicket.bookTickets()} \n"
      f"\t{myTicket.trailInfo()}"
      f"\t{myTicket.bookedSeat()}"
      )
