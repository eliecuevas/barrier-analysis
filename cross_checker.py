from audioop import cross
from response_class import Response
from condom_structures import master, master_list

total_list = []

for large in master.keys():
    total_list.append(large)
    temp = []
    for small in master[large].keys():
        temp.append(small)
    total_list.append(temp)

reference = dict()
count = 1

for i in range(len(total_list)):
    if isinstance(total_list[i], str):
        reference[count] = total_list[i]
        count += 1
    elif isinstance(total_list[i], list):
        for j in range(len(total_list[i])):
            reference[count] = total_list[i][j]
            count += 1

'''
REFERENCE DICT in string value:

    1: Completeness - Is the response filled to completion?
        2: Complete
        3: Incomplete

    4: Sexual Frequency - How often respondent had sex in year before pandemic
        5: Several times per week
        6: Several times per month
        7: Never
        8: Several times per year
    
    9: Condom Use Frequency - How often respondent used condoms during sex in year before pandemic
        10: Every time
        11: About half of the time
        12: Never
        13: More than half of the time
        14: Less than half of the time
    
    15: Amount of sexual Partners - How many sexual partners respondent had in year before pandemic
        16: 5-10
        17: One
        18: 2 to 5
        19: More than 10

    20: Pregnancy Prevention Concern - Whether or not preventing pregnancy is a concern during sex for respondent
        21: Yes
        22: No
    
    23: STI Prevention Concern - Whether or not preventing STI is a concern during sex for respondent
        24: Yes
        25: No
    
    26: Confidence - Is respondent confident they can use a condom correctly
        27: Strongly Agree
        28: Neither Agree Nor Disagree
        29: Agree
        30: Strongly Disagree
        31: Disagree

    32: New Partner and Condom - How likely respondent would use a condom when having sex with a new sexual partner
        33: I would likely use a condom when I have sex with a new partner
        34: I am not sure I would use a condom when I have sex with a new partner
        35: I would likely NOT use a condom when having sex with a new partner
    
    36: Condom reducing pleasure - Does putting on a condom reduce sexual pleasure for respondent
        37: Strongly Disagree
        38: Strongly Agree
        39: Neither Agree nor Disagree
        40: Disagree
        41: Agree
    
    42: Easy condom negotiation - Does it feel easy for respondent to have a conversation with sexual partner about using condoms
        43: Always
        44: About half of the time
        45: Most of the time
        46: Rarely
        47: Never
    
    48: Why no condom - Reasons respondent cites for not using condoms
        49: Other
        50: Chose another form of contraception
        51: Was trying to conceive
        52: Condom not available
        53: Interferting with spontaneity
        54: Pressure from partner
        55: Difficulty putting it on
        56: Decided condom was not necessary
        57: Felt uncomfortable talking about it with partner
        58: Loss of intimacy
        59: Loss of sensation
        60: Texture/smell of condom
        61: Interruption of Sex
        62: Loss of erection
        63: I always use a condom/this question does not apply to me
    
    64: Pleasure enhancing devices - Pleasure enhancing devices enhances respondent's sexual pleasure
        65: Strongly Agree
        66: I do not use pleasure-enhancing devices
        67: Agree
        68: Strongly disagree
        69: Neither agree nor disagree
        70: Disagree
    
    71: Interest in applicator - Respondent is interested in trying novel applicator
        72: Strongly Agree
        73: Agree
        74: Disagree
        75: Strongly Disagree
        76: Neither Agree nor Disagree
    
    77: Reasons for interest in applicator - why respondent wants to try applicator
        78: Other
        79: To feel confident that I have applied the condom correctly
        80: To help apply the condom as quickly as possible
        81: To enhance stimulation to the penis while putting on condom
        82: To help maintain erection
    
    83: Reasons for no interest in applicator - why respondent does not want to try applicator
        84: Other
        85: I don't see the point
        86: It would take too much time
        87: Added interruption/inconvenience
        88: Cost
    
    89: Interest in multi-layer condom - respondent is interested in trying multi-layer condom
        90: Agree
        91: Strongly Agree
        92: Disagree
        93: Strongly Disagree
        94: Neither agree nor disagree
    
    95: Reasons for MLC interest - why respondent is interest in trying multi-layer condom
        96: Other
        97: To enhance stimulation to the person receiving penetration during sex
        98: To help apply the condom quickly
        99: To help maintain erection
        100: To enhance stimulation to the penis during sex

    101: Reasons for no MLC interest - why respondent is not interested in trying multi-layer condom
        102: Other
        103: It would take too much time
        104: Added interruption/inconvenience
        105: Cost
        106: I don't see the point

    107: Which one - which of the two responses (MLC, applicator) sounds most appealing to respondent
        108: Both
        109: Perforated Package with Tabs that allows Condom Application
        110: Neither
        111: Multi-Layer Lubricated Condom
    
    113: Age - age of respondent
        114: 30-39 years
        115: 40-49 years
        116: 18-29 years
        117: 50-59 years
        118: 60-69 years
        119: 70-79 years

    120: Country - country respondent lives in
        121: United States
        122: Nigeria
        123: Jamaica
        124: Dominican Republic
        125: Burkina Faso
        126: South Sudan
        127: Belize
        128: Kenya
        129: Suriname
        130: United Kingdom
        131: India
        132: Belgium
        133: Bhutan
        134: Laos
        135: Uruguay
        136: Lesotho
        137: Burma
        138: Mexico
        139: Haiti
        140: Canada
        141: Thailand
        142: Liberia
        143: Germany
        144: Switzerland
        145: Uganda
        146: Madagascar
        147: Uzbekistan
        148: Iran
        149: Papua New Guinea
        150: Costa Rica
        151: Trinidad and Tobago
        152: Philippines
        153: Namibia
        154: China
        155: Indonesia
        156: Burundi
        157: Vietnam
        158: Mauritania
        159: Mozambique
        160: Botswana
        161: Eritrea
        162: Malaysia
        163: Kazakhstan
        164: Cambodia
        165: Bolivia
        166: Guyana
        167: Barbados
        168: Guatemala
        169: Venezuela
        170: Angola
        171: Central African Republic
        172: Moldova
        173: Luxembourg
        174: Zambia
        175: Malawi
        176: Democratic Republic of the Congo
        177: South Africa
        178: Denmark
        179: Australia
        180: Nicaragua
        181: Macedonia
        182: Turkmenistan
        183: Cameroon
        184: Mongolia
        185: Zimbabwe
        186: Sri Lanka
        187: France
        188: New Zealand
        189: Comoros
        190: Senegal
        191: Togo
        192: Georgia
        193: Kyrzygstan
        194: Russia
        195: Belarus
        196: Sweden
        197: Spain
        198: Brazil
        199: Hungary
    
    200: relationship status - relationship status of the respondent
        201: Other
        202: Non-monogamous relationship
        203: Single- dating
        204: Single- not dating
        205: Monogamous relationship
        206: Open relationship
    
    207: gender identity - gender identity of respondent
        208: Man
        209: Woman
        210: Prefer not to answer
        211: Non-Binary/Gender Fluid
    
    212: transgender - Does the respondent identify as transgender
        213: No
        214: Prefer not to Answer
        215: Yes
    
    216: Sexual Orientation - Respondent's Sexual Orientation
        217: Bisexual
        218: Prefer not to Answer
        219: Heterosexual
        220: Homosexual/Gay
        221: Other
    
    222: Race - What race(s)/ethnic identities respondent identifies with
        223: Other
        224: Non-Hispanic White
        225: Black, Afro-Caribbean or African American
        226: Asian/Pacific Islander
        227: Prefer not to Answer
        228: Latinx
        229: Native American or American Indian
    
    230: Economic situation - respondent's economic situation
        231: I cover expenses, with the ability to indulge
        232: I never worry about covering expenses and indulge often
        233: I cover expenses comfortably
        234: I meet basic needs, but carefully watch my spending
        235: I struggle to make ends meet
        236: Prefer not to answer
    
    237: Religion's importance - If religious beliefs influence any of respondent's answers to the questions in this survey
        238: No
        239: Yes
        240: Prefer not to Answer
    
    241: Disability yes/no - Does the respondent identify as someone with disabilities
        242: No
        243: Yes
        244: Prefer not to Answer
    
    245: Disabilities - Disabilities Respondent claims to have (if any)
        246: Other
        247: Mental Health
        248: Mobility
        249: Vision
        250: Prefer not to Answer
        251: Cognitive
        252: Communication
        253: Hearing
        254: Dexterity
    
'''

