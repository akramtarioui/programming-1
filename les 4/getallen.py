cijferICOR = 6
cijferPROG = 6
cijferCSN = 6

gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3

beloningICOR = cijferICOR * 30
beloningPROG = cijferPROG * 30
beloningCSN = cijferCSN * 30

beloning = beloningCSN + beloningICOR + beloningPROG

overzicht = 'mijn cijfers zijn gemiddeld een: ' + str(gemiddelde) + ', ik heb een beloning van: ' + str(beloning) + ' euro'

print (overzicht)
