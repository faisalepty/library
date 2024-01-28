def CalculateFine(currentDate, returnDate):
    daysOverdue = max(0, (currentDate - returnDate).days)
    fine = 20 * daysOverdue
    return fine
