FEW_SHOT_EXAMPLES = """
Examples 1
Input text:
<text>
Is this any less brainwashed than Americans going to go fight front line infantry for Zelenskyy? Its patriotism/nationalism on either side. Suicide before capture isnt a new thing, and not historically abnormal in war.
</text>
labeled output:
<labeled_text>
<logical_fallacy>Is this any less brainwashed than Americans going to go fight front line infantry for Zelenskyy? </logical_fallacy>Its patriotism/nationalism on either side. Suicide before capture isnt a new thing, and not historically abnormal in war.
</labeled_text>

Examples 2: multiple fallacies with adjacent fallacy tags
Input text:
<text>
I think they didnt have malicious intentions . Weve dealth with Bojo for a while m, hes been playing the lol im just dumb for too long. He isnt dumb, he is malicious to the bone.
</text>
labeled output:
<labeled_text>
I think they didnt have malicious intentions . <logical_fallacy>Weve dealth with Bojo for a while m, hes been playing the lol im just dumb for too long.</logical_fallacy> <credibility_fallacy>He isnt dumb, he is malicious to the bone.</credibility_fallacy>
</labeled_text>

Examples 3
Input text:
<text>
I know what risks I am taking. But man fucking a kg  yo hoholina is sure worth it.And the  was a conflict of mostly professional soldiers there might be a handful of them here but I guess not many.I remain comfy.
</text>
labeled output:
<labeled_text>
I know what risks I am taking.<emotional_fallacy>But man fucking a kg  yo hoholina is sure worth it.</emotional_fallacy>And the  was a conflict of mostly professional soldiers there might be a handful of them here but I guess not many.<emotional_fallacy>I remain comfy.</emotional_fallacy>
</labeled_text>

Examples 4: no fallacies
Input text:
<text>
crazy good hits. trucks driving fast and they still hit
</text>
labeled output:
<labeled_text>
crazy good hits. trucks driving fast and they still hit
</labeled_text>
"""


FEW_SHOT_EXAMPLES_00 = """
"""

FEW_SHOT_EXAMPLES_90_10 = """
Examples 1:
Input text:
<text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</text>
<labeled_text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</labeled_text>

Examples 2:
Input text:
<text>
I dont think so ,myself . LIKE ABSOLUTE BS .
</text>
<labeled_text>
I dont think so ,myself . LIKE ABSOLUTE BS .
</labeled_text>

Examples 3:
Input text:
<text>
Don't count your chickens yet, there is no ceasefire Russia's terms remain the withdraw of all piggies from Kursk, Donetsk, Lugansk, Zaporozhye, and Kherson Then negotiation
</text>
<labeled_text>
Don't count your chickens yet, there is no ceasefire <logical_fallacy>Russia's terms remain the withdraw of all piggies from Kursk, Donetsk, Lugansk, Zaporozhye, and Kherson Then negotiation</logical_fallacy>
</labeled_text>

Examples 4:
Input text:
<text>
The world needs to wake up, read a book, listen to the very few remaining survivors, see the obvious, stand up to that hate. Control the narrative before we slip into darkness once again.
</text>
<labeled_text>
<emotional_fallacy>The world needs to wake up, read a book, listen to the very few remaining survivors, see the obvious, stand up to that hate</emotional_fallacy>. <emotional_fallacy>Control the narrative before we slip into darkness once again</emotional_fallacy>.
</labeled_text>

Examples 5:
Input text:
<text>
Polska annexed Odesa and Lviv.Zelensky and cadre are already dead.
</text>
<labeled_text>
<emotional_fallacy>Polska annexed Odesa and Lviv</emotional_fallacy>.<emotional_fallacy>Zelensky and cadre are already dead.</emotional_fallacy>
</labeled_text>

Examples 6:
Input text:
<text>
R.I.P. TO ALL THE THE LITTLE ANGELES 🇮🇪🇺🇦
</text>
<labeled_text>
R.I.P. TO ALL THE THE LITTLE ANGELES 🇮🇪🇺🇦
</labeled_text>

Examples 7:
Input text:
<text>
I met Fico in 1995 in Komarno, Slovakia. I was an English teacher in that city. He was a wanker then, and hes a wanker now
</text>
<labeled_text>
I met Fico in 1995 in Komarno, Slovakia. I was an English teacher in that city. <credibility_fallacy>He was a wanker then, and hes a wanker now</credibility_fallacy>
</labeled_text>
"""

