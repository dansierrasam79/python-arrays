# detect pattern of colors
patterns = ["a", "b", "b"]
color1 = ["red", "green", "green"]
color2 = ["red", "green", "greenn"]
pattern_color={}
for i in range(len(patterns)):
    pattern_color[patterns[i]] = color1[i]
final_pattern = []
for color in color2:
    for k,v in pattern_color.items():
        if color == v:
            final_pattern.append(k)
if final_pattern == patterns:
    print(True)
else:
    print(False)