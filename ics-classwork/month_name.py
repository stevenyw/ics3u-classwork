
def main():
    print("Month 1: " + month_name(1))
    print("Month 2: " + month_name(2))
    print("Month 3: " + month_name(3))
    print("Month 4: " + month_name(4))
    print("Month 5: " + month_name(5))
    print("Month 6: " + month_name(6))
    print("Month 7: " + month_name(7))
    print("Month 8: " + month_name(8))
    print("Month 9: " + month_name(9))
    print("Month 10: " + month_name(10))
    print("Month 11: " + month_name(11))
    print("Month 12: " + month_name(12))
    print("Month 43: " + month_name(43))


def month_name(month: int) -> str:
    result = ""
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return "Error"


if __name__ == "__main__":
    main()
