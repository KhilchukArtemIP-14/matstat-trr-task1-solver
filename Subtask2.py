import math
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t as stat_t

def subtask2(data,known_dispersion,gamma):
    #математичного сподівання при відомій дисперсії
    print("Calculating for the mathematical expectation given a known variance")
    mean=sum(data)/len(data)
    print(f"\tMean for sample: {mean}")
    f_t = gamma/2+norm.cdf(0)
    t=round(norm.ppf(f_t),4)
    print(f"\tF_t = {gamma/2}\n\tSo t = {t}")
    delta_e=t*math.sqrt(known_dispersion)/math.sqrt(len(data))

    lower_interval_bound=mean-delta_e
    upper_interval_bound=mean+delta_e

    print(f"\nSo, given confidence level of {gamma} confidence interval for mathematical expectation is ({lower_interval_bound};{upper_interval_bound})")

    #для невідомої
    print("\nCalculating for the mathematical expectation given an unknown variance")

    dispersion_vib=sum([(a-mean)**2 for a in data])/len(data)
    s_kv=len(data)/(len(data)-1)*dispersion_vib
    deviat_vipr=math.sqrt(s_kv)
    print(f"\tDispersion for sample:{dispersion_vib}\n\tS^2: {s_kv}")

    critical_tvalue = stat_t.ppf((1 + gamma) / 2, len(data)-1)
    print(f"Critical t-value for a given variance:{critical_tvalue}")

    delta_e = critical_tvalue * deviat_vipr / math.sqrt(len(data))

    lower_interval_bound = mean - delta_e
    upper_interval_bound = mean + delta_e

    print(f"\nSo, given confidence level of {gamma} confidence interval for mathematical expectation is ({lower_interval_bound};{upper_interval_bound})")

    #для дисперсії
    print("\nCalculating for the variance:")
    f2=(1-gamma)/2
    f1=(1+gamma)/2
    print(f"\n\tF1 value: {f1}\n\tF2 value: {f2}")

    chi_1 = chi2.ppf(f1, len(data) - 1)
    chi_2 = chi2.ppf(f2, len(data) - 1)

    lower_interval_bound = (len(data)-1)*s_kv/chi_1
    upper_interval_bound = (len(data)-1)*s_kv/chi_2

    print(f"\n\tChi-1 value: {chi_1}\n\tChi-2 value: {chi_2}")
    print(f"\nSo, given confidence level of {gamma} confidence interval for variance is ({lower_interval_bound};{upper_interval_bound})")