def test_reference():
    if reference == {1: 'completeness', 2: 'Complete', 3: 'Incomplete', 4: 'sf', 5: 'Several times per week', 6: 'Several times per month', 7: 'Never', 8: 'Several times per year', 9: 'cuf', 10: 'Every time', 11: 'About half of the time', 12: 'Never', 13: 'More than half of the time', 14: 'Less than half of the time', 15: 'asp', 16: '5-10', 17: 'One', 18: '2 to 5', 19: 'More than 10', 20: 'ppc', 21: 'Yes', 22: 'No', 23: 'sti', 24: 'Yes', 25: 'No', 26: 'confidence', 27: 'Strongly Agree', 28: 'Neither Agree Nor Disagree', 29: 'Agree', 30: 'Strongly Disagree', 31: 'Disagree', 32: 'lucnp', 33: 'I would likely use a condom when I have sex with a new partner.', 34: 'I am not sure I would use a condom when I have sex with a new partner.', 35: 'I would likely NOT use a condom when having sex with a new partner.', 36: 'poce', 37: 'Strongly Disagree', 38: 'Strongly Agree', 39: 'Neither Agree Nor Disagree', 40: 'Disagree', 41: 'Agree', 42: 'ecn', 43: 'Always', 44: 'About half of the time', 45: 'Most of the time', 46: 'Rarely', 47: 'Never', 48: 'wnc', 49: 'Other', 50: 'Chose another form of contraception', 51: 'Was trying to conceive', 52: 'Condom not available', 53: 'Interfering with spontaneity', 54: 'Pressure from partner', 55: 'Difficulty putting it on', 56: 'Decided condom was not necessary', 57: 'Felt uncomfortable talking about it with partner', 58: 'Loss of intimacy', 59: 'Loss of sensation', 60: 'Texture/smell of the condom', 61: 'Interruption of sex', 62: 'Loss of erection', 63: 'I always use a condom/this question does not apply to me', 64: 'ped', 65: 'Strongly agree', 66: 'I do not use pleasure-enhancing devices', 67: 'Agree', 68: 'Strongly disagree', 69: 'Neither agree nor disagree', 70: 'Disagree', 71: 'itp1', 72: 'Strongly agree', 73: 'Agree', 74: 'Disagree', 75: 'Strongly disagree', 76: 'Neither agree nor disagree', 77: 'rfi1', 78: 'Other', 79: 'To feel confident that I have applied the condom correctly', 80: 'To help apply the condom as quickly as possible', 81: 'To enhance stimulation to the penis while putting on condom', 82: 'To help maintain erection', 83: 'rfn1', 84: 'Other', 85: "I don't see the point", 86: 'It would take too much time', 87: 'Added interruption/inconvenience', 88: 'Cost', 89: 'itp2', 90: 'Agree', 91: 'Strongly agree', 92: 'Disagree', 93: 'Strongly disagree', 94: 'Neither agree nor disagree', 95: 'rfi2', 96: 'Other', 97: 'To enhance stimulation to the person receiving penetration during sex', 98: 'To help apply the condom quickly', 99: 'To help maintain erection', 100: 'To enhance stimulation to the penis during sex', 101: 'rfn2', 102: 'Other', 103: 'It would take too much time', 104: 'Added interruption/inconvenience', 105: 'Cost', 106: "I don't see the point", 107: 'aa', 108: 'Both the Perforated Package with Tabs and the Multi-Layer Lubricated Condom', 109: 'Perforated Package with Tabs that Allows Condom Application', 110: 'Neither', 111: 'Multi-Layer Lubricated Condom', 112: 'explainwhy', 113: 'age', 114: '30-39 years', 115: '40-49 years', 116: '18-29 years', 117: '50-59 years', 118: '60-69 years', 119: '70-79 years', 120: 'country', 121: 'United States', 122: 'Nigeria', 123: 'Jamaica', 124: 'Dominican Republic', 125: 'Burkina Faso', 126: 'South Sudan', 127: 'Belize', 128: 'Kenya', 129: 'Suriname', 130: 'United Kingdom', 131: 'India', 132: 'Belgium', 133: 'Bhutan', 134: 'Laos', 135: 'Uruguay', 136: 'Lesotho', 137: 'Burma', 138: 'Mexico', 139: 'Haiti', 140: 'Canada', 141: 'Thailand', 142: 'Liberia', 143: 'Germany', 144: 'Switzerland', 145: 'Uganda', 146: 'Madagascar', 147: 'Uzbekistan', 148: 'Iran', 149: 'Papua New Guinea', 150: 'Costa Rica', 151: 'Trinidad and Tobago', 152: 'Philippines', 153: 'Namibia', 154: 'China', 155: 'Indonesia', 156: 'Burundi', 157: 'Vietnam', 158: 'Mauritania', 159: 'Mozambique', 160: 'Botswana', 161: 'Eritrea', 162: 'Malaysia', 163: 'Kazakhstan', 164: 'Cambodia', 165: 'Bolivia', 166: 'Guyana', 167: 'Barbados', 168: 'Guatemala', 169: 'Venezuela', 170: 'Angola', 171: 'Central African Republic', 172: 'Moldova', 173: 'Luxembourg', 174: 'Zambia', 175: 'Malawi', 176: 'Congo, Democratic Republic of the', 177: 'South Africa', 178: 'Denmark', 179: 'Australia', 180: 'Nicaragua', 181: 'Macedonia', 182: 'Turkmenistan', 183: 'Cameroon', 184: 'Mongolia', 185: 'Zimbabwe', 186: 'Sri Lanka', 187: 'France', 188: 'New Zealand', 189: 'Comoros', 190: 'Senegal', 191: 'Togo', 192: 'Georgia', 193: 'Kyrgyzstan', 194: 'Russia', 195: 'Belarus', 196: 'Sweden', 197: 'Spain', 198: 'Brazil', 199: 'Hungary', 200: 'rs', 201: 'Other', 202: 'Non-monogamous relationship', 203: 'Single- dating', 204: 'Single- not dating', 205: 'Monogamous relationship', 206: 'Open relationship', 207: 'gi', 208: 'Man', 209: 'Woman', 210: 'Prefer Not to Answer', 211: 'Non-Binary/Gender Fluid', 212: 'trans', 213: 'No', 214: 'Prefer Not to Answer', 215: 'Yes', 216: 'so', 217: 'Bisexual', 218: 'Prefer Not to Answer', 219: 'Heterosexual', 220: 'Homosexual/Gay', 221: 'Other', 222: 'race', 223: 'Other', 224: 'Non-Hispanic White', 225: 'Black, Afro-Caribbean or African American', 226: 'Asian/Pacific Islander', 227: 'Prefer Not to Answer', 228: 'Latinx', 229: 'Native American or American Indian', 230: 'econ', 231: 'I cover expenses, with the ability to indulge', 232: 'I never worry about covering expenses and indulge often', 233: 'I cover expenses comfortably', 234: 'I meet basic needs, but carefully watch my spending', 235: 'I struggle to make ends meet', 236: 'Prefer not to answer', 237: 'god', 238: 'No', 239: 'Yes', 240: 'Prefer Not to Answer', 241: 'dis', 242: 'No', 243: 'Yes', 244: 'Prefer Not to Answer', 245: 'disabilities', 246: 'Other', 247: 'Mental Health', 248: 'Mobility', 249: 'Vision', 250: 'Prefer Not to Answer', 251: 'Cognitive', 252: 'Communication', 253: 'Hearing', 254: 'Dexterity'}:
        return (True)
    else:
        return (False)


