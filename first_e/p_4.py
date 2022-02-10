
dictionary = {

    'Robert_downey':{'Mark':['Tl',8,{'Lenoardo':['Jd',1],
                                     'Alexandra':['Jd',1]}],

                     'Samuel':['Tl',8],

                     'Paul':['Tl',8,{'Fergal':['Sd',4.5]}],

                     'Tom':['Tl',8,{'Jerry':['Jd',1.5],
                                    'James':['Jd',1.5]}]},

    'Anne':{'Chris':['Tl',5,{'James':['Tl',None],
                             'Jennifer':['Sd',3.8],
                             'Scott':['Sd',3.8],
                             'Sophie':['Sd',3.8]}],

            'Pratt':['Tl',5],
            'Emma':['Tl',5,{}],
            'Will':['Tl',5,{'Edge':['Sd',3],
                            'Ryan':['Sd',3.5]}],

            'Smith':['Tl',5,{'Walker':['Sd',2.7],
                             'Diana':['Sd',2.7]}]}

}

data = []
def find_emp_name(dictionary):
    data.extend(dictionary.keys())
    for v in dictionary.values():
        if type(v)== list:
            for i in v:
                if type(i) == dict:
                    data.extend(i.keys())

find_emp_name(dictionary['Robert_downey'])
print("Robert Employee Name:",data)

data.clear()
find_emp_name(dictionary['Anne'])
print("Anne Employee Name:",data)


def exp_4(dictionary):
        for k,v in dictionary.items():
            if type(v) == dict:
                exp_4(v)
            elif type(v) == list:
                for i in v:
                    if type(i) == dict:
                        exp_4(i)

                    if v[1] == None:
                        pass
                    elif v[1] > 4:
                        data.append(k)
data.clear()
exp_4(dictionary)
print(set(data))

def update_exp(dictionary):
    for k,v in dictionary.items():
        if type(v) == dict:
            update_exp(v)
        elif type(v) == list:
            for i in v:
                if type(i) == dict:
                    update_exp(i)
            if v[1] == None:
                pass
            elif(v[1]>=3.5 and v[1]<=4.5):
                v[1]=4.6

update_exp(dictionary)
print("Update Experience:",dictionary)

def check_tl(dictionary):
    for k,v in dictionary.items():
        if type(v) == dict:
            check_tl(v)
        elif type(v) == list:
            for i in v:
                if type(i)==dict:
                    check_tl(i)
            if v[0]=='Tl' and v[1] != None:
                print(k,':',v[1])
            elif v[0]=='Tl' and v[1]==None:
                print(k,':','Na')

check_tl(dictionary)

def check_ex_2(dictionary):
    for k,v in dictionary.items():
        if type(v) == dict:
            check_ex_2(v)
        elif type(v) == list:
            for i in v:
                if type(i) == dict:
                    check_ex_2(i)
            if v[1] == None:
                pass
            elif v[1] >=2:
                data.append(v)
data.clear()
check_ex_2(dictionary)
print("Employee  Less than 2 Years Exp:",data)


def check_tl(dictionary):
    for k,v in dictionary.items():
        if type(v)== dict:
            check_tl(v)
        elif type(v)== list:
            for i in v:
                if type(i)==dict:
                    check_tl(i)
            if k=="Edge" and v[0]!='Tl':
                v[0]='Tl'


check_tl(dictionary)
print("Edge is tl",dictionary)

smith=[]
def smith_value(dictionary):
    for k,v in dictionary.items():
        if k=='Smith':
            smith.append(v[2])
        elif type(v)==dict:
            smith_value(v)
        elif type(v)==list:
            for i in v:
                if type(i)==dict:
                    smith_value(i)

smith_value(dictionary)
#print(smith)

def ryan(dictionary):
    for k,v in dictionary.items():
        if k=='Ryan':
            v.append(smith)
        elif type(v)==dict:
            ryan(v)
        elif type(v)==list:
            for i in v:
                if type(i)==dict:
                    ryan(i)
        

ryan(dictionary)
dictionary['Anne'].pop('Smith')
print("Assign to ryan:",dictionary)