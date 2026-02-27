import time

import numpy as np
numpy_arr=np.arange(1,50001)
python_list=list(range(1,50001))

start = time.time()
numpy_sum = np.sum(numpy_arr)
numpy_time= time.time()-start

start=time.time()
python_sum = sum(python_list)
python_time=time.time()-start

numpy_speed=python_time/numpy_time


print(f"Numpy sum:{numpy_sum}")
print(f"Python sum:{python_sum}")
print(f"Numpy time:{numpy_time:.4f} seconds")
print(f"Python time:{python_time:.4f} seconds")
print(f"Numpy is {numpy_speed}x faster ")




