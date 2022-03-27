import sys 
import pprint
import time

def main():

    start = time.time()
    

    # handling sys.argv

    if len(sys.argv) > 2:
        print("Too many arguments provided.")
        return 1
    

    # reading in the file
    
    file = sys.argv[1]

    with open(file, encoding="utf8") as f:
        lines = f.readlines()
    

    # performing the desired calculations and organization

    org_dict = {}

    for line in lines:
        line_list = line.split(sep="|")
        line_list[1] = int(line_list[1])
        code = line_list[2].strip('\n')
        organize_by_code(line_list, code, org_dict)
        org_dict[f"{code}"]["longest_line"] = determine_longest_line(line_list, code, org_dict)
        org_dict[f"{code}"]["shortest_line"] = determine_shortest_line(line_list, code, org_dict)

    for key, _ in org_dict.items():
        print()
        print(f"{key}")
        print(f"Longest line ({org_dict[key]['longest_line'][1]}): {org_dict[key]['longest_line'][0]}")
        print(f"Shortest line ({org_dict[key]['shortest_line'][1]}): {org_dict[key]['shortest_line'][0]}")

    #TODO: create a function for calculating the shortest line 

    print("\n ----------------------------------------")
    print(f"Program executed in {round(time.time() - start)}")


def organize_by_code(line_list, code, org_dict):
    try:
        org_dict[f"{code}"]["raw_data"].append(line_list)
    except KeyError: # create the new key 
        org_dict[f"{code}"] = {}
        org_dict[f"{code}"]["raw_data"] = []
        org_dict[f"{code}"]["raw_data"].append(line_list)
        org_dict[f"{code}"]["longest_line"] = ["",0,0] #initiate the longest line with a length of 1
        org_dict[f"{code}"]["shortest_line"] = line_list #initiate the longest line with a length of 1


def determine_longest_line(line_list, code, org_dict):
    
    if len(line_list[0]) > len(org_dict[f"{code}"]["longest_line"][0]):
        return line_list 
    
    return org_dict[f"{code}"]["longest_line"]


def determine_shortest_line(line_list, code, org_dict):
    
    if len(line_list[0]) < len(org_dict[f"{code}"]["shortest_line"][0]):
        return line_list 
    
    return org_dict[f"{code}"]["shortest_line"]

    
if __name__ == "__main__":
    main()