def check_pass(password):
    return ((len([char for char in password if char.islower()]) > 0) and (len([char for char in password if char.isupper()]) > 0) and (len([char for char in password if char.isdigit()]) > 0))

print 'pizza: ' + str(check_pass('pizza'))
print 'Pizza: ' + str(check_pass('pizza'))
print 'P1zza: ' + str(check_pass('pizza'))

#def strength(password):
