import pandas as pd
import matplotlib.pyplot as plt
from aide_design.shared.units import unit_registry as u


def time_to_day_fraction(time):
  '''
  Parameters
  ----------
  time
    string in the form of hh:mm
  '''
  hour = int(time.split(":")[0])
  minute = int(time.split(":")[1])
  return hour/24 + minute/1440


def remove_notes(data):
  '''
  Parameters
  ----------
  data
    pandas.DataFrame object
  '''
  has_text = data.iloc[:,0].astype(str).str.contains('[a-z]', '[A-Z]')
  text_rows = list(has_text.index[has_text])
  return data.drop(text_rows)


def plot_columns(directory, extension, start_datetime, end_datetime, x_column, y_column):
  '''
  Parameters
  ----------
  start_datetime and end_datetime
      must be in the format 'MM-DD-YYYY hh:mm' (24 hr time)
  interval
      in seconds, minutes, or hours
  x_column and y_column
      for now, only integer indices
  directory
      must end in '/'
  extension
      preceeded by '.', such as '.csv'
  '''
  # Locate data file(s)
  start_date = start_datetime.split(' ')[0]
  paths = [directory + "datalog " + start_date + extension]
  data = [remove_notes(pd.read_csv(paths[0], delimiter='\t'))]

  end_date = end_datetime.split(' ')[0]
  if start_date != end_date:
    paths.append(directory + "datalog " + end_date + extension)
    data.append(remove_notes(pd.read_csv(paths[1], delimiter='\t')))

  # Calculate start index
  start_time = time_to_day_fraction(start_datetime.split(' ')[1])
  time_column = pd.to_numeric(data[0].iloc[:, 0])
  interval = time_column[1]-time_column[0]

  start_idx = int(round((start_time - time_column[0])/interval + .5)) #round up

  # Calculate end index and get columns of interest
  end_time = time_to_day_fraction(end_datetime.split(' ')[1])
  if len(paths) == 1:
    end_idx = int(round((end_time - time_column[0])/interval + .5)) #round up
    x = pd.to_numeric(data[0].iloc[start_idx:end_idx, x_column])
    y = pd.to_numeric(data[0].iloc[start_idx:end_idx, y_column])

  else:
    time_column = pd.to_numeric(data[1].iloc[:, 0])
    end_idx = int(round((end_time - time_column[0])/interval + .5)) #round up
    x = list(pd.to_numeric(data[0].iloc[start_idx:, x_column]))
    x += list(pd.to_numeric(data[1].iloc[:end_idx, x_column]) + 1)
    y = list(pd.to_numeric(data[0].iloc[start_idx:, y_column]))
    y += list(pd.to_numeric(data[1].iloc[:end_idx, y_column]))

  plt.figure(figsize=(12,4))
  plt.plot(x, y, 'o', markersize = 2)
  plt.xlabel(list(data[0])[x_column])
  plt.ylabel(list(data[0])[y_column])
  plt.title(list(data[0])[y_column] + " vs " + list(data[0])[x_column])
  plt.minorticks_on()
  plt.grid(which = 'major')
  plt.grid(which = 'minor')
  plt.show()


#example usage
plot_columns('/Users/HannahSi/Desktop/AguaClara Summer/Data/','.xls', '7-16-2018 11:15', '7-17-2018 9:35', 0, 4)