# print(master["country"].keys())
# print (reference)

question_nums = {1,4,9,15,20,23,26,32,36,42,48,64,71,77,83,89,95,101,107,113,120,200,207,212,216,222,230,237,241,245}

def obtain(response, number):
    if number == 1:
        return response.completeness
    elif number == 4:
        return response.sf
    elif number ==  9:
        return response.cuf 
    elif number ==  15:
        return response.asp
    elif number ==  20:
        return response.ppc 
    elif number ==  23:
        return response.sti 
    elif number ==  26:
        return response.confidence
    elif number ==  32:
        return response.lucnp 
    elif number ==  36:
        return response.poce 
    elif number ==  42:
        return response.ecn 
    elif number ==  48:
        return response.wnc
    elif number ==  64:
        return response.ped
    elif number ==  71:
        return response.itp1 
    elif number ==  77:
        return response.rfi1
    elif number ==  83:
        return response.rfn1
    elif number ==  89:
        return response.itp2
    elif number ==  95:
        return response.rfi2 
    elif number ==  101:
        return response.rfn2 
    elif number ==  107:
        return response.aa 
    elif number ==  113:
        return response.age
    elif number ==  120:
        return response.country
    elif number ==  200:
        return response.rs
    elif number ==  207:
        return response.gi 
    elif number ==  212:
        return response.trans 
    elif number ==  216:
        return response.so
    elif number ==  222:
        return response.race
    elif number ==  230:
        return response.econ 
    elif number ==  237:
        return response.god
    elif number ==  241:
        return response.dis
    elif number ==  245:
        return response.disabilities


