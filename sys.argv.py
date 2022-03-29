import sys



def main():
    '''
    Project Name: Library of Congress
    Author: Peter Williams
    Due Date: 03/28/2022
    Course: CS1400-X02

    Inputs:
    -------
        - File from the command line

    Outputs:
    --------
        - novel_summary.txt (file containing summary info about the provided text)
        - novel_text.txt (file containing the ordred texts for each book code provided)
    '''

    # handling sys.argv

    if len(sys.argv) > 2:
        print("Too many arguments provided.")
        return


    # reading in the file
    file = sys.argv[1]

    with open(file, encoding="utf8") as file:
        lines = file.readlines()


    # performing the desired calculations and organization

    org_dict = {}

    for line in lines:
        line_list = line.split(sep="|")
        line_list[1] = int(line_list[1])
        code = line_list[2].strip('\n')
        organize_by_code(line_list, code, org_dict)
        org_dict[f"{code}"]["longest_line"] = determine_longest_line(line_list, code, org_dict)
        org_dict[f"{code}"]["shortest_line"] = determine_shortest_line(line_list, code, org_dict)
        org_dict[f"{code}"]["total_length"] += len(line_list[0])
        org_dict[f"{code}"]["total_lines"] += 1

    # saving the summaries to a file
    with open('novel_summary.txt', 'w') as file:

        for key, _ in sorted(org_dict.items()):
            file.write(f"{key}\n")
            file.write(f"Longest line ({org_dict[key]['longest_line'][1]}): {org_dict[key]['longest_line'][0]}\n")
            file.write(f"Shortest line ({org_dict[key]['shortest_line'][1]}): {org_dict[key]['shortest_line'][0]}\n")
            file.write(f"Average length: {round(org_dict[key]['total_length'] / org_dict[key]['total_lines'])}\n")
            file.write("\n")

    # saving the cleaned text to a file
    with open('novel_text.txt', 'w') as file:
        for key,_ in sorted(org_dict.items()):
            temp_list = sorted(org_dict[key]['raw_data'], key=lambda x: x[1])
            temp_clean = "\n".join([str(item[0]) for item in temp_list])
            file.write(f"{key}\n")
            file.write(temp_clean)
            file.write("\n-----\n")
    return

def organize_by_code(line_list, code, org_dict):
    try:
        org_dict[f"{code}"]["raw_data"].append(line_list)
    except KeyError: # create the new key
        org_dict[f"{code}"] = {}
        org_dict[f"{code}"]["raw_data"] = []
        org_dict[f"{code}"]["raw_data"].append(line_list)
        org_dict[f"{code}"]["longest_line"] = ["",0,0] #initiate the longest line with a length of 1
        org_dict[f"{code}"]["shortest_line"] = line_list
        org_dict[f"{code}"]["total_length"] = 0
        org_dict[f"{code}"]["total_lines"] = 0

def determine_longest_line(line_list, code, org_dict):

    if len(line_list[0]) > len(org_dict[f"{code}"]["longest_line"][0]):
        return line_list
    elif len(line_list[0]) == len(org_dict[f"{code}"]["longest_line"][0]):
        if line_list[1] > org_dict[f"{code}"]["longest_line"][1]:
            return line_list

    return org_dict[f"{code}"]["longest_line"]


def determine_shortest_line(line_list, code, org_dict):

    if len(line_list[0]) < len(org_dict[f"{code}"]["shortest_line"][0]):
        return line_list
    elif len(line_list[0]) == len(org_dict[f"{code}"]["shortest_line"][0]):
        if line_list[1] < org_dict[f"{code}"]["shortest_line"][1]:
            return line_list

    return org_dict[f"{code}"]["shortest_line"]


if __name__ == "__main__":
    main()
