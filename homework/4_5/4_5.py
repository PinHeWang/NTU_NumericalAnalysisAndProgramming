article = '''They make a pool of silver, swim as stones through the pine 
branches, push back needles like a dog's fur shaking off the 
bathwater and carry what is left of the sky as bones hitched 
together into a stream. It never tires. The stars so still are 
never really still. And what pieces you can hold-thread, whiskey, 
chigger bites, sin-you lose like the loosest water round and 
round your fingers, like her hair you cannot touch now, like 
the last bits of light you mapped on the bed until worn 
blind-through, sleepless, breath-rattled, loping through 
the dark alone.'''

a = [None]*(len(article)-1);
for i in range(len(article)-1):
    if article[i+1]==',' or article[i+1]==' ' or article[i+1]=='.' or article[i+1]=='\'' or article[i+1]=='-':
        a[i] = article[i].upper();
    else:
        a[i] = article[i];
a += ['.']      
a = ''.join(a);
article = a;
        
print article

