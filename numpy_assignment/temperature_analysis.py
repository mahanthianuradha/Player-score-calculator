import numpy as np
temps_celsius=np.array([22,25,28,24,26])
print(f"Celsius:{temps_celsius}")
temps_fh=temps_celsius*1.8+32
print(f"Fahrenheit:{temps_fh}")
avg_fh=sum(temps_fh)/len(temps_fh)
print(f"Average Fahrenheit:{avg_fh:.1f}")