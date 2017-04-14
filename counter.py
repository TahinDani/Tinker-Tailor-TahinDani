def counter(player_num, syllables_num):
    players = list(range(1, player_num+1))
    print(players)
    out = [] 
    for i in range(syllables_num-1, 30, syllables_num):
        if i > len(players)-1:
            print("break")
            i = 0
        print("i is:", i)
        print("player poped:", players[i])
        out.append(players[i])
        print("players:",players)
        print("out:",out)


def counter2(player_num, syllables_num):
    players = list(range(1, player_num+1))
    print(players)
    out = []
    for i in players:
        if i%syllables_num == 0:
            print("player out:", i)
            out.append(i)
            players.remove(i)
            print(players)
            print("out:", out)


def counter3(player_num, syllables_num):
    players = list(range(1, player_num+1))
    print(players)
    out = players[syllables_num-1::syllables_num]
    print("out:", out)


def counter4(player_num, syllables_num):
    players = list(range(1, player_num+1))
    result = []
    i = 1
    while len(result) < len(players):
        j = i*(syllables_num)-1
        result.append(players[j])
        print(result)
        i += 1
        if j>=len(players)-1:
            i=1


# i = player_num-((player_num//syllables_num)*syllables_num)


def counter6(player_num, syllables_num):
    players = list(range(1, player_num+1))
    result = []
    skip = syllables_num-1
    i = skip
    while len(result) < player_num:
        try:
            result.append(players.pop(i))
            print(result)
            print(players)
            i = (i + skip) % len(players)
        except (ZeroDivisionError):
            break


def josephus(ls, skip):
    players = list(range(1, ls+1))
    skip -= 1  # pop automatically skips the dead guy
    idx = skip
    while len(players) > 1:
        players.pop(idx)  # kill prisoner at idx
        idx = (idx + skip) % len(players)
    print('survivor: ', players[0])


counter6(42, 15)
print("----josephus:")
josephus(42, 15)



# public class Josephus {
#     public static void main(String[] args) {
#         int m = Integer.parseInt(args[0]);
#         int n = Integer.parseInt(args[1]);

#         // initialize the queue
#         Queue<Integer> queue = new Queue<Integer>();
#         for (int i = 1; i <= n; i++)
#             queue.enqueue(i);

#         while (!queue.isEmpty()) {
#             for (int i = 0; i < m-1; i++)
#                 queue.enqueue(queue.dequeue());
#             StdOut.print(queue.dequeue() + " ");
#         } 
#         StdOut.println();
#     }
# }