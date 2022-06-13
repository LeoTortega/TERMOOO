import random
import unidecode

# Biblioteca de palavras
lista_palavras = ['sagaz', 'âmago', 'negro', 'êxito', 'mexer', 'termo', 'senso', 'nobre', 'algoz', 'afeto', 'plena',
                  'ética', 'mútua', 'tênue', 'sutil', 'vigor', 'aquém', 'porém', 'audaz', 'fazer', 'sanar', 'seção',
                  'inato', 'assim', 'cerne', 'ideia', 'fosse', 'desde', 'poder', 'moral', 'torpe', 'honra', 'muito',
                  'justo', 'fútil', 'gozar', 'anexo', 'razão', 'quiçá', 'etnia', 'sobre', 'ícone', 'tange', 'égide',
                  'sonho', 'lapso', 'mútuo', 'expor', 'haver', 'hábil', 'amigo', 'casal', 'tempo', 'seara', 'pesar',
                  'posse', 'ávido', 'então', 'porra', 'boçal', 'dengo', 'genro', 'coser', 'ardil', 'corja', 'causa',
                  'prole', 'pária', 'detém', 'dizer', 'tenaz', 'dever', 'digno', 'crivo', 'saber', 'óbice', 'ápice',
                  'ânsia', 'ânimo', 'ceder', 'graça', 'brado', 'orgia', 'gleba', 'comum', 'assaz', 'atroz', 'culto',
                  'sendo', 'temor', 'mundo', 'pauta', 'censo', 'fugaz', 'denso', 'valha', 'cozer', 'ainda', 'neném',
                  'vício', 'forte', 'estar', 'revés', 'vulgo', 'pudor', 'regra', 'dogma', 'louco', 'criar', 'banal',
                  'impor', 'pífio', 'tenro', 'desse', 'apraz', 'round', 'jeito', 'saúde', 'ordem', 'atrás', 'pedir',
                  'reaça', 'mercê', 'clava', 'usura', 'viril', 'juízo', 'sábio', 'prosa', 'servo', 'manso', 'ontem',
                  'feliz', 'presa', 'coisa', 'homem', 'falar', 'cunho', 'forma', 'fluir', 'devir', 'afago', 'ébrio',
                  'meiga', 'platô', 'xibiu', 'sério', 'vendo', 'guisa', 'mesmo', 'limbo', 'pleno', 'visar', 'temer',
                  'mágoa', 'cisma', 'herói', 'bruma', 'acaso', 'puder', 'lugar', 'êxodo', 'valor', 'óbvio', 'gerar',
                  'afins', 'obter', 'ímpio', 'matiz', 'crise', 'certo', 'praxe', 'senil', 'havia', 'posso', 'vênia',
                  'fluxo', 'enfim', 'ritmo', 'tédio', 'álibi', 'todos', 'tomar', 'garbo', 'união', 'abrir', 'reter',
                  'pulha', 'parvo', 'valia', 'visão', 'grato', 'vital', 'favor', 'bravo', 'fácil', 'vivaz', 'laico',
                  'falso', 'parco', 'prumo', 'gênio', 'ameno', 'olhar', 'possa', 'reles', 'óbito', 'burro', 'levar',
                  'prime', 'tesão', 'casta', 'tecer', 'selar', 'anelo', 'legal', 'fator', 'ranço', 'citar', 'rogar',
                  'farsa', 'façam', 'noção', 'adiar', 'morte', 'achar', 'coeso', 'cisão', 'cabal', 'épico', 'sábia',
                  'nicho', 'falta', 'fardo', 'imune', 'sinto', 'força', 'ativo', 'ouvir', 'gente', 'viver', 'exato',
                  'haste', 'amplo', 'brega', 'lavra', 'noite', 'sulco', 'dúbio', 'passo', 'sonso', 'gesto', 'labor',
                  'cesta', 'revel', 'tendo', 'sesta', 'leigo', 'único', 'deter', 'vemos', 'árduo', 'atuar', 'feixe',
                  'calma', 'rever', 'vadia', 'ótica', 'humor', 'ciúme', 'tende', 'igual', 'pobre', 'hiato', 'toada',
                  'sonsa', 'débil', 'ponto', 'ideal', 'velho', 'vácuo', 'outro', 'claro', 'ambos', 'linda', 'terno',
                  'remir', 'carma', 'fusão', 'varão', 'cauda', 'probo', 'ajuda', 'leito', 'senão', 'advém', 'doido',
                  'marco', 'fonte', 'horda', 'jovem', 'inata', 'capaz', 'xeque', 'relva', 'tenra', 'algum', 'caçar',
                  'ficar', 'velar', 'apoio', 'anuir', 'série', 'terra', 'farão', 'rigor', 'vimos', 'dorso', 'verso',
                  'líder', 'vazio', 'tanto', 'botar', 'entre', 'coçar', 'frase', 'cruel', 'prece', 'massa', 'vírus',
                  'moção', 'pouco', 'morar', 'ambas', 'peste', 'coesa', 'signo', 'sente', 'casto', 'fauna', 'covil',
                  'preso', 'credo', 'faina', 'minha', 'feito', 'raiva', 'furor', 'lazer', 'dócil', 'ímpar', 'ciclo',
                  'torço', 'vetor', 'flora', 'maior', 'chata', 'árido', 'corno', 'papel', 'brisa', 'aceso', 'beata',
                  'trama', 'vulto', 'houve', 'pegar', 'breve', 'liame', 'manha', 'birra', 'adeus', 'vasto', 'setor',
                  'salvo', 'senda', 'blasé', 'seita', 'banzo', 'ardor', 'morro', 'nossa', 'pecha', 'átomo', 'livro',
                  'visse', 'prado', 'reger', 'antro', 'peixe', 'avaro', 'segue', 'comer', 'meses', 'prono', 'plano',
                  'ocaso', 'rezar', 'saiba', 'chuva', 'sorte', 'anciã', 'áureo', 'saída', 'ótimo', 'aliás', 'pajem',
                  'nunca', 'temer', 'acima', 'junto', 'chulo', 'mudar', 'fitar', 'opção', 'serão', 'jazia', 'carro',
                  'sinal', 'fruir', 'parar', 'treta', 'séria', 'puxar', 'fugir', 'bando', 'nação', 'motim', 'gerir',
                  'prazo', 'andar', 'grupo', 'tosco', 'alude', 'leite', 'norma', 'época', 'sinhá', 'brava', 'rapaz',
                  'lenda', 'tenso', 'parte', 'exame', 'avião', 'arcar', 'ídolo', 'campo', 'tirar', 'venal', 'psico',
                  'soldo', 'reino', 'malta', 'praga', 'quota', 'virão', 'vilão', 'sumir', 'anais', 'aonde', 'exijo',
                  'logro', 'corpo', 'pompa', 'traga', 'preto', 'agora', 'voraz', 'fixar', 'antes', 'quase', 'cheio',
                  'risco', 'certa', 'praia', 'turva', 'nódoa', 'solto', 'cópia', 'filho', 'oásis', 'índio', 'turba',
                  'alado', 'apego', 'texto', 'messe', 'caixa', 'estão', 'grave', 'doído', 'parva', 'prova', 'acesa',
                  'perda', 'verve', 'nível', 'apelo', 'ligar', 'pardo', 'átrio', 'tocar', 'trupe', 'fenda', 'lindo',
                  'retém', 'viria', 'dessa', 'sabia', 'alçar', 'livre', 'coito', 'conta', 'verbo', 'opaco', 'navio',
                  'áurea', 'ficha', 'fraco', 'afora', 'ético', 'astro', 'faixa', 'elite', 'supra', 'parca', 'glosa',
                  'verba', 'autor', 'cioso', 'jirau', 'lidar', 'mente', 'tinha', 'firme', 'oxalá', 'grata', 'festa',
                  'fatos', 'magia', 'bater', 'calda', 'fatal', 'reses', 'cousa', 'privê', 'junco', 'pique', 'irmão',
                  'deixa', 'molho', 'pagão', 'salve', 'douto', 'macio', 'abriu', 'torso', 'turvo', 'supor', 'light',
                  'atual', 'manhã', 'bicho', 'ígneo', 'posto', 'asilo', 'órfão', 'rouca', 'extra', 'caber', 'judeu',
                  'curso', 'sarça', 'sexta', 'locus', 'besta', 'vezes', 'ruína', 'desta', 'pisar', 'zelar', 'rádio',
                  'vídeo', 'abuso', 'paira', 'porta', 'longe', 'combo', 'ereto', 'finda', 'bioma', 'cânon', 'culpa',
                  'vinha', 'agudo', 'vosso', 'feudo', 'menos', 'baixo', 'facto', 'tetra', 'urgia', 'advir', 'cútis',
                  'bônus', 'surja', 'drops', 'meigo', 'estio', 'traço', 'super', 'sítio', 'autos', 'tento', 'gosto',
                  'rumor', 'suave', 'facho', 'cocho', 'calão', 'pilar', 'museu', 'amena', 'clean', 'lasso', 'nosso',
                  'turma', 'geral', 'acolá', 'chama', 'ações', 'optar', 'pífia', 'medir', 'boato', 'louça', 'mosto',
                  'pódio', 'penta', 'lápis', 'local', 'rubro', 'hobby', 'crime', 'letal', 'pacto', 'ponha', 'folga',
                  'cover', 'cacho', 'refém', 'drama', 'brabo', 'aroma', 'hoste', 'vetar', 'vigia', 'poema', 'fazia',
                  'pasmo', 'feroz', 'açude', 'móvel', 'mesma', 'finjo', 'rival', 'troça', 'axila', 'monte', 'peito',
                  'golpe', 'metiê', 'ecoar', 'aluno', 'ávida', 'páreo', 'coral', 'riste', 'fórum', 'teste', 'lesse',
                  'lição', 'plebe', 'daqui', 'súcia', 'forem', 'júlia', 'monge', 'clima', 'chato', 'carta', 'poeta',
                  'ébano', 'escol', 'cetro', 'macro', 'swing', 'viram', 'sarau', 'falha', 'passa', 'piada', 'venha',
                  'ateia', 'briga', 'tacha', 'conto', 'verde', 'farta', 'calmo', 'cargo', 'légua', 'átimo', 'fruto',
                  'perco', 'berro', 'busca', 'roupa', 'plaga', 'tarde', 'idoso', 'plumo', 'broxa', 'aviso', 'virar',
                  'chefe', 'vento', 'tribo', 'corso', 'artur', 'grama', 'arado', 'surto', 'assar', 'civil', 'estro',
                  'seixo', 'bruta', 'recém', 'catre', 'traje', 'ornar', 'saldo', 'nuvem', 'deste', 'beijo', 'ímpia',
                  'fosso', 'troca', 'pedra', 'deram', 'trato', 'vedar', 'depor', 'arfar', 'tição', 'porte', 'gíria',
                  'irado', 'úteis', 'grota', 'canso', 'âmbar', 'casar', 'mangá', 'silvo', 'pasma', 'cifra', 'manga',
                  'única', 'bença', 'gabar', 'bazar', 'amado', 'sósia', 'magna', 'vazão', 'tutor', 'régio', 'rural',
                  'laudo', 'tiver', 'pavor', 'bruto', 'segar', 'perto', 'itens', 'bucho', 'renda', 'troco', 'mídia',
                  'tchau', 'nesse', 'jejum', 'amiga', 'vagar', 'minar', 'molde', 'odiar', 'inter', 'lesto', 'viado',
                  'clero', 'vadio', 'feita', 'órgão', 'fossa', 'meche', 'sótão', 'areia', 'aviar', 'pomar', 'negar',
                  'cenho', 'largo', 'cinto', 'paiol', 'ileso', 'lesão', 'canto', 'rocha', 'horto', 'visto', 'pugna',
                  'ruído', 'pinho', 'bolsa', 'proto', 'podar', 'invés', 'ufano', 'urdir', 'marca', 'guria', 'densa',
                  'vista', 'cível', 'morfo', 'dúbia', 'jogar', 'frota', 'vasta', 'mocho', 'close', 'penso', 'xucro',
                  'bulir', 'mamãe', 'piche', 'culta', 'úmido', 'bunda', 'peita', 'chula', 'cheia', 'esgar', 'úbere',
                  'linha', 'amada', 'canil', 'resto', 'stand', 'varoa', 'apear', 'misto', 'demão', 'fazes', 'natal',
                  'manto', 'monta', 'narco', 'fundo', 'findo', 'campa', 'barão', 'gemer', 'ágape', 'nessa', 'tenha',
                  'chaga', 'jazer', 'símio', 'retro', 'álbum', 'mover', 'cerca', 'preço', 'venho', 'ardis', 'folia',
                  'cosmo', 'pólis', 'lábia', 'santo', 'punha', 'velha', 'volta', 'sabor', 'álamo', 'matar', 'seiva',
                  'porca', 'ferpa', 'letra', 'banto', 'verão', 'sigla', 'calça', 'rente', 'ceita', 'louro', 'firma',
                  'barro', 'salva', 'nesta', 'etapa', 'arroz', 'trago', 'axial', 'áudio', 'redor', 'tumba', 'troço',
                  'torna', 'limpo', 'míope', 'coevo', 'bolso', 'final', 'solta', 'enjoo', 'lousa', 'ousar', 'lutar',
                  'sinta', 'baixa', 'coroa', 'queda', 'fugiu', 'logos', 'zumbi', 'corar', 'mimar', 'farol', 'obtém',
                  'veloz', 'neste', 'cacto', 'nácar', 'burra', 'reler', 'folha', 'fátuo', 'longo', 'penca', 'dança',
                  'vário', 'vazia', 'forro', 'quite', 'macho', 'mania', 'farto', 'justa', 'bedel', 'sugar', 'puído',
                  'repor', 'staff', 'ultra', 'lucro', 'salmo', 'refil', 'subir', 'gueto', 'chave', 'calor', 'viger',
                  'passe', 'custo', 'sexto', 'urgir', 'sadio', 'mimos', 'logia', 'harém', 'hífen', 'valer', 'todas',
                  'versa', 'calvo', 'usual', 'lento', 'sócio', 'mouro', 'cardo', 'rédea', 'árdua', 'anzol']


