# try except
# finally
# rise


def find_cheaters(users):
    print("Start searching")
    # iter by users
    # logic to find cheaters
    cheaters_found = []
    return cheaters_found or None
    # if not cheaters_found:
    #     raise ValueError("Cheaters does not exist")


def logic_if_cheaters_not_found(users):
    ...


users_list = []

cheaters = find_cheaters(users_list)

if cheaters is None:
    logic_if_cheaters_not_found(users_list)

# try:
#     cheaters = find_cheaters(users_list)
# except ValueError as err:
#     print("Handled err", err)
#     logic_if_cheaters_not_found(users_list)

#
#
#
# try:
#     cheaters = find_cheaters(users_list)
# except ValueError:
#     logic_if_cheaters_not_found(users_list)
#
#
# print("Works")
