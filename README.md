# Análise de dados esportiva com Api
<hr>

<p>Bot-telegram capaz de análisar jogos ao-vivo e retornar alertas baseados na estratégia de apostadores</p>
<h6>O que é retornado</h6>
<ul>
<li>Dados live(casa, visitante, liga, estádio)</li>
<li>Dados goals(chutes, goals..)</li>
<li>Dados cards(Cartões amarelos, vermelhos)</li>
<li>Dados Under/Over casas de aposta(mais de..., menos de...)</li>
<li>Probabilidades(vítoria, derrota, empate)</li>
<li>Dados Geo(Informações geográficas)</li>
<li>Calculos da Api(MH1,MH2,APPM1,APPM2,Exg)</li>
</ul>

# Como conseguir a Api com os dados?

<p>Já está disponível no código fonte!!</p>
<p>você também pode encontrar o link dela  <a href="https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores?include=weatherReport,additionalInfo,league,stats,pressureStats,probabilities">aqui</a>!!</p>


# Como funciona os Cálculos da Api?

<p>É utilizado o website da <a href="https://playscores.com/scanner-futebol-online/ao-vivo">PlayScores</a> para a base da construção de estratégias</p>

# Posso personalizar o código com minhas estrátegias?

<p>Sim, o propósito é você concentrar e entender os dados estátisticos da partida/liga e desenvolver estratégias bem aplicadas que demonstre assertividade na aplicação de apostas em live.<p>
<p>Entenda o mercado de apostas e automotize seu robô!!</P>


# Blibiotecas utilizadas

<p>Time, requests, json,telegram</p>

# Como o código foi estruturado?

<ul>
<li>Classe com o inicializador do bot(recebe:token,chat_id)</li>
<li>função que configura a Api da playscores</li>
<li>função que configura o recebimento de dados do JSON[DATA]</li>
<li>função que retorna alertas baseados nas estratégias pré definidas em um periódo de análise</li>
</ul>

# bot_telegram
