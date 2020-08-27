def read_hidden_variables():
  variables = {}
  with open(".env", 'r') as f:
    line = f.readline()
    key, value = line.split('=')
    if value.isdecimal():
      if value.find('.') > 0:
        value = float(value)
      else:
        value = int(value)
    variables[key] = value
  return variables

hidden_variables = read_hidden_variables()