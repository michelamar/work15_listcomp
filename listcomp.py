def check_pass(password):
    return ((len([char for char in password if char.islower()]) > 0) and (len([char for char in password if char.isupper()]) > 0) and (len([char for char in password if char.isdigit()]) > 0))

print "CHECK"
print 'pizza: ' + str(check_pass('pizza'))
print 'Pizza: ' + str(check_pass('Pizza'))
print 'P1zza: ' + str(check_pass('P1zza'))

def strength(password):
    if not check_pass(password):
        return 0
    else:
        lower = len([char for char in password if char.islower()])
        upper = len([char for char in password if char.isupper()])
        num = len([char for char in password if char.isdigit()])
        other = len([char for char in password if char in ".?!&#,;:-_*"])
        strength = (float(upper+num+other)/len(password))*len(password)
        print strength
        if strength > 10:
            strength = 10
        return strength

print "STRENGTH"
print 'pizza: ' + str(strength('pizza'))
print 'P1zza: ' + str(strength('P1zza'))
print 'OHUwuefwj984728388383838+: ' + str(strength('OHUwuefwj984728388383838+'))

    
