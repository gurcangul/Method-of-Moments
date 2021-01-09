import numpy as np
import matplotlib.pyplot as plt

est_p_200 = [];
est_n_200 = [];
for i in range(1000):
    nosuccess = np.random.binomial(40, 0.3, 200)
    est_p = 1 - np.std(nosuccess) ** 2 / np.mean(nosuccess)
    est_p_200.append(est_p)
    est_n = np.mean(nosuccess) ** 2 / (np.mean(nosuccess) - np.std(nosuccess) ** 2)
    est_n_200.append(est_n)

est_p_800 = [];
est_n_800 = [];
for i in range(1000):
    nosuccess = np.random.binomial(40, 0.3, 800)
    est_p = 1 - np.std(nosuccess) ** 2 / np.mean(nosuccess)
    est_p_800.append(est_p)
    est_n = np.mean(nosuccess) ** 2 / (np.mean(nosuccess) - np.std(nosuccess) ** 2)
    est_n_800.append(est_n)

est_p_3200 = []
est_n_3200 = [];
for i in range(1000):
    nosuccess = np.random.binomial(40, 0.3, 3200)
    est_p = 1 - np.std(nosuccess) ** 2 / np.mean(nosuccess)
    est_p_3200.append(est_p)
    est_n = np.mean(nosuccess) ** 2 / (np.mean(nosuccess) - np.std(nosuccess) ** 2)
    est_n_3200.append(est_n)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(est_p_200, **kwargs)
plt.hist(est_p_800, **kwargs)
plt.hist(est_p_3200, **kwargs)
plt.title('Histogram for estimated p')

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)
plt.hist(est_n_200, **kwargs)
plt.hist(est_n_800, **kwargs)
plt.hist(est_n_3200, **kwargs);
plt.title('Histogram for estimated n')


print(f'Mean for estimated p for sample size of 200 is {np.mean(est_p_200)}.')
print(f'Standard deviation for estimated p for sample size of 200 is {np.std(est_p_200)}.')
print(f'Mean for estimated p for sample size of 200 is {np.mean(est_p_800)}.')
print(f'Standard deviation for estimated p for sample size of 200 is {np.std(est_p_800)}.')
print(f'Mean for estimated p for sample size of 200 is {np.mean(est_p_3200)}.')
print(f'Standard deviation for estimated p for sample size of 200 is {np.std(est_p_200)}.')
