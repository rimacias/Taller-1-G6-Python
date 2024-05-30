class DestinationList:
    def __init__(self):
        self.favorites = {'Paris': 500, 'NYC': 600}

    def getExtraCost(self, destination):
        return self.favorites.get(destination, 0)


class Passenger:
    def __init__(self, num):
        self.num = num

    def validNumber(self):
        return self.num is int and self.num > 0

    def forHereDiscount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2
        # TODO: add more discount levels if needed
        else:
            return 0.0


class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def isValidTotalTime(self):
        return self.dur is int and self.dur > 0

    def getFee(self):
        return 200 if self.dur < 7 else 0

    def getPromotion(self):
        return 200 if self.dur > 30 else 0

    def getWeekend(self):
        return 100 if self.dur > 7 else 0


class TripCostCalculator:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.DestinationList = DestinationList()
        self.passenger = Passenger(num)
        self.totalTime = TotalTime(dur)
        self.dist = dist

    def calculateTripCost(self):
        isValidNumber = self.passenger.validNumber()
        isValidTotalTime = self.totalTime.isValidTotalTime()
        if self.dist is str and isValidNumber and isValidTotalTime:
            return -1
        numberTotal = self.costBas
        numberTotal += self.DestinationList.getExtraCost(self.dist)
        numberTotal += self.totalTime.getFee()
        numberTotal -= self.totalTime.getPromotion()

        discount = self.passenger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)


def main():
    destination = "Paris"
    passengers = 5
    flightTime = 10

    calculator = TripCostCalculator(destination, passengers, flightTime)
    cost = calculator.calculateTripCost()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()