FEW_SHOT_EXAMPLES_80_20 = """
Examples 1:
Input text:
<text>
Okay, so, there are  entries in your db where there are no officials listed. You should probably post them as another .txt file.
</text>
<labeled_text>
Okay, so, there are  entries in your db where there are no officials listed. You should probably post them as another .txt file.
</labeled_text>

Examples 2:
Input text:
<text>
As much as I support my own Country Canada I support Ukraine 100% with my dieing breath I will support them
</text>
<labeled_text>
As much as I support my own Country Canada I support Ukraine 100% with my dieing breath I will support them
</labeled_text>

Examples 3:
Input text:
<text>
For the Russian anonbelow you can see how they sent the money and why they sent the money.Its distress money for when a family member has to kill their off spring and the family goes into distress.
</text>
<labeled_text>
For the Russian anonbelow you can see how they sent the money and why they sent the money.<emotional_fallacy>Its distress money for when a family member has to kill their off spring and the family goes into distress.</emotional_fallacy>
</labeled_text>

Examples 4:
Input text:
<text>
I guess they do taste and color. A lot.
</text>
<labeled_text>
<emotional_fallacy>I guess they do taste and color</emotional_fallacy>. A lot.
</labeled_text>

Examples 5:
Input text:
<text>
Is there a map anywhere with details on all the oil infrastructure hits?
</text>
<labeled_text>
Is there a map anywhere with details on all the oil infrastructure hits?
</labeled_text>

Examples 6:
Input text:
<text>
R.I.P. TO ALL THE THE LITTLE ANGELES 🇮🇪🇺🇦
</text>
<labeled_text>
R.I.P. TO ALL THE THE LITTLE ANGELES 🇮🇪🇺🇦
</labeled_text>

Examples 7:
Input text:
<text>
Im rooting for Ukrainian terrorists worldwide. Ill donate $ to Sternenko sometime today. Maybe well end up with based ultranationalist and far-right terrorists in Europe and Russia.
</text>
<labeled_text>
<emotional_fallacy>Im rooting for Ukrainian terrorists worldwide.</emotional_fallacy> Ill donate $ to Sternenko sometime today. <emotional_fallacy>Maybe well end up with based ultranationalist and far-right terrorists in Europe and Russia.</emotional_fallacy>
</labeled_text>

Examples 8:
Input text:
<text>
What grid connection will Kalingrad have..
</text>
<labeled_text>
What grid connection will Kalingrad have..
</labeled_text>

Examples 9:
Input text:
<text>
3 out of 10? with painful being what, 1 or 10? Blog/Opinion Piece theres no such thing linked
</text>
<labeled_text>
3 out of 10? with painful being what, 1 or 10? Blog/Opinion Piece theres no such thing linked
</labeled_text>

Examples 10:
Input text:
<text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</text>
<labeled_text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</labeled_text>

Examples 11:
Input text:
<text>
According to X, this guy is a Putin sympathizer, the prime rib of Slovakia, and upset because Ukraine is banning the transit of russian natural gas.
</text>
<labeled_text>
<credibility_fallacy>According to X, this guy is a Putin sympathizer</credibility_fallacy>, the prime rib of Slovakia, and upset because Ukraine is banning the transit of russian natural gas.
</labeled_text>

Examples 12:
Input text:
<text>
This desu. We're seeing the fall of U . SofA
</text>
<labeled_text>
This desu. <emotional_fallacy>We're seeing the fall of U . SofA</emotional_fallacy>
</labeled_text>

Examples 13:
Input text:
<text>
Europeans must provide security . This, thats why this war is unlikely to end IMHO.Kremlin will never agree to station NATO troops near its border in Ukraine.
</text>
<labeled_text>
Europeans must provide security . This, thats why this war is unlikely to end IMHO.Kremlin will never agree to station NATO troops near its border in Ukraine.
</labeled_text>
"""

