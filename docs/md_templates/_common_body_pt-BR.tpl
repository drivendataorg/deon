<h1><b>Um checklist de ética para cientistas de dados</b></h1>


`deon` é uma ferramenta de linha de comando que permite facilmente acrescentar um checklist de ética para seus projetos de ciência de dados. Suportamos a criação de um arquivo novo, isolado ou acrescentar um checklist a uma análise existente em [muitos formatos comuns](#tipos-de-arquivo-suportados).

---

**δέον** • (déon) [n.] (_Grego antigo_) <small><a  href="https://en.wiktionary.org/wiki/%CE%B4%CE%AD%CE%BF%CE%BD#Ancient_Greek" target="_blank" style="text-decoration: none; color: #6d6d6d">wikitionary</a></small>
 > Dever; aquilo que vincula, necessário, certo, apropriado.

--------

O diálogo sobre a ética na ciência de dados, aprendizado de máquina e IA é cada vez mais importante. A meta do ‘deon’ é colocar esse diálogo em evidência e criar lembretes concretos e acionáveis para os desenvolvedores que tenham influência sobre como a ciência de dados é feita.

# Histórico e perspectiva

Temos uma perspectiva em particular com esse pacote que usaremos para tomar decisões sobre contribuições, questões, RP e outras atividades de manutenção e suporte.

Em primeiro lugar, nossa meta não é arbitrar quais questões éticas merecem inclusão. Temos um [processo para mudar a checklist padrão](#mudando-a-checklist), mas acreditamos que muitas preocupações específicas de certos ramos não estão incluídas e as equipes podem se beneficiar de desenvolver [checklists customizados](#checklists-customizadas). Nem todo item da checklist será relevante. Encorajamos as equipes a remover itens, seções ou marcar itens como “N/A” de acordo com o que as preocupações de seus projetos ditarem.

Segundo, construímos nossa lista inicial a partir de itens propostos em [múltiplos checklists que citamos](#checklist-citations). Este checklist foi fortemente inspirado em um artigo escrito por Mike Loukides, Hilary Mason e DJ Patil e publicado pela O’Reilly: [“Of Oaths and Checklists”](https://www.oreilly.com/ideas/of-oaths-and-checklists). Temos um débito enorme com o pensamento que nos precedeu e esperamos nos engajar com a discussão corrente sobre checklists para a ética da ciência de dados.

Terceiro, acreditamos no poder dos exemplos para trazer os princípios da ética de dados para a experiência humana. Este repositório inclui uma [lista de exemplos do mundo real](http://deon.drivendata.org/examples/) conectado com cada item na checklist padrão. Nós te encorajamos a contribuir com casos de uso relevantes que você acredite que possa beneficiar a comunidade por seu exemplo. Além disso, se você tiver um tópico, ideia ou comentário que não pareça adequado para a documentação, por favor coloque na [página da wiki](https://github.com/drivendataorg/deon/wiki) para este projeto!

Quarto, não cabe aos cientistas de dados sozinhos decidir qual o curso de ação ético a seguir. Isso sempre foi uma responsabilidade das organizações que são parte da sociedade civil. Este checklist foi construído para provocar diálogos ao redor de questões em que os cientistas de dados têm particular responsabilidade e perspective. Este diálogo deve ser parte de um compromisso organizacional maior de fazer o que é certo.

Quinto, acreditamos que o benefício primário de um checklist é assegurar que não deixamos passar tarefas importantes. Algumas vezes é difícil, com prazos curtos e uma demanda para fazer várias coisas ao mesmo tempo, nos assegurar de que fizemos o trabalho difícil de pensar no todo. Este pacote pretende ajudar a tomar em conta que essas discussões aconteçam, mesmo em ambientes de rápida movimentação. Ética é uma matéria difícil e esperamos que algumas das conversas que surjam deste checklist sejam difíceis.

Sexto, estamos trabalhando num nível de abstração que não pode concretamente recomendar uma ação específica (p.ex., “remova a variável X do seu modelo”). Quase todos os itens na checklist são para provocar uma discussão entre agentes de boa-fé que levam a sério sua responsabilidade ética. Por causa disso, a maior parte dos itens foi enquadrado como pontos a discutir ou considerar. Equipes vão querer documentar essas discussões e decisões para a posteridade.

Sétimo, não podemos definir de forma exauriente todos os termos que aparecem na checklist. Alguns desses termos estão abertos a interpretação ou significam coisas diferentes em diferentes contextos. Recomendamos que quando relevante os usuários criem seu próprio glossário para referência.

Oitavo, queremos evitar quaisquer itens que caiam estritamente no reino de melhores práticas estatísticas. Ao invés disso, queremos frisar as áreas onde precisamos prestar particular atenção acima e para além de melhores práticas.

Nono, queremos que todos os itens da checklist sejam o mais simples possível (mas não mais simples do que isso), e possam ser acionáveis.

# Usando esta ferramenta

<img src="https://s3.amazonaws.com/drivendata-public-assets/deon_demo.svg">

## Pré-requisitos

 - Python >3.6: Seu projeto não precisa ser em Python 3, mas você vai precisar de Python 3 para executar esta ferramenta.

## Instalação

```
$ pip install deon
```

ou

```
$ conda install deon -c conda-forge
```

## Uso simples

Recomendamos acrescentar uma checklist como o primeiro passo em seu projeto de ciência de dados. Depois de criar sua pasta de projeto, você pode rodar

```
$ deon -o ETHICS.md
```

Isso criará um arquivo markdown chamado ‘ETHICS.md’ que você pode acrescentar diretamente a seu projeto.

Para análises isoladas, você pode acrescentar a checklist num notebook Jupyter ou arquivo RMarkdown usando a opção ‘-o’ para indicar o arquivo de saída. ‘deon’ vai automaticamente acrescentar ao arquivo que eventualmente exista.

```
$ jupyter notebook minha-analise.ipynb

...

$ deon -o minha-analise.ipynb  # acrescenta células ao arquivo de saída existente
```

Esta checklist pode ser usada por indivíduos ou equipes para se assegurar de que rever as implicações éticas de seu trabalho é parte de todo projeto. A checklist serve de ponto de partida e deveria iniciar discussões mais profundas e abrangentes ao invés de substituí-las.

## Mostre sua medalha Deon orgulhosamente
Você pode acrescentar uma medalha Deon à documentação de seu projeto, como o README, para encorajar a adoção mais ampla dessas práticas éticas na comunidade de ciência de dados.

### Medalha HTML
```html
<a href="http://deon.drivendata.org/">
    <img src="https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square" alt="Medalha Deon" />
</a>
```

### Medalha Markdown

```
[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)
```

# Tipos de arquivo suportados

Aqui estão os tipos de arquivo correntemente suportados. Aceitamos pull requests com novos tipos de arquivo se houver uma causa forte para o uso ampliado daquele tipo de arquivo.

{% for f, n in supported_formats.items() %}
- `{{ f }}`: {{ n }}{% endfor %}

# Opções de linha de comando

```
{{ cli_options }}
```

# Checklist padrão

<hr class="checklist-buffer"/>

{{ default_checklist }}

<hr class="checklist-buffer"/>

# Checklists customizadas

Esta não é a única checklist de ética, mas tentamos capturar padrões razoáveis que são normalmente suficientes para ser amplamente utilizados. Para seus próprios projetos com questões particulares, recomendamos seu próprio arquivo ‘checklist.yml’ que é mantido por nossa equipe e passado a esta ferramenta com a opção ‘-l’.

As checklists customizadas precisam seguir o mesmo esquema do ‘checklist.yml’. É necessário um ‘title’ (título) de nível superior que é uma frase, e ‘sections’ (seções) que são uma lista. Cada seção na lista ‘sections’ precisa ter um ‘title’ (título), um ‘section_id’ (identificador de seção) e então uma lista de ‘lines’ (linhas). Cada linha precisa ter um ‘line_id’ (identificador de linha), um ‘line_summary’ (resumo da linha), que é um resumo de 1-3 palavras, e uma frase ‘line’ que é o conteúdo. O formato é o seguinte:

```
title: TITLE
sections:
  - title: SECTION TITLE
    section_id: SECTION NUMBER
    lines:
        - line_id: LINE NUMBER
          line_summary: LINE SUMMARY
          line: LINE CONTENT
```

# Mudando a checklist

Por favor confira [o enquadramento](#histórico-e-perspectiva) para uma compreensão de nossa perspectiva. Partindo dessa perspectiva, tomaremos em consideração mudanças à checklist padrão que se encaixarem naquela perspectiva e seguirem este processo.

Nossa meta é ter itens de checklist que sejam acionáveis como parte de um trabalho de revisão de ciência de dados ou seja parte de um plano. Por favor evite sugerir itens demasiado vagos (p.ex. “não prejudique ninguém”) ou demasiado específicos (p.ex. “remova os CPFs dos dados”).
**Nota: Este processo é experimental e sujeito a mudanças baseadas em quão bem funcionem. Nossa meta é evitar debates acalorados nos tópicos de problemas enquanto ainda criamos uma ferramenta que facilite o trabalho de acrescentar uma checklist de ética a um projeto.**

Para requisitar uma mudança, por favor crie uma issue que comece com uma dessas palavras: CREATE (criar), UPDATE (atualizar), DELETE (apagar). Há QUATRO requerimentos para pedir uma mudança na checklist:

 - Uma justificativa para a mudança
 - Ao menos dez votos positivos da comunidade para a issue
 - Um exemplo publicado (acadêmico ou artigo da imprensa) de quando negligenciar o princípio criou um dano concreto (artigos que discutam danos em potencial ou hipotéticos não serão considerados suficientes)
 - Uma consideração de itens relacionados que já existem, e por que essa mudança é diferente do que já existe.

Um pull request para acrescentar um item deveria mudar:

  - [`deon/assets/checklist.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/checklist.yml): contém os itens da checklist padrão
  - [`deon/assets/examples_of_ethical_issues.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/examples_of_ethical_issues.yml): contém exemplos de danos causados quando o item não foi tomado em conta.

# Discussão e comentário

Em acréscimo a esta documentação, as [páginas wiki para o repositório GitHub](https://github.com/drivendataorg/deon/wiki) estão habilitadas. É um bom lugar para compartilhar links e discussão de como as checklists são usadas na prática.

Se você tiver um tópico, ideia ou comentário que não pareça adequado para a documentação, por favor acrescente na wiki!

# Referências, leitura e mais

Uma discussão robusta da ética dos dados é importante para a profissão. A meta desta ferramenta é facilitar a implementação de revisões éticas dentro de projetos técnicos. Há vários grandes recursos se você quiser pensar sobre a ética dos dados, e nós te encorajamos a fazer isso!

## Citações de checklists

Estamos entusiasmados de ver tantos artigos surgindo sobre ética de dados! A curta lista abaixo inclui artigos que diretamente informaram o conteúdo da checklist, bem como alguns estudos de caso e pontos que provocam a pensar no todo.

- [Of oaths and checklists](https://www.oreilly.com/ideas/of-oaths-and-checklists)
- How to build ethics into AI ([Part I](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-i-bf35494cce9) and [Part II](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-ii-a563f3372447))
- [An ethical checklist for data science](https://dssg.uchicago.edu/2015/09/18/an-ethical-checklist-for-data-science/)
- [How to recognize exclusion in AI](https://medium.com/microsoft-design/how-to-recognize-exclusion-in-ai-ec2d6d89f850)
- [Case studies in data ethics](https://www.oreilly.com/ideas/case-studies-in-data-ethics)
- [Technology is biased too. How do we fix it?](https://fivethirtyeight.com/features/technology-is-biased-too-how-do-we-fix-it/)
- [The dark secret at the heart of AI](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/)

## Onde as coisas deram errado

Para tornar as ideias contidas na checklist mais concretas, compilamos [exemplos](http://deon.drivendata.org/examples/) de situações em que as coisas deram errado. Estão vinculadas a questões da checklist para ajudar a iluminar onde no processo as discussões éticas poderiam ter ajudado a criar uma correção no curso.

Nós aceitamos contribuições! Siga [estas instruções](https://github.com/drivendataorg/deon/blob/main/CONTRIBUTING.md) para acrescentar um exemplo.

## Ferramentas relacionadas

Há outros grupos trabalhando na ética de dados e pensando sobre como ferramentas podem ajudar neste espaço. Aqui estão alguns dos que vimos até agora:
There are other groups working on data ethics and thinking about how tools can help in this space. Here are a few we've seen so far:

- [Aequitas](https://dsapp.uchicago.edu/aequitas/) ([github](https://github.com/dssg/aequitas))
- [Ethical OS Toolkit](https://ethicalos.org/)
- [Ethics & Algorithms Toolkit: A risk management framework for governments](http://ethicstoolkit.ai/)
- Ethics and Data Science ([ebook gratuito](https://www.amazon.com/dp/B07GTC8ZN7/ref=cm_sw_r_cp_ep_dp_klAOBb4Z72B4G)) and ([write-up](https://medium.com/@sjgadler/care-about-ai-ethics-what-you-can-do-starting-today-882a0e63d828))
