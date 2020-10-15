import sys, hcl

with open(sys.argv[1], 'r') as fp:
    try:
      obj = hcl.load(fp)
    except ValueError as e:
      print(str(e) + '\n')
      print('Note: pyhcl 0.4.4 and below do not seem to support validation sections in variables.')
      exit(1)
    except Exception as e:
      print(str(e) + '\n')
      print('Error Loading File: ' + sys.argv[1] + ', May need to update pyhcl.')
      exit(1)

    if str(obj) == "{}":
        print('Empty Variables File: ' + sys.argv[1])
        exit(2)

    # Default Column Widths
    col1 = 8  # variable
    col2 = 8  # default
    col3 = 8  # required
    col4 = 12 # description

    # Calculate Column Widths
    for key in obj['variable'].keys():
        default = len(str(obj['variable'][key].get('default', '')))
        description = len(str(obj['variable'][key].get('description', '')))
        if len(str(key)) > col1:
            col1 = len(str(key))
        if default > col2:
            col2 = min(default, 40)
        if description > col4:
            col4 = min(description, 100)

    # Default value for Variables with no Values
    defvalue = ""
    if len(sys.argv) > 2:
        defvalue = sys.argv[2]

    # Generate Table
    print("| {} | {} | {} | {} |".format('variable'.ljust(col1),'default'.ljust(col2),'required'.ljust(col3),'description'.ljust(col4)))
    print("|-{}-|-{}-|-{}-|-{}-|".format('-'*col1,'-'*col2,'-'*col3,'-'*col4))
    #print "| Variable | Default | Required | Description |"
    #print "|----------|---------|----------|-------------|"
    for key in obj['variable'].keys():
        default = obj['variable'][key].get('default', key + '%defvalue%')
        description = obj['variable'][key].get('description', '')
        if 'default' in obj['variable'][key]:
            required = 'No'
        else:
            required = 'Yes'

        # Indicate that a blank value is an empty String
        if str(default).strip(' ') == "":
            default = '""'
        elif default == key + '%defvalue%':
            default = defvalue

        print("| {} | {} | {} | {} |".format(str(key).strip(' ').ljust(col1), str(default).strip(' ').ljust(col2), str(required).strip(' ').ljust(col3), str(description).strip(' ').ljust(col4)))
