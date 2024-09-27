import numpy as np
import math
def split_file(df, path):

  max_number_line_file = 24000
  number_chunk = math.ceil(len(df)/max_number_line_file)
  df = np.array_split(df, number_chunk)
  # df[0] = first array, last array df[n-1].
  i = number_chunk - 1
  
  while i > -1:
      df[i].to_csv(
          path+'clean_csv_'+'part_%s.csv' % i,
          header=True,
          index=False,
          encoding='utf-8',
          )
      i = i - 1
