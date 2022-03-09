def estimateCusts(weekend, rainy, game):
    customers = 0
    if weekend: customers += 350
    
    else: customers += 200

    if rainy: customers *=  .90
        
    if game: customers *= .85

    return int(round(customers, 0))


    
print (estimateCusts(True, True, False))
