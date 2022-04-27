from operator import concat
import random
from typing import List
#generates 20 random numbers 1-361
randList = random.choice(range(1,2))
#Now that we have made a random number generator what comes in a draft booster pack?
#What's in a Strixhaven Draft Booster?
#Each pack contains 1 Mystical Archive card (Uncommon, Rare, or Mythic Rare), 
# 1 Lesson card (Common, Rare, or Mythic Rare), 1 Rare or Mythic Rare, 3 Uncommons, and 9 Commons. 
# A traditional foil card of any rarity replaces a Common in 33 percent of Strixhaven Draft Boosters, 
# and a traditional foil Mystical Archive Mythic Rare can be found in less than 1 percent of packs.

#The cards included in a Strixhaven Draft Booster are numbered 1-275.
cardlist = random.sample(range(1,276),15)
#every common card in the card set.
commons = list()
commons += list(range(1,5))
commons += list(range(8,10))
commons += list(range(11,13))
commons += list(range(16,17))
commons += list(range(18,20))
commons += list(range(22,24))
commons += list(range(30,31))
commons += list(range(32,33))
commons += list(range(34,35))
commons += list(range(36,37))
commons += list(range(38,41))
commons += list(range(43,44))
commons += list(range(49,53))
commons += list(range(55,56))
commons += list(range(60,62))
commons += list(range(63,64))
commons += list(range(68,70))
commons += list(range(73,76))
commons += list(range(77,78))
commons += list(range(79,80))
commons += list(range(84,86))
commons += list(range(87,88))
commons += list(range(90,91))
commons += list(range(93,94))
commons += list(range(97,98))
commons += list(range(99,100))
commons += list(range(102,104))
commons += list(range(109,110))
commons += list(range(111,113))
commons += list(range(116,119))
commons += list(range(121,123))
commons += list(range(124,125))
commons += list(range(131,132))
commons += list(range(136,138))
commons += list(range(140,146))
commons += list(range(166,167))
commons += list(range(170,171))
commons += list(range(182,186))
commons += list(range(187,188))
commons += list(range(194,196))
commons += list(range(201,202))
commons += list(range(204,205))
commons += list(range(206,207))
commons += list(range(208,212))
commons += list(range(215,216))
commons += list(range(219,220))
commons += list(range(223,224))
commons += list(range(226,227))
commons += list(range(233,234))
commons += list(range(235,240))
commons += list(range(241,242))
commons += list(range(243,244))
commons += list(range(249,250))
commons += list(range(251,253))
commons += list(range(254,257))
commons += list(range(263,264))
commons += list(range(268,269))
commons += list(range(270,272))
commons += list(range(273,274))
commons += list(range(275,276))
#every uncommon.
uncommons = list()
uncommons += list(range(10,11))
uncommons += list(range(13,14))
uncommons += list(range(15,16))
uncommons += list(range(24,27))
uncommons += list(range(28,29))
uncommons += list(range(31,32))
uncommons += list(range(35,36))
uncommons += list(range(41,42))
uncommons += list(range(45,48))
uncommons += list(range(53,55))
uncommons += list(range(56,57))
uncommons += list(range(59,60))
uncommons += list(range(62,63))
uncommons += list(range(65,66))
uncommons += list(range(70,73))
uncommons += list(range(76,77))
uncommons += list(range(78,79))
uncommons += list(range(88,90))
uncommons += list(range(91,93))
uncommons += list(range(100,101))
uncommons += list(range(104,106))
uncommons += list(range(107,108))
uncommons += list(range(110,111))
uncommons += list(range(114,116))
uncommons += list(range(123,124))
uncommons += list(range(125,127))
uncommons += list(range(129,130))
uncommons += list(range(132,133))
uncommons += list(range(134,136))
uncommons += list(range(138,140))
uncommons += list(range(162,163))
uncommons += list(range(169,171))
uncommons += list(range(175,179))
uncommons += list(range(186,187))
uncommons += list(range(188,189))
uncommons += list(range(190,191))
uncommons += list(range(193,194))
uncommons += list(range(197,199))
uncommons += list(range(200,201))
uncommons += list(range(202,203))
uncommons += list(range(207,208))
uncommons += list(range(212,214))
uncommons += list(range(216,217))
uncommons += list(range(218,219))
uncommons += list(range(220,221))
uncommons += list(range(222,223))
uncommons += list(range(224,226))
uncommons += list(range(227,228))
uncommons += list(range(229,230))
uncommons += list(range(231,232))
uncommons += list(range(242,243))
uncommons += list(range(247,248))
uncommons += list(range(250,251))
uncommons += list(range(257,259))
uncommons += list(range(260,263))
#every rare and mythic.
# 5,6,7,14,17,20,21,27,29,33,37,42,48
# 57,58,66,67,82,83,86,94,95,96,98,101,108,113,119,120,127,128,130,133
# 146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,163,165,167,168
# 172,173,174,179,180,181,189,191,192,196,199,203,205,214,217,221,228,230,232,234
# 240,244,245,246,248,253,259,264,265,266,267,269,272,274
raresOrMythics = list()
raresOrMythics+= list(range(5,8))
raresOrMythics+= list(range(14,15))
raresOrMythics+= list(range(17,18))
raresOrMythics+= list(range(20,22))
raresOrMythics+= list(range(27,28))
raresOrMythics+= list(range(29,30))
raresOrMythics+= list(range(33,34))
raresOrMythics+= list(range(37,38))
raresOrMythics+= list(range(42,43))
raresOrMythics+= list(range(48,49))
raresOrMythics+= list(range(57,59))
raresOrMythics+= list(range(66,68))
raresOrMythics+= list(range(82,84))
raresOrMythics+= list(range(86,87))
raresOrMythics+= list(range(94,97))
raresOrMythics+= list(range(98,99))
raresOrMythics+= list(range(101,102))
raresOrMythics+= list(range(108,109))
raresOrMythics+= list(range(113,114))
raresOrMythics+= list(range(119,121))
raresOrMythics+= list(range(127,129))
raresOrMythics+= list(range(130,131))
raresOrMythics+= list(range(133,134))
raresOrMythics+= list(range(146,162))
raresOrMythics+= list(range(163,164))
raresOrMythics+= list(range(165,166))
raresOrMythics+= list(range(167,169))
raresOrMythics+= list(range(172,175))
raresOrMythics+= list(range(179,182))
raresOrMythics+= list(range(189,190))
raresOrMythics+= list(range(191,193))
raresOrMythics+= list(range(196,197))
raresOrMythics+= list(range(199,200))
raresOrMythics+= list(range(203,204))
raresOrMythics+= list(range(205,206))
raresOrMythics+= list(range(214,215))
raresOrMythics+= list(range(217,218))
raresOrMythics+= list(range(221,222))
raresOrMythics+= list(range(228,229))
raresOrMythics+= list(range(230,231))
raresOrMythics+= list(range(232,233))
raresOrMythics+= list(range(234,235))
raresOrMythics+= list(range(240,241))
raresOrMythics+= list(range(244,247))
raresOrMythics+= list(range(248,249))
raresOrMythics+= list(range(253,254))
raresOrMythics+= list(range(259,260))
raresOrMythics+= list(range(264,268))
raresOrMythics+= list(range(269,270))
raresOrMythics+= list(range(272,273))
raresOrMythics+= list(range(274,275))

#all of the mystical archive cards.
mystic = list()
jp=random.sample(range(1,101),1)
if(jp==100):
    print("you got a japanese card!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    mystic+= list(range(64,126))
else:
    mystic+= list(range(1,64))
#Now lets pick random cards from those lists.
randCommons = random.sample(commons,9)
randUncommons = random.sample(uncommons,3)
randRaresOrMythics = random.sample(raresOrMythics,1)
randMystic = random.sample(mystic,1)
print("Your pack contains:")
print(randCommons)
print(randUncommons)
print(randRaresOrMythics)
print(randMystic)