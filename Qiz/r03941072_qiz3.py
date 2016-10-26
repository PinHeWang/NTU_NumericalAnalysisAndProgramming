code = 'V jnf greevoyr va Ratyvfu. V pbhyq abg fgnaq gur fhowrpg. Vg frrzrq gb zr evqvphybhf gb jbeel nobhg jurgure lbh fcryyrq fbzrguvat jebat be abg, orpnhfr Ratyvfu fcryyvat vf whfg n uhzna pbairagvba - vg unf abguvat gb qb jvgu nalguvat erny, nalguvat sebz angher. Evpuneq C. Srlazna'

decoded_content = ''

### START YOUR CODE HERE ###
d = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z',\
'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m',' ':' ','.':'.',',':',','-':'-',\
'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z',\
'N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'};

for i in range(len(code)):
    decoded_content += d[code[i]];




#### END YOUR CODE HERE ####
                
print decoded_content