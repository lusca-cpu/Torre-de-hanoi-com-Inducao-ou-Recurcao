def HanoiSolver(disco, origem, aux, destino):
    ## BASE INDUTIVA ########################
    if disco == 1: # caso base
        ## PASSO INDUTIVO ######################
        print(f'Mova o disco {disco} da torre {origem} para a torre {destino}.')
        return 
    else:
        ## HIPOTESE INDUTIVO ######################
        HanoiSolver(disco-1, origem, destino, aux)

    ## PASSO INDUTIVO ######################
    print(f'Mova o disco {disco} da torre {origem} para a torre {destino}.')
    ## HIPOTESE INDUTIVA ######################
    HanoiSolver(disco-1, aux, origem, destino)
    return

if __name__ == '__main__':
    disco = int(input("Digite a quantidade de que deseja: "))

    HanoiSolver(disco, 'A', 'B', 'C')  