'''
Structure of the  Cross-Check Program:
Inputs list and int:    one arbitrarily large list of lists of tuples (each tuple of length 2), where the tuples are two numbers,
                            the first being the question # and the second being the response # of what is to be the independent variable(s). 
                            To cross check between answers, just put in more tuples, tuples in the same sublist is 'or' , and in differing sublists is 'and'

                        integer should be a question #, that is the desired dependent variable

'''

def cross_check(independent, dependent):
    '''
    independent: arbitrary list of lists of tuples (each of length 2 containing only ints)
    dependent: int
    '''

    if dependent not in question_nums:
        raise ValueError
    
    for list1 in independent:
        for tuple1 in list1:
            if len(tuple1) != 2:
                raise ValueError
            if tuple1[0] not in question_nums:
                raise ValueError
            if tuple1[1] not in range(1, 255) or tuple[1] in question_nums:
                raise ValueError

    relevant = set(master_list)
    list_relevant = []
    none_tracker = 0

    for large_variable in independent:
        temp = set()
        for variable in large_variable:
            temp = temp.union(master[reference[variable[0]]][reference[variable[1]]])
        list_relevant.append(temp.copy())

    for variable in list_relevant:
        relevant = relevant.intersection(variable)

    
    result_dict = {"Other" : 0}
    result_pct = dict()
    total_number = len(relevant)
    results = []

    for response in relevant:
        answer = obtain(response, dependent)
        if isinstance(answer, str):
            if "Other:" in answer:
                result_dict["Other"] += 1
            elif answer in result_dict.keys():
                result_dict[answer] += 1
            else:
                result_dict[answer] = 1
        if isinstance(answer, list):
            if answer == []:
                none_tracker += 1
            else:
                for item in answer:
                    if "Other:" in item:
                        result_dict["Other"] += 1
                    elif item in result_dict.keys():
                        result_dict[item] += 1
                    else:
                        result_dict[item] = 1
        elif answer == None:
            none_tracker += 1
    
    total_number = total_number - none_tracker
    if result_dict["Other"] == 0:
        del result_dict["Other"]
    
    for result in result_dict:
        result_pct[result] = result_dict[result] / total_number

    result = "RESPONSE BREAKDOWN \nOnly valid if this says True -> *" + str(test_reference()) + "* \n\ninputs: \n"
    for list1 in independent:
        result += "[\n"
        for tuple1 in list1:
            result += "\t[ " + str(tuple1[0]) + " , " + str(tuple1[1]) + " ] \n"
        result += "]\n\n"
    result += "\n \ndesired output: " + str(dependent) + "\n \n \n"
    result += "results: \n \nOut of " + str(total_number) + " relevant responses \n\n"
    for response in result_dict:
        answer = str(result_dict[response]) +  " (" + str(result_pct[response]*100)[:4] + "%) " + "answered " + response + "\n"
        results.append(answer)
        result += answer

    return result, results, str(total_number)




