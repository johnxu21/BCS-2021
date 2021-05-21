def open_file():
    """This function opens the file and returns a file object"""
    while True:
        prompt = input("Enter Input File Name: ")
        try:
            file_ = open(prompt, 'r')
            break
        except:
            print("Enter Valid File Name!")
    return file_


def process_file(open_object):
    """This function processes the file"""
    try:
        low_income = 'WB_LI '
        lower_middle = 'WB_LMI'
        upper_middle = 'WB_UMI'
        high_income = 'WB_HI '
        year = input("Enter Year: ")
        menu = """
        1 - Low income
        2 - Lower middle income
        3 - upper middle income
        4 - high income 
        """
        income_level = input(f"{menu} \nEnter income Level: ")
        count = 0
        total = 0

        # variables used in the maximum and minimum
        countries = []
        percentages = []

        for line in open_object:
            # comparing the year inputs
            if year == line[88:92]:
                if income_level == '1':
                    if line[51:57] == low_income:
                        pos = line[58:61]
                        percent = float(pos)
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
                elif income_level == '2':
                    if line[51:57] == lower_middle:
                        pos = line[58:61]
                        percent = float(pos)
                        total += percent
                        count += 1
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
                elif income_level == '3':
                    if line[51:57] == upper_middle:
                        pos = line[58:61]
                        percent = float(pos)
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
                elif income_level == '4':
                    if line[51:57] == high_income:
                        pos = line[58:61]
                        percent = float(pos)
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
        print(f'There are {count} countries found')
        print(f'The average is {round(total / count, 1)}')
        print("")
        max_value = max(percentages)
        min_value = min(percentages)

        dic = dict(zip(countries, percentages))
        mx =[k for k, v in dic.items() if v == max_value]
        mn =[k for k,v in dic.items() if v == min_value]
        print(f"The following have the maximum value of {max_value}")
        for i in mx:
            print(i)
        print(f"The following have the minimum value of {min_value}")
        for i in mn:
            print(i)
    except:
        print("Invalid Inputs")


def main():
    """This func calls the open_file function and process_file function"""
    handle = open_file()
    process_file(handle)


main()
