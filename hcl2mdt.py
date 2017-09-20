import sys,hcl

with open(sys.argv[1], 'r') as fp:
   obj = hcl.load(fp)


print "|{}|{}|{}|{}|".format(' variable'.ljust(20),' default'.ljust(15),'required'.ljust(8),' description'.ljust(40))
print "|{}|{}|{}|{}|".format('-'*20,'-'*15,'-'*8,'-'*40)
#print "| variable  |  default  |  required  |  description    |"
#print "|-----------|-----------|------------|-----------------|"
for key in obj['variable'].keys():
  var = key
  default = obj['variable'][key].get('default', '')
  description = obj['variable'][key].get('description', '')
  if 'default' in obj['variable'][key]:
    required = 'No'
  else:
    required = 'Yes'
  #print "|  %s   |   %s   |  %s  |   %s                | " % (str(var).ljust(15), str(default).ljust(10), str(required).ljust(10), str(description).ljust(30))
  print "|{}|{}|{}|{}|".format(str(var).ljust(20), str(default).ljust(15), str(required).ljust(8), str(description).ljust(40))
  
