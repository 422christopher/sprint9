import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(adjectives, nouns):

    first = random.choice(adjectives)
    second = random.choice(nouns)

    return str(first) + ' ' + str(second)

# def random_float(min_val, max_val):
#     return random.uniform(min_val, max_val)

# def random_bowling_score():
#     return random.randint(0,300)

# def silly_tuple():
#     return (random_phrase(), round(random.uniform(1,5), 1), random_bowling_score())

# def silly_tuple_list(num_tuples):
#     tuple_list = []
#     for i in range(num_tuples):
#         tuple_list.append(silly_tuple())
#     return tuple_list

# print(silly_tuple_list(4))
# print(silly_tuple_list(2))

# def null_count(df):
#     return df.isna().sum().sum()

if __name__ == '__main__':
    pass
    # print(random_phrase(adjectives, nouns))