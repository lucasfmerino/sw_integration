<h1 align="center">
  <img src="src/images/sw_integration_01.png" alt="sw_integration_01">
</h1>

Esta é uma demonstração simples para integrar o Python com o SolidWorks e melhorar a eficiência nos projetos e modelagem 3D.
<br>


## O Python e o Solid Works:
O SolidWorks é um software CAD popular que é amplamente utilizado na indústria para projetar peças e montagens em 3D. A integração do Python com o SolidWorks pode permitir a automação de tarefas repetitivas, a execução de simulações e análises de dados e a criação de recursos personalizados.
<br>


## Sobre esta demonstração:
Neste exemplo, você aprenderá como criar as suas variáveis personalizadas utilizando o Python e realizar a integração com o SolidWorks. Essas variáveis formarão a identidade dos modelos, proporcionando maior eficiência ao criar ou modificar seus componentes 3D no SolidWorks.
<br>


## Dependências:
No Python, para essa integração, usaremos apenas os recursos e bibliotecas nativas da linguagem.
Como trata-se de uma integração, é necessário que o SolidWorks esteja devidamente instalado.
É indicado conhecimentos básicos em SolidWorks ou em softwares de modelagem 3D similares.
<br>
<br>


# MÃOS A OBRA 🛠
## PASSO 1 - Conhecendo as Variáveis
<div>
    <p>
        É muito importante identificar corretamente as variáveis do seu projeto, pois são elas as responsáveis pelas características e funcionalidades do seu produto.<br>
        Neste exemplo, utilizarei como o modelo deste projeto, uma ferramenta de puncionadeira para estampagem de furos redondos em chapas metálicas.
    </p>
    <p>
        Este modelo de ferramenta possuí três componentes, sendo eles: punção, extrator e matriz.
    </p>
    <p>
        Temos então nossa primeira variável, o diâmetro do furo redondo. Repare que todos os componentes da ferramenta dependem desta variável. É o diâmetro do furo que determina a dimensão do punção e os outros componentes devem ser modelados de forma que, suas dimensões estejam referenciadas com o punção ou diretamente interligadas à nossa primeira variável.
    </p>
    <p>
        Entender essa relação de dependências é essencial, para que a estrutura e a escolha dos recursos de modelagem possam garantir o resultado desejado.
    </p>
    <p>
        Como o objetivo desta demonstração é realizar uma interação simples com o SolidWorks utilizando Python e não um tutorial de projeto de ferramentas, vamos direto para as próximas variáveis.
    </p>
    <p>
        No punção, temos a próxima variável, o diâmetro da base. Essa dimensão deve variar conforme os parâmetros estabelecidos para a dimensão do furo.<br>
        Temos uma ocorrência similar na matriz, onde o diâmetro da sua base também deve variar conforme os parâmetros de projeto.<br>
        Ainda na matriz, será aplicada a folga de corte. Essa variável depende de outras variáveis para ser calculada. Toda essa resolução pode ser emplementada diretamente no código python, assim não precisamos adicionar as dependências da folga de corte ao software de modelagem.
    </p>
    <p>
        Agora com as nossas variáveis definidas, sendo elas o diâmetro do furo, o diâmetro da base do punção, o diâmetro da base da matriz e a folga de corte, podemos dar sequência à nossa interação.
    </p>
    <br>
</div>

## PASSO 2 - Apresentar os Resultados
<div>
    <p>
        O nosso próximo passo é apresentar o resultado das nossas variáveis so SolidWorks, em um formato que ele possa reconhecer e assim utilizar esses valores.
    </p>
    <p>
        Sabendo disso, vamos utilizar o python para criar um arquivo de texto, contendo os valores calculados e adequadamente atribuidos às variáveis no seguinte formato:<br>
        "nome_da_variável" = valor_atribuído
    </p>
    <p>
        Podemos gerar o arquivo txt através do comando with open(f'{file_name}.txt', 'w') e utilizar o método writelines para escrever cada uma das nossas variáveis. Veja, como por exemplo, o trecho do nosso código:
    </p>

```Python
    ...
        with open(f'{file_name}.txt', 'w') as file:
            file.writelines(f'"hole_diameter" = {hole_diameter()}\n')
            file.writelines(f'"die_clearance" = {die_clearance()}\n')
            file.writelines(f'"punch_base" = {punch_base()}\n')
            file.writelines(f'"die_base" = {die_base()}\n')
    ...
```



Como resultado do nosso exemplo, temos o nosso arquivo de texto com o seguinte conteúdo:



```
    "hole_diameter" = 3.0
    "die_clearance" = 4.8
    "punch_base" = 30
    "die_base" = 60
```

</div>

## PASSO 3 - Adicionar as variáveis ao SolidWorks


<h4 align="center"> 
	🚧  🚀 Em construção...  🚧
</h4>