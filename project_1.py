import math



def main():
    '''
    Project Name: Yondu
    Author: Peter Williams
    Due Date: 02/05/2022
    Course: CS1400-X02

    Inputs:
    -------
        - Number of Reavers in crew when making port
        - Total units brought in by crew

    Outputs:
    --------
    (no returned values, only prints)
        - Yondu's share
        - Peter's share
        - Crew's share
        - RBF Amount
    '''

    try:
        # (1) replace pass with your code
        reavers = int(input("How many Reavers: "))
        units = int(input("How many units: "))
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return
    if reavers < 3:
        print("Not enough crew.")
        return
    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    # giving 3 units to each member but Peter and Yondu:
    celebration_units = 3*(reavers - 2)
    # calculate remaining units
    remaining_units = units - celebration_units
    # yondu gets a cut from the take minus the celebration
    yondus_secret_cut = math.floor(remaining_units * .13)
    # peter gets a cut of the take minus the celebration and yondus cut
    remaining_units = remaining_units - yondus_secret_cut
    peters_secret_cut = math.floor(remaining_units * .11)
    # the final take is calculated without peters and yondus cut and the celebration money
    remaining_units = remaining_units - peters_secret_cut

    # try and divide the units evenly
    rbf = 0
    # find the number of units that need to go to the rbf
    while remaining_units % reavers != 0:
        remaining_units = remaining_units - 1
        rbf += 1

    fair_split = remaining_units / reavers

    peters_cut = peters_secret_cut + fair_split
    yondus_cut = yondus_secret_cut + fair_split




    print(f"Yondu's share: {int(yondus_cut)}")
    print(f"Peter's share: {int(peters_cut)}")
    print(f"Crew: {int(fair_split)}")
    print(f"RBF: {int(rbf)}")

if __name__ == "__main__":
    main()
    