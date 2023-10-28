import time

print('\033[4;49;96m-'*50)
print('SEJA BEM VINDO! TEST, TRANSFORMAR DINHEIRO R$ EM DOLAR ∆ O PREÇO DO DOLAR ESTA EM MEDIA 5.20 ∆')
print('-'*50)
print('''\033[0;49;96m######## #### #### ########  ######## ##    ## 
     ##   ##   ##  ##     ##      ##   ##  ##  
    ##    ##   ##  ##     ##     ##     ####   
   ##     ##   ##  ########     ##       ##    
  ##      ##   ##  ##          ##        ##    
 ##       ##   ##  ##         ##         ##    
######## #### #### ##        ########    ##   \n''')

xsdf = input('clique enter para avançar...')
print('AGUARDE!...')
time.sleep(5)


real=float(input('Quantos reais voce tem na carteira?R$:'))

dolar=real/5.20

print('''-----------------------------
\033[0;49;91m[!]\033[0;49;00000mCom R${}
-----------------------------
\033[0;49;91m[!]\033[0;49;9999mPODE COMPRAR
-----------------------------
\033[0;49;91m[!]\033[0;49;83746mUS${}\n
-----------------------------'''.format(real, dolar))

print('''DESENVOLVIDO POR:
[!]ZIIP
[!]INSTAGRAM: @ziip_019]
[!]GIT HUB: https://github.com/ziippk''')
