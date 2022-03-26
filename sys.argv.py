import sys 
import pprint
import time

def main():
    start = time.time()
    if len(sys.argv) > 2:
        print("Too many arguments provided.")
        return 1
        
    file = sys.argv[1]

    with open(file, encoding="utf8") as f:
        lines = f.readlines()
    
    org_dict = {}

    for line in lines:
        organize_by_code(line, org_dict)
        
        
            
    

    print(org_dict.keys())
    
    print("\n ----------------------------------------")
    print(f"Program executed in {round(time.time() - start)}")


def organize_by_code(line, org_dict):
    temp_list = line.split(sep="|")
    temp_list[1] = int(temp_list[1])
    code = temp_list[2].strip('\n')
    try:
        org_dict[f"{code}"].append(temp_list)
    except KeyError: # create the new key 
        org_dict[f"{code}"] = []
        org_dict[f"{code}"].append(temp_list)

def determine_longest_line(new_line, longest_line):
    if len(new_line) > len(longest_line):
        return new_line 
    
    return longest_line

    
if __name__ == "__main__":
    main()