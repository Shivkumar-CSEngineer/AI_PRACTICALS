male_list = ["arjun", "shyam", "ram", "mohan"];
female_list = ["seeta", "hema", "maya"];
parent_list=[["seeta","shyam"],["ram","shyam"],["shyam","maya"],["shyam","hema"],["hema","arjun"],["mohan","arjun"]];

def find_pairs_of_mothor_and_child():
    print("List of mother and there child are as follows")
    for key,value in enumerate(parent_list):
        # print(key," -> ",value)
        if value[0] in female_list:
            print(value)

find_pairs_of_mothor_and_child()


def find_pairs_of_father_and_child():
    print("List of father and there child are as follows")
    for key,value in enumerate(parent_list):
        # print(key," -> ",value)
        if value[0] in male_list:
            print(value)
find_pairs_of_father_and_child()

def find_pairs_of_father_and_child():
    print("List of father and there child are as follows")
    for key,value in enumerate(parent_list):
        # print(key," -> ",value)
        if value[0] in male_list:
            print(value)
find_pairs_of_father_and_child()




