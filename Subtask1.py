import math
import pandas as pd
from scipy.stats import norm
from scipy.stats import chi2

def subtask1(numbers):
    size=len(numbers)
    maximum=max(numbers)
    minimum=min(numbers)
    R=maximum-minimum
    h=round(R/math.sqrt(size),3)
    print(f"Minimum:{minimum}\nMaximum:{maximum}\nR(rozmah):{R}\nh(optimalny krok):{h}")

    curr=minimum
    intervalni={}
    print("\nIntervalni:")
    while(curr+h<maximum):
        upper=round(curr+h,3)
        count=len([value for value in numbers if curr <= value < upper])
        intervalni[(curr,upper)]=count
        print(f"\t[{curr};{upper}) - {count}")
        curr=upper
    upper = round(curr + h, 3)
    count = len([value for value in numbers if curr <= value <= upper])
    intervalni[(curr, upper)] = count
    print(f"\t[{curr};{upper}] - {count}")
    print("\nStatis rozpodil z variantami po centru:")

    centri={}
    for key in intervalni:
        curr,upper = key
        centr=round((curr+upper)/2,3)
        print(f"\t{centr} - {intervalni[key]}")
        centri[centr]=intervalni[key]

    print("\nNeobhidni parametri:")
    serednye_obrah="("
    for a in centri:
        serednye_obrah+=f"{a}*{centri[a]}+"

    serednye_obrah=serednye_obrah[:-1]+f")/{size}"
    serednye_znach=sum([a*centri[a] for a in centri])/size
    print("\n\tX z liniyeyu i zirochkoyu = *formula* =",serednye_obrah,f"={serednye_znach}")

    serednye_kvadrat_obrah="=("
    for a in centri:
        serednye_kvadrat_obrah+=f"{a}^2*{centri[a]}+"

    serednye_kvadrat_obrah=serednye_kvadrat_obrah[:-1]+f")/{size}"

    serednye_kvadrat_znach=sum([a*a*centri[a] for a in centri])/size
    print("\tX z liniyeyu i zirochkoyu kvadrat = *formula*",serednye_kvadrat_obrah,f"={serednye_kvadrat_znach}")

    sigma_zirochka=math.sqrt(serednye_kvadrat_znach-serednye_znach**2)
    print("\n\tSigma zirochka= *formula* =",sigma_zirochka)

    print("Obchislyuemo teoretichni chastoti:")
    teor_freq=pd.DataFrame()
    lower_bounds=[]
    upper_bounds=[]
    for key in intervalni:
        lower,upper = key
        lower_bounds.append(lower)
        upper_bounds.append(upper)
    teor_freq["x_i"]=lower_bounds
    teor_freq["x_(i+1)"]=upper_bounds

    z_i=[]
    z_i_plus_one=[]

    for index, row in teor_freq.iterrows():
        previous_row = teor_freq.iloc[index - 1] if index > 0 else None
        next_row = teor_freq.iloc[index + 1] if index < len(teor_freq) - 1 else None

        if(previous_row is None):
            z_i.append(-float('inf'))
        else:
            z_i.append((row["x_i"]-serednye_znach)/sigma_zirochka)

        if (next_row is None):
            z_i_plus_one.append(float('inf'))
        else:
            z_i_plus_one.append((row["x_(i+1)"] - serednye_znach) / sigma_zirochka)

    teor_freq["z_i"]=z_i
    teor_freq["z_(i+1)"]=z_i_plus_one
    teor_freq["f(z_i)"]=norm.cdf(teor_freq["z_i"])-norm.cdf(0)
    teor_freq["f(z_i)"]=teor_freq["f(z_i)"]
    teor_freq["f(z_(i+1))"]=norm.cdf(teor_freq["z_(i+1)"])-norm.cdf(0)
    teor_freq["f(z_(i+1))"]=teor_freq["f(z_(i+1))"]

    teor_freq["p_i"]=teor_freq["f(z_(i+1))"]-teor_freq["f(z_i)"]
    teor_freq["n_i"]=teor_freq["p_i"]*size

    for col in teor_freq.columns:
        teor_freq[col]=teor_freq[col].round(4)

    print(teor_freq)

    teor_freq.to_csv("teor_freq.csv")

    #obchislyuem chi_sp
    chi_square_calcs=pd.DataFrame()
    chi_square_calcs['n_i']=centri.values()
    chi_square_calcs['n_i_shtrih']=teor_freq["n_i"]
    chi_square_calcs['difference']=chi_square_calcs['n_i']-chi_square_calcs['n_i_shtrih']
    chi_square_calcs['square_difference']=chi_square_calcs['difference']**2
    chi_square_calcs['square_difference_div_n_i']=chi_square_calcs['square_difference']/chi_square_calcs['n_i']

    print()
    for col in chi_square_calcs.columns:
        chi_square_calcs[col]=chi_square_calcs[col].round(4)

    chi_square_calcs.to_csv("chi_square_calcs.csv")
    print(chi_square_calcs)

    #calculate x_sp
    x_sp=chi_square_calcs['square_difference_div_n_i'].sum()
    print(f"X_sp: {x_sp}")

    x_crit=chi2.ppf(1 - 0.05, len(centri)-3)
    print(f"X_crit: {x_crit}")
    if(x_crit>x_sp):
        print("There is no basis to reject zero hypothesis")
    else:
        print("There is basis to reject zero hypothesis")