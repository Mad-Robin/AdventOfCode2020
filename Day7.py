class Bags:
    def __init__(self, rule):
        rule = rule.rstrip().replace('.', '').split(' contain ')
        self.desc = rule[0]
        contents = rule[1].split(',')
        contents_dict = {}
        for i in range(0, len(contents)):
            if contents[i] == 'no other bags':
                contents_dict[contents[i]] = 0
            else:
                value = "".join([i for i in contents[i] if i.isdigit()])
                key = "".join([i for i in contents[i] if not i.isdigit()]).lstrip()
                if key.endswith('bag'):
                    key = key.replace('bag', 'bags')
                contents_dict[key] = value
        self.contents = contents_dict


def check_bag_contents(bag_name, bag_dict):
    possibilities = 0
    for each_bag in bag_dict[bag_name]:
        if each_bag == 'shiny gold bags':
            possibilities += 1
        elif each_bag != 'no other bags':
            possibilities += check_bag_contents(each_bag, bag_dict)
        else:
            possibilities += 0
    return possibilities


def bag_within_bag(bag_name, bag_dict):
    quant = 0
    for bag_parent in bag_dict[bag_name]:
        upper_range = int(bag_dict[bag_name][bag_parent])
        for i in range(0, upper_range):
            quant += 1
            if bag_parent != 'no other bags':
                quant += bag_within_bag(bag_parent, bag_dict)
    return quant


def main():
    bags = []
    with open("Inputs/day7.txt", "r") as file:
        for line in file:
            bags.append(Bags(line))

    bag_dict = {}
    for bag in bags:
        bag_dict[bag.desc] = bag.contents

    result = 0
    for bag in bags:
        if check_bag_contents(bag.desc, bag_dict) > 0:
            result += 1

    print(result)

    print(bag_within_bag('shiny gold bags', bag_dict))


if __name__ == '__main__':
    main()
