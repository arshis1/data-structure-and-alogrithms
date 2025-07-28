#program that prints all permutatons of n coin tosses*/
#2powern
nbr_coins = input("Number of coins")
print("nbr of coins", nbr_coins, type(nbr_coins))
answer = []
def coins(depth, nbr_coins, output):
    # print(str(depth) + " " + output )
    if depth == int(nbr_coins):
        answer.append(output)

        return
    coins(depth+1, nbr_coins, output+'h')
    coins(depth+1,nbr_coins,  output +'t')

coins(0, nbr_coins, "")
print(answer)



