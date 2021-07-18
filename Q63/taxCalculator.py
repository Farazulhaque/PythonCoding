def main():
    print("\t\tPersonal Income tax Calculator")
    print("Valid Filing Statuses (0 = Unmarried Filer, 1 = Married Filing Jointly, 2 = Head of Household)\n")
    filing_status = int(input("Enter the filing status: "))
    income = float(input("Enter your taxable income: "))

    if filing_status == 0:
        if income < 9951:
            tax = 0
        elif income < 40526:
            tax = (9951 * 0.10) + (income - 9951) * 0.12
        elif income < 86376:
            tax = (9951 * 0.10) + (40526 - 9951) * \
                0.12 + (income - 40526) * 0.22
        elif income < 164926:
            tax = (9951 * 0.10) + (40526 - 9951) * 0.12 + \
                (86376 - 40526) * 0.22 + (income - 86376) * 0.24
        elif income < 209426:
            tax = (9951 * 0.10) + (40526 - 9951) * 0.12 + (86376 - 40526) * \
                0.22 + (164926 - 86376) * 0.24 + (income - 164926) * 0.32
        elif income < 523601:
            tax = (9951 * 0.10) + (40526 - 9951) * 0.12 + (86376 - 40526) * 0.22 + \
                (164926 - 86376) * 0.24 + (209426 - 164926) * \
                0.32 + (income - 209426) * 0.35
        elif income >= 523601:
            tax = (9951 * 0.10) + (40526 - 9951) * 0.12 + (86376 - 40526) * 0.22 + (164926 - 86376) * \
                0.24 + (209426 - 164926) * 0.32 + (523601 - 209426) * \
                0.35 + (income - 523601) * 0.35
        print("Your income tax fo 2021 will be: ${:.2f}".format(tax))

    elif filing_status == 1:
        if income < 19901:
            tax = 0
        elif income < 81501:
            tax = (19901 * 0.10) + (income - 19901) * 0.12
        elif income < 172751:
            tax = (19901 * 0.10) + (81501 - 19901) * \
                0.12 + (income - 81501) * 0.22
        elif income < 329851:
            tax = (19901 * 0.10) + (81501 - 19901) * 0.12 + \
                (172751 - 81501) * 0.22 + (income - 172751) * 0.24
        elif income < 418851:
            tax = (19901 * 0.10) + (81501 - 19901) * 0.12 + (172751 - 81501) * \
                0.22 + (329851 - 172751) * 0.24 + (income - 329851) * 0.32
        elif income < 628301:
            tax = (19901 * 0.10) + (81501 - 19901) * 0.12 + (172751 - 81501) * 0.22 + \
                (329851 - 172751) * 0.24 + (418851 - 329851) * \
                0.32 + (income - 418851) * 0.35
        elif income >= 628301:
            tax = (19901 * 0.10) + (81501 - 19901) * 0.12 + (172751 - 81501) * 0.22 + (329851 - 172751) * \
                0.24 + (418851 - 329851) * 0.32 + (628301 - 418851) * \
                0.35 + (income - 628301) * 0.35
        print("Your income tax fo 2021 will be: ${:.2f}".format(tax))

    elif filing_status == 2:
        if income < 14201:
            tax = 0
        elif income < 54201:
            tax = (14201 * 0.10) + (income - 14201) * 0.12
        elif income < 86351:
            tax = (14201 * 0.10) + (54201 - 14201) * \
                0.12 + (income - 54201) * 0.22
        elif income < 164901:
            tax = (14201 * 0.10) + (54201 - 14201) * 0.12 + \
                (86351 - 54201) * 0.22 + (income - 86351) * 0.24
        elif income < 209401:
            tax = (14201 * 0.10) + (54201 - 14201) * 0.12 + (86351 - 54201) * \
                0.22 + (164901 - 86351) * 0.24 + (income - 164901) * 0.32
        elif income < 523601:
            tax = (14201 * 0.10) + (54201 - 14201) * 0.12 + (86351 - 54201) * 0.22 + \
                (164901 - 86351) * 0.24 + (209401 - 164901) * \
                0.32 + (income - 209401) * 0.35
        elif income >= 523601:
            tax = (14201 * 0.10) + (54201 - 14201) * 0.12 + (86351 - 54201) * 0.22 + (164901 - 86351) * \
                0.24 + (209401 - 164901) * 0.32 + (523601 - 209401) * \
                0.35 + (income - 523601) * 0.35
        print("Your income tax fo 2021 will be: ${:.2f}".format(tax))

    else:
        print("Input error in filing status or income. Processing stopped")


main()
