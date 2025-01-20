with open('C:/users/mzbor/python/vety/vstup.txt', 'r') as t:
    ps = 0  # počet slov
    pz = 0  # počet znakov
    pv = 0  # počet viet

    for riadok in t:
        riadok = riadok.strip()
        ps += len(riadok.split())
        pz += len(riadok)
        pv += sum(1 for znak in riadok if znak in '.!?')

print('Počet slov v súbore je:', ps)
print('Počet znakov v súbore je:', pz)
print('Počet viet v súbore je:', pv)