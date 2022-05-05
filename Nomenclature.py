def nomenclature(c,nb_alcan,place_alcan,grp_car,place_grp):
  grp_car=grp_car.upper()
  if place_alcan==0:
    place_alcan=""
  if place_grp==0:
    place_grp=""
  radical=""
  prefixe=""
  suffixe=""
  if c==1:
    radical="méthan"
  if c==2:
    radical="éthan"
  if c==3:
    radical="propan"
  if c==4:
    radical="butan"
  if c==5:
    radical="pentan"
  if c==6:
    radical="hexan"
  if c==7:
    radical="heptan"
  if c==8:
    radical="octan"
  if nb_alcan==1:
    prefixe="méthyl"
  if nb_alcan==2:
    prefixe="éthyl" 
  if nb_alcan==3:
    prefixe="propyl"
  if grp_car == "OH":
    print("Grp hydroxyle et fam alcool")
    suffixe="ol"
  if grp_car == "OOH":
    print("Grp carboxyle et fam acide carboxylique")
    suffixe="oïque"
  if grp_car == "CO":
    print("Grp carbonyle et fam cétone")
    suffixe="one"
  if grp_car == "CHO":
    print("Grp carbonyle et fam aldéhyde")
    suffixe="al"
  print(prefixe+"-"+str(place_alcan)+"-"+radical+"-"+str(place_grp)+"-"+suffixe)