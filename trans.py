import time
score = 0
ac = False
checkscore = "\nCurrent score: {}".format(score)
print("Made by u/roseinabox28 please give me some hugs or pats if you liked this! (Or upvotes, they work too!)")
time.sleep(.5)
print("Welcome I will predict if you are transgender!")
time.sleep(1)
print("Do you frequent subreddits like r/traa or r/egg_IRL just for the memes?")
while ac == False:
    reddit = input("Please answer yes or no:  ")
    if "yes" in reddit:
        #1 point
        score += 5
        print("Okay, most people on there are usually trans or eggs...{}".format("\nCurrent score: {}".format(score)))
        break
    elif "no" in reddit:
        #-1 point
        score += 0
        print("Hmm, I'm not too sure...I'll just call it even...{}".format("\nCurrent score: {}".format(score)))
        break
time.sleep(1.5)
print("Do you sometimes wish you were born with a body with certain sex characteristics?")
while ac == False:
    reddit = input("Please answer yes or no:  ")
    if "yes" in reddit:
        #1 point
        score += 8
        print("That's something that a lot of transgender people resonate with. {}".format("\nCurrent score: {}".format(score)))
        time.sleep(.5)
        print("Do you think that it's just a fetish?")
        while True:
            r = input("please answer yes or no:  ")
            if "yes" in r:
                score += 7
                print("That's valid! Even if you think it's a fetish (it's not), you can still be transgender!{}".format("\nCurrent score: {}".format(score)))
                break
            elif "no" in r:
                score += 5
                print("That's fine! {}".format("\nCurrent score: {}".format(score)))
                break
        break
    elif "no" in reddit:
        #-1 point
        score += -5
        print("Hmm I'm not too sure about this one. You could still be in denial...{}".format("\nCurrent score: {}".format(score)))
        break
time.sleep(1.23)
print("Did(or do) you hate puberty?")
while ac == False:
    reddit = input("Please answer yes or no:  ")
    if "yes" in reddit:
        #1 point
        score += 20
        print("Yeah that's pretty common in trans-folk.{}".format("\nCurrent score: {}".format(score)))
        break
    elif "no" in reddit:
        #-1 point
        score += 2
        print("Not everyone who's trans hates or hated puberty!{}".format("\nCurrent score: {}".format(score)))
        break
time.sleep(1.5)
print("Did you take this test?")
while ac == False:
    reddit = input("Please answer yes or no:  ")
    if "yes" in reddit:
        #1 point
        score += 1000000
        print("Just like with \"Am I gay?\" tests, if you took it you probably are! {}".format("\nCurrent score: {}".format(score)))
        break
    elif "no" in reddit:
        #-1 point
        score += -1000000000
        print("I don't think that's right... You just don't want it to be true...{}".format("\nCurrent score: {}".format(score)))
        break
time.sleep(1.5)
if score > 10000:
    print("You are transgender and are valid!")
elif score < 0:
    print("You must be an egg, or someone that wants all the endings")
