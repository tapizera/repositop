import random

start_intro2 = ['Nesse sentido', 'Nesse contexto', 'Dessa forma', 'sob esse viés', 'é valido destacar']
start_intro3 = ['Além disso', 'No entanto', 'Da mesma forma', 'Outrossim']

# desenvolvimento
start_des1 = []
start_des2 = []

# conclusão
start_conclusão = ['Em suma', 'Destarte', 'Diante do exposto']

sinonimos = {
# sinônimos básicos
'e' : ['ademais', 'além disso'],
'mas' : ['contudo', 'entretanto', 'todavia'],
'então' : ['portanto', 'logo', 'por conseguinte'],

# sinônimos chiques
'considerado' : ['eminente' , 'ilustre (nobre)', 'célebre (famoso)', 'notável','destacado', 'relevante'],
'muito foda' : ['sublime', 'trascendente', 'esplêndido', 'soberbo', 'exuberante'],
'precisa' : ['é mister', 'é necessário', 'é fundamental'],
'acabar' : ['mitigar', 'erradicar', 'atenuar', 'impedir', 'coibir'],
'que forma' : ['contituem', 'integramw', 'consistem', 'compõem', 'produzem', 'estruturam', 'preparam', 'introduzem'],
'problema' : ['obstáculo', 'empecilho', 'revé', 'entrave', 'barreira', 'impasse', 'questões', 'entorvos'],
'cenário' : ['panorama', 'perspectiva', 'realidade', 'óptica'],
'ruim' : ['lamentável', 'miserável', 'angustiante', 'inaporpriado', 'afligente', 'penoso'],
'para que' : ['a fim de', 'com propósito de', 'com finalidade de', 'com intensão de', 'com o objetivo de'],
'prejudicial' : ['infesto', 'nocente', 'deleério', 'nóxio', 'maléfico'],
'permitido' : ['outorgado', 'concedido', 'aprovado', 'dispõe'],
'utiliza' : ['usufrui', 'desfruta', 'desfrui'],
'determina' : ['estabelece', 'dispõe', 'define']
}

palavra = input('sinonimar: ')
def sinonimar(palavra):
    if palavra in sinonimos:
        print(random.choice(sinonimos[palavra]))
    else:
        print(f'não conheço sinônimos para {palavra}')

sinonimar(palavra)

dnv = input(f'de novo?(s/n) ')
while dnv == 's':
        palavra = input('sinonimar: ')
        sinonimar(palavra)
else: 
        print('é isso')
