weapons=["missile"];
hostile_nations=["nano"];
Americans=["robert"];
enemies=[["america","nano"]];
sells=[
    ["robert","nano","missile"],
    ["colonel", "india", "missile"]

];
def isCriminal(name):
    for key,value in enumerate(sells):
        if name == value[0]:
            if value[1] in hostile_nations:
                if value[2] in weapons:
                    print(f"{name} is Criminal")
                    return
    print(f"{name} not criminal");

isCriminal("colonel")
