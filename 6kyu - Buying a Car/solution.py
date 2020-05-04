#https://www.codewars.com/kata/554a44516729e4d80b000012/train/python
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month = 0
    total_saving = 0
    while startPriceOld + total_saving < startPriceNew:
        month += 1
        if month >= 2 and month % 2 == 0:
            percentLossByMonth += 0.5
        total_saving = month * savingperMonth
        startPriceOld = startPriceOld - (startPriceOld * (percentLossByMonth / 100) )
        startPriceNew = startPriceNew -(startPriceNew * (percentLossByMonth / 100) )
    if startPriceOld + total_saving >= startPriceNew:
        return [month, round(startPriceOld + total_saving - startPriceNew)]
