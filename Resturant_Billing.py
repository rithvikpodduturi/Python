print ('----------------------------------------');
print ('-- Welcome to FedUni Roast Dinners!----');
print ('----------------------------------------');
print ('Could I take your name Please ?')
name = input();
print ('And Your Phone Number ?')
phone = input();
cost= 0;
count= 0;
def dinner():
    
    print ('What size dinner would you like? (M)edium, (L)arge or e(X)large');
    size = input();
    meat_name = '';
    meat = 0;
    global cost;
    sides1 = 0;
    sides2 = 0;
    extra_name='';
    extras_name='';
    sides1_name='';
    sides2_name='';

    if(size=='M'):
        print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
        meat = input();
        if(meat == 'B'):
            meat_name = 'Beef '
           
        elif(meat == 'C'):
            meat_name = 'Chicken '
        
        elif(meat == 'P'):
            meat_name = 'Pork '
           
        
        print('Medium dinners come with two sides.');
        print('Available sides are:');
        print('   - (R)oastPotatoes');
        print('   - (C)arrots');
        print('   - (P)eas');
        print('   - (Y)orkshirePudding');
        print('   - (G)ravy');
        print('   - (B)rocolli');
        sides1 =  input();
        if(sides1 == 'R'):
            sides1_name = 'RoastPotatoes '
        elif(sides1 == 'C'):
            sides1_name = 'Carrots '
        elif(sides1 == 'P'):
            sides1_name = 'Peas '
        elif(sides1 == 'Y'):
            sides1_name = 'YorkshirePudding '
        elif(sides1 == 'G'):
            sides1_name = 'Gravy '
        elif(sides1 == 'B'):
            sides1_name = 'Brocolli '
        print('And your next side?');
        sides2 = input();
        if(sides2 == 'R'):
            sides2_name = 'RoastPotatoes '
        elif(sides2 == 'C'):
            sides2_name = 'Carrots '
        elif(sides2 == 'P'):
            sides2_name = 'Peas '
        elif(sides2 == 'Y'):
            sides2_name = 'YorkshirePudding '
        elif(sides2 == 'G'):
            sides2_name = 'Gravy '
        elif(sides2 == 'B'):
            sides2_name = 'Brocolli '   
        cost = cost+10;
        while True:
            print('Thank you. Would you like to add a serve of (M)eat or a (S)side ? (N)0');
            print('thanks.');
            other = input();
            if(other == 'M'):
                print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
                extra = input();
                if(extra == 'B'):
                  extra_name = 'Beef '
                elif(extra == 'C'):
                  extra_name = 'Chicken '
                elif(extra == 'P'):
                  extra_name = 'Pork '
                cost = cost+4;
            elif(other == 'S'):
                print('Available sides are:');
                print('   - (R)oastPotatoes ');
                print('   - (C)arrots ');
                print('   - (P)eas ');
                print('   - (Y)orkshirePudding ');
                print('   - (G)ravy ');
                print('   - (B)rocolli ');
                extras = input();
                if(extras == 'R'):
                   extras_name = 'RoastPotatoesf '
                elif(extras == 'C'):
                   extras_name = 'Carrots '
                elif(extras == 'P'):
                   extras_name = 'Peas '
                elif(extras == 'Y'):
                   extras_name = 'YorkshirePudding '
                elif(extras == 'G'):
                   extras_name = 'Gravy '
                elif(extras == 'B'):
                   extras_name = 'Brocolli '
                cost = cost+2;
            else:
                print('Would You like to (A)dd dinner to your order? (N)o thanks.');
                add_dinner = input();
                if(add_dinner == 'A'):
                    dinner();
                     
                                
                else:
                    print('Thank you',name,phone)
                    print('your Order summary is:',meat_name,sides1_name,sides2_name,extra_name,extras_name)
                    print('Your order comes to: $',cost)
                    print ('--------------------------------------------------')
                    print ('----Thank you to visiting FedUni Roast Dinners!----')
                    print ('---------------------------------------------------')
                    break;

    elif(size=='L'):
        print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
        meat = input();
        if(meat == 'B'):
            meat_name = 'Beef '
        elif(meat == 'C'):
            meat_name = 'Chicken '
        elif(meat == 'P'):
            meat_name = 'Pork '
        print('Large dinners come with three sides.');
        print('Available sides are:');
        print('   - (R)oastPotatoes');
        print('   - (C)arrots');
        print('   - (P)eas');
        print('   - (Y)orkshirePudding');
        print('   - (G)ravy');
        print('   - (B)rocolli');
        sides1 =  input();
        if(sides1 == 'R'):
            sides1_name = 'RoastPotatoesf '
        elif(sides1 == 'C'):
           sides1_name = 'Carrots '
        elif(sides1 == 'P'):
            sides1_name = 'Peas '
        elif(sides1 == 'Y'):
           sides1_name = 'YorkshirePudding '
        elif(sides1 == 'G'):
            sides1_name = 'Gravy '
        elif(sides1 == 'B'):
            sides1_name = 'Brocolli '
        print('And your next side?');
        sides2 = input();
        if(sides2 == 'R'):
            sides2_name = 'RoastPotatoesf '
        elif(sides2 == 'C'):
           sides2_name = 'Carrots '
        elif(sides2 == 'P'):
            sides2_name = 'Peas '
        elif(sides2 == 'Y'):
           sides2_name = 'YorkshirePudding '
        elif(sides2 == 'G'):
            sides2_name = 'Gravy '
        elif(sides2 == 'B'):
            sides2_name = 'Brocolli '
        print('And your next side?');
        sides3 = input();
        if(sides3 == 'R'):
            sides3_name = 'RoastPotatoesf '
        elif(sides3 == 'C'):
           sides3_name = 'Carrots '
        elif(sides3 == 'P'):
            sides3_name = 'Peas '
        elif(sides3 == 'Y'):
           sides3_name = 'YorkshirePudding '
        elif(sides3 == 'G'):
            sides3_name = 'Gravy '
        elif(sides3 == 'B'):
            sides3_name = 'Brocolli '
        cost = cost+15;
        while True:
            print('Thank you. Would you like to add a serve of (M)eat or a (S)side ? (N)0');
            print('thanks.');
            other = input();
            if(other == 'M'):
                print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
                extra = input();
                cost = cost+4;
            elif(other == 'S'):
                print('Available sides are:');
                print('   - (R)oastPotatoes');
                print('   - (C)arrots');
                print('   - (P)eas');
                print('   - (Y)orkshirePudding');
                print('   - (G)ravy');
                print('   - (B)rocolli');
                extra = input();
                cost = cost+2;
            else:
                print('Would You like to (A)dd dinner to your order? (N)o thanks.');
                add_dinner = input();
                if(add_dinner == 'A'):
                    dinner();
                else:
                  print('your Order summary is:'+meat_name+sides1_name+sides2_name+sides3_name)
                  print('Your order comes to: $',cost)
                  print ('--------------------------------------------------');
                  print ('----Thank you to visiting FedUni Roast Dinners!----');
                  print ('---------------------------------------------------');
                break;
    elif(size=='X'):
        print(' Extra Large dinners come with two serves of meat.');
        print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
        meat1 = input();
        if(meat1 == 'B'):
            meat1_name = 'Beef '
        elif(meat1 == 'C'):
            meat1_name = 'Chicken '
        elif(meat1 == 'P'):
            meat1_name = 'Pork '
        print('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
        meat2 = input();
        if(meat2 == 'B'):
            meat2_name = 'Beef '
        elif(meat2 == 'C'):
            meat2_name = 'Chicken '
        elif(meat2 == 'P'):
            meat2_name = 'Pork '
        print('Large dinners come with four sides.');
        print('Available sides are:');
        print('   - (R)oastPotatoes');
        print('   - (C)arrots');
        print('   - (P)eas');
        print('   - (Y)orkshirePudding');
        print('   - (G)ravy');
        print('   - (B)rocolli');
        sides1 =  input();
        if(sides1 == 'R'):
            sides1_name = 'RoastPotatoesf '
        elif(sides1 == 'C'):
            sides1_name = 'Carrots '
        elif(sides1 == 'P'):
            sides1_name = 'Peas '
        elif(sides1 == 'Y'):
            sides1_name = 'YorkshirePudding '
        elif(sides1 == 'G'):
            sides1_name = 'Gravy '
        elif(sides1 == 'B'):
            sides1_name = 'Brocolli '
        print('And your next side?');
        sides2 = input();
        if(sides2 == 'R'):
            sides2_name = 'RoastPotatoesf '
        elif(sides2 == 'C'):
            sides2_name = 'Carrots '
        elif(sides2 == 'P'):
            sides2_name = 'Peas '
        elif(sides2 == 'Y'):
            sides2_name = 'YorkshirePudding '
        elif(sides2 == 'G'):
            sides2_name = 'Gravy '
        elif(sides2 == 'B'):
            sides2_name = 'Brocolli '
        print('And your next side?');
        sides3 = input();
        if(sides3 == 'R'):
            sides3_name = 'RoastPotatoesf '
        elif(sides3 == 'C'):
            sides3_name = 'Carrots '
        elif(sides3 == 'P'):
            sides3_name = 'Peas '
        elif(sides3 == 'Y'):
            sides3_name = 'YorkshirePudding '
        elif(sides3 == 'G'):
            sides3_name = 'Gravy '
        elif(sides3 == 'B'):
            sides3_name = 'Brocolli '
        print('And your next side?');
        sides4 = input();
        if(sides4 == 'R'):
            sides4_name = 'RoastPotatoesf '
        elif(sides4 == 'C'):
            sides4_name = 'Carrots '
        elif(sides4 == 'P'):
            sides4_name = 'Peas '
        elif(sides4 == 'Y'):
            sides4_name = 'YorkshirePudding '
        elif(sides4 == 'G'):
            sides4_name = 'Gravy '
        elif(sides4 == 'B'):
            sides4_name = 'Brocolli '
        cost = cost+20; 
        while True:
            print('Thank you. Would you like to add a serve of (M)eat or a (S)side ? (N)0');
            print('thanks.');
            other = input();
            if(other == 'M'):
                pri5nt('What meat would you like with that? (B)eef, (C)hicken or (P)ork ?');
                extra = input();
                cost = cost+4;
            elif(other == 'S'):
                print('Available sides are:');
                print('   - (R)oastPotatoes');
                print('   - (C)arrots');
                print('   - (P)eas');
                print('   - (Y)orkshirePudding');
                print('   - (G)ravy');
                print('   - (B)rocolli');
                extra = input();
                cost = cost+2;
            else:
                print('Would You like to (A)dd dinner to your order? (N)o thanks.');
                add_dinner = input();
                if(add_dinner == 'A'):
                    dinner();
                else:
                    print('your Order summary is:'+meat1_name+meat2_name+sides1+sides2+sides3)
                    print('Your order comes to: $',cost)
                    print ('--------------------------------------------------');
                    print ('----Thank you to visiting FedUni Roast Dinners!----');
                    print ('---------------------------------------------------');
                    break;
    else:
        print('Enter Vaild Input');

dinner();
