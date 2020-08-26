def read_hidden_variables():
  variables = {}
  with open(".env", 'r') as f:
    line = f.readline()
    key, value = line.split('=')
    variables[key] = value
  return variables

hidden_variables = read_hidden_variables()