FEW_SHOT_EXAMPLES_70_30 = """
Examples 1:
Input text:
<text>
Absolutely. Its like Ursula said a couple of years ago - the Russians are running out of microchips stolen from Ukrainian dishwashers so pretty soon they will not be able to make any more missiles. The victory is close.
</text>
<labeled_text>
Absolutely. Its like Ursula said a couple of years ago - <emotional_fallacy>the Russians are running out of microchips stolen from Ukrainian dishwashers so pretty soon they will not be able to make any more missiles.</emotional_fallacy> The victory is close.
</labeled_text>

Examples 2:
Input text:
<text>
Its the same pic from a year ago?
</text>
<labeled_text>
Its the same pic from a year ago?
</labeled_text>

Examples 3:
Input text:
<text>
Reminds me of us Japanese during ww2. Brainwashed to believe that dying for the emperor was righteous
</text>
<labeled_text>
Reminds me of us Japanese during ww2. <emotional_fallacy>Brainwashed to believe that dying for the emperor was righteous</emotional_fallacy>
</labeled_text>

Examples 4:
Input text:
<text>
NO PISS DEALNO WORLD WITHOUT FRIEREN
</text>
<labeled_text>
NO PISS DEALNO WORLD WITHOUT FRIEREN
</labeled_text>

Examples 5:
Input text:
<text>
Is there a map anywhere with details on all the oil infrastructure hits?
</text>
<labeled_text>
Is there a map anywhere with details on all the oil infrastructure hits?
</labeled_text>

Examples 6:
Input text:
<text>
If Ukraine had nuclear weapons wed literally be engulfed in a third world war right now, or living out the aftermath of nuclear strikes.
</text>
<labeled_text>
<logical_fallacy>If Ukraine had nuclear weapons wed literally be engulfed in a third world war right now, or living out the aftermath of nuclear strikes.</logical_fallacy>
</labeled_text>

Examples 7:
Input text:
<text>
Legitimate question: why are Russian troops burning N . Koreans faces to hide theyre N . Korean when the whole world knows they are? Is Russian command telling their soldiers to do so, giving them the impression its mandatory to keep the secret?
</text>
<labeled_text>
<logical_fallacy>Legitimate question: why are Russian troops burning N . Koreans faces to hide theyre N . Korean when the whole world knows they are?</logical_fallacy> Is Russian command telling their soldiers to do so, giving them the impression its mandatory to keep the secret?
</labeled_text>

Examples 8:
Input text:
<text>
Short on tanks again, but other vehicles getting battered. Good stuff.
</text>
<labeled_text>
Short on tanks again, but other vehicles getting battered. Good stuff.
</labeled_text>

Examples 9:
Input text:
<text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</text>
<labeled_text>
The dutch government does not have a winner takes all system but a multi party system where each party gets seats in the parliament equal to the percentage of votes. This means almost always that compromises and working together with different political parties is needed. Its a system that helps a bit against polarization and ignoring minorities. Not saying its perfect though
</labeled_text>

Examples 10:
Input text:
<text>
I guess they do taste and color. A lot.
</text>
<labeled_text>
<emotional_fallacy>I guess they do taste and color</emotional_fallacy>. A lot.
</labeled_text>

Examples 11:
Input text:
<text>
Hit the vodka distilleries, sure way to cause a revolution.
</text>
<labeled_text>
<emotional_fallacy>Hit the vodka distilleries, sure way to cause a revolution.</emotional_fallacy>
</labeled_text>

Examples 12:
Input text:
<text>
The world needs to wake up, read a book, listen to the very few remaining survivors, see the obvious, stand up to that hate. Control the narrative before we slip into darkness once again.
</text>
<labeled_text>
<emotional_fallacy>The world needs to wake up, read a book, listen to the very few remaining survivors, see the obvious, stand up to that hate</emotional_fallacy>. <emotional_fallacy>Control the narrative before we slip into darkness once again</emotional_fallacy>.
</labeled_text>

Examples 13:
Input text:
<text>
As much as I support my own Country Canada I support Ukraine 100% with my dieing breath I will support them
</text>
<labeled_text>
As much as I support my own Country Canada I support Ukraine 100% with my dieing breath I will support them
</labeled_text>

Examples 14:
Input text:
<text>
NO REFUNDS YOU FUCKING PIGS DIE DIE DIE
</text>
<labeled_text>
<emotional_fallacy>NO REFUNDS YOU FUCKING PIGS DIE DIE DIE</emotional_fallacy>
</labeled_text>

Examples 15:
Input text:
<text>
According to X, this guy is a Putin sympathizer, the prime rib of Slovakia, and upset because Ukraine is banning the transit of russian natural gas.
</text>
<labeled_text>
<credibility_fallacy>According to X, this guy is a Putin sympathizer</credibility_fallacy>, the prime rib of Slovakia, and upset because Ukraine is banning the transit of russian natural gas.
</labeled_text>

Examples 16:
Input text:
<text>
He says Make America Great Again, when it's China that's going to be the winner from his "HULK MAD!!!! HULK SMASH!!!!” Strategy.
</text>
<labeled_text>
He says Make America Great Again, when it's China that's going to be the winner from his "HULK MAD!!!! HULK SMASH!!!!” Strategy.
</labeled_text>

Examples 17:
Input text:
<text>
Breaking: Zelenskyy signs the unconditional surrender of his government to the Russian Armed Forces.
</text>
<labeled_text>
<logical_fallacy>Breaking: Zelenskyy signs the unconditional surrender of his government to the Russian Armed Forces.</logical_fallacy>
</labeled_text>

Examples 18:
Input text:
<text>
Picture is a mortar, not kornet atm…
</text>
<labeled_text>
Picture is a mortar, not kornet atm…
</labeled_text>

Examples 19:
Input text:
<text>
Clowns are too afraid of getting nuked!
</text>
<labeled_text>
<emotional_fallacy>Clowns are too afraid of getting nuked</emotional_fallacy>!
</labeled_text>

Examples 20:
Input text:
<text>
I met Fico in 1995 in Komarno, Slovakia. I was an English teacher in that city. He was a wanker then, and hes a wanker now
</text>
<labeled_text>
I met Fico in 1995 in Komarno, Slovakia. I was an English teacher in that city. <credibility_fallacy>He was a wanker then, and hes a wanker now</credibility_fallacy>
</labeled_text>
"""