def introducao():
    logo = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%***************?************??**********?%%%?*****%%%%%%?****?%%%%?*;:::;+*%%%%%%%%%%%%%%%
%%%%%%%%%%:.............,*,...........+*.........,:*%%?,...,?%%%%%+....;%%%+:.......,;?%%%%?%%%%%%%%
%%%%%%%%%?:.............,+,...........+*...........,+%*,....+%%%%?:....;%?;...........,*%%%%%%%%%%%%
%%%%%%%%%%:.....,.......,*,...........+*.,..........,?*,....:%%%%*,....;%+......,......,?%%%%%%%%%%%
%%%%%%%%%%?++++,...,+*++?*,...,+*++++*?+....:++;,....+?,....,*%%%;.....;?,....:*??+,....;%%?%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,?%%%%%%%+....;%%%;....;*,.....;%%?,.....;+....,?%%%%+....,?%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,?%%%%%%%+....:%%%+....;*,...,.,?%+......;;....;%%%%%?,....*%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,;;;;+?%%+....;%%%;....;*,......+%:......::....+%%%%%?:....+%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,..,......+%%+....:++:,....+?,...,..:*,..,.,.::...,*%%%%%%;....;%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,........,+%%+..........,.,?*,...:,.,:..,,...::...,?%%%%%%;....+%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,,,,,,*%%+...........,+%*,...;:.....+,...::...,*%%%%%?;....+%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,*????%%%+,.........,+%%*,...;+....:*,...;;....+%%%%%?:....*%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,?%%%%%%%+....:*;....+%%*,...;?:...+?,...;;....:?%%%%*,.,.,?%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,*??????%+,...;%?,...,?%*,...;%+..,??,...;*,...,;?%%*:....;?%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...,,,,,,,,**....;%%;....+%*,...;%?:,+%?,...;%;.....,::,....,*%%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%%%*,...........++....;?%*,...:?*,.,.;%%%%%%?,...;%?:...........,+%%%%%%%%%%%%
%%%%%%%%%%%%%%?,...,*%%?%*,...........+*....:%%?:....*?,...;%%%%%%?,...;%%?:,........,+%%%%%%%%%%%%%
%%%%%%%%%%%%%%?+;;;+?%%%%?+;;;;;;;;;;;*?;;;;*%%%*;;;;*?+;;;*%%%%%%?+;;;*%%%%*;:,,,,;+?%%%%?%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%?%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%?????%%%%%?%%%%%%%%%%%
"""
    print(logo)


# Selecionar uma palavra entre as que estão na lista
def seletor():
    palavra = lista_palavras[random.randint(0, 999)]
    return palavra


# Compara uma palavra digitada pelo usuario com a selecionada pelo computador
def verificador(palavra_computador, palavra_real):
    req_palavra = False
    contador = 1
    while not req_palavra:
        if contador < 7:
            palavra_usuario = unidecode.unidecode(input("\nDigite uma palavra de 5 letras: ")).lower()
            if palavra_usuario.isalpha() and len(palavra_usuario) == 5:
                for i in range(5):
                    if palavra_usuario[i] == palavra_computador[i]:
                        print("V", end="")
                    elif palavra_usuario[i] in palavra_computador:
                        print("Q", end="")
                    else:
                        print("F", end="")

                usuarioS = ", ".join(palavra_usuario)
                computadorS = ", ".join(palavra_computador)
                contador += 1
                if usuarioS == computadorS:
                    print("\nPalavra Correta")
                    req_palavra = True
                    return req_palavra
                else:
                    print(f"\nPalavra Incorreta, {7-contador} tentativas restantes")
            else:
                print("\nPalavra invalida")
        else:
            print("Você atingiu o limite de tentativas")
            print(f"A palavra era: {palavra_real}")
            break


introducao()
palavra = seletor()
palavra_computador = unidecode.unidecode(palavra)

verificador(palavra_computador, palavra)
