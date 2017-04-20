import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({"x" : [v[0] for v in vectors_set],
                "y" : [v[1] for v in vecotrs_set]})

sns.lmplog("x","y",data=df, fit_reg = False, size =6)
plt.show()