#print (cross_check([[(113, 116)], [(120, 121)]], 107 )[0]) # takes 18-29 year olds in the united states, and sees which new approaches they are interested in
#print (cross_check([[(216, 220), (216, 217)]], 89)[0]) # takes homosexuals and bisexuals, sees how interested they are in trying the multi-layer condom
#print (cross_check([[(9,14) , (9,12), (9, 11)], [(32,35)]] , 107)[0]) #takes anyone that uses condoms half or less of the time, and that also would likely not use a condom with a new partner, and sees what they approaches they are interested in
# print (cross_check([[(9,14) , (9,12)]] , 89)[0]) #takes anyone that uses condoms half or less of the time, and their interest in the multi-layer condom
# print (cross_check([ [(36,41), (36,38)], [(71, 73), (71, 72)] ] , 77)[0]) # takes anyone that agrees that condoms reduce sexual pleasure and those who are interested in the applicator, and sees the reasons they are interested in the applicator

# print (cross_check([[(200,203), (200, 206), (200, 201), (200, 202), (200, 204)], [(23,24)], [(32,33)]], 42)[0])
# print (cross_check([ [()]]))


# print (cross_check([[(9,11), (9,10), (9,13)], [(36,38), (36, 41)]] , 89)[0])
#print (cross_check([[(26, 28), (26, 31), (26, 30)]], 71)[0])
#print (cross_check([[(23,25)]], 9)[0])

# print (cross_check([[(216, 219)], [(36, 41)]], 48)[0])

# for num in [71, 77, 83, 89, 95, 101, 48, 36]:
#     print (reference[num] + "\n\n")
#     print (cross_check([[(64,68), (64, 70)]], num)[0])
#     print ("\n\n\n")

