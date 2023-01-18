
import time
import requests
import telegram
import json


class Bot_telegram:
    def __init__(self, token, chat_id):
        self._token = token
        self._chatid = chat_id

        self._json_elements = {}

    # Confg Api (Recebe os dados dos jogos ao vivo)

    def confg_Api(self):
        url = "https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores?"

        querystring = {"include": "weatherReport,additionalInfo,league,stats,pressureStats,probabilities"}

        payload = ""
        headers = {"cookie": "route=93d3fcde97da7043d51f34c8d08924d3; SRVGROUP=common"}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        dic_response = response.json()
        self._json_elements = dic_response

    # JSON (DATA) - (Confg de dados do JSON recebido em um novo dicionario)
    def data_json_Api(self, espera_alerta):
        data_elements = []
        self.confg_Api()
        for tag in self._json_elements["data"]:

            if tag["stats"] is None:
                continue

            if tag["pressureStats"] is None:
                continue

            # time data
            visitante = tag["awayTeam"]["name"]
            casa = tag["homeTeam"]["name"]
            liga = tag["league"]["name"]

            # Current time (tempo de jogo)
            minuto = tag["currentTime"]["minute"]
            segundo = tag["currentTime"]["second"]
            dia_de_game = tag["date"]

            # corners (cantos)

            cantos_casa = tag["stats"]["corners"]["home"]
            cantos_visitante = tag["stats"]["corners"]["away"]

            # atakks (ataques)

            ataques_casa = tag["stats"]["attacks"]["home"]
            ataques_visitante = tag["stats"]["attacks"]["away"]

            # atakks dangers (perigos de ataque)

            ataques_dg_casa = tag["stats"]["dangerousAttacks"]["home"]
            ataques_dg_visitante = tag["stats"]["dangerousAttacks"]["away"]

            # gols (gols de cada time)

            gols_casa = tag["stats"]["goals"]["home"]
            gols_visitante = tag["stats"]["goals"]["away"]

            # chutes fora (fora kicks)

            chutes_fora_home = tag["stats"]["shotsOffgoal"]["home"]
            chutes_fora_visitante = tag["stats"]["shotsOffgoal"]["away"]

            # chutes em gol (on goal kicks)

            chutes_gol_home = tag["stats"]["shotsOngoal"]["home"]
            chutes_gol_visitante = tag["stats"]["shotsOngoal"]["away"]

            # cards yellows (cartões amarelos)

            cardy_home = tag["stats"]["yellowcards"]["home"]
            cardy_visitante = tag["stats"]["yellowcards"]["away"]

            # analises mh e ppm

            # mh's

            # mh1

            mh1_home = tag["pressureStats"]["mh1"]["home"]
            mh1_visitante = tag["pressureStats"]["mh1"]["away"]

            # mh2

            mh2_home = tag["pressureStats"]["mh2"]["home"]
            mh2_visitante = tag["pressureStats"]["mh2"]["away"]

            # mh3

            mh3_home = tag["pressureStats"]["mh3"]["home"]
            mh3_visitante = tag["pressureStats"]["mh3"]["away"]

            # appm's

            # appm1

            appm1_home = tag["pressureStats"]["appm1"]["home"]
            appm1_visitante = tag["pressureStats"]["appm1"]["away"]

            # appm2

            appm2_home = tag["pressureStats"]["appm2"]["home"]
            appm2_visitante = tag["pressureStats"]["appm2"]["away"]

            # exg

            exg_home = tag["pressureStats"]["exg"]["home"]
            exg_visitante = tag["pressureStats"]["exg"]["away"]

            # probabilidades
            prob_casa = tag["probabilities"]["home"]
            prob_visitante = tag["probabilities"]["away"]
            prob_empate = tag["probabilities"]["draw"]

            prob_mais1_5 = tag["probabilities"]["over_1_5"]
            prob_menos1_5 = tag["probabilities"]["under_1_5"]

            data_elements.append({"Dados_jogo": [casa, visitante, liga],
                                  "Tempo_jogo": minuto,
                                  "Cards_Y": [cardy_home, cardy_visitante],
                                  "Cantos_jogo": [cantos_casa, cantos_visitante],
                                  "probb_jogo": [prob_casa, prob_visitante, prob_empate],
                                  "1_5_ap": [prob_mais1_5, prob_menos1_5],
                                  "chutes_gol": [chutes_gol_home, chutes_gol_visitante, chutes_fora_home,
                                                 chutes_fora_visitante],
                                  "appm1": [appm1_home, appm1_visitante],
                                  "appm2": [appm2_home, appm2_visitante],
                                  "exg": [exg_home, exg_visitante],
                                  "mh1": [mh1_home, mh1_visitante],
                                  "goals": [gols_casa, gols_visitante],
                                  "atkdg": [ataques_dg_casa, ataques_dg_visitante],
                                  "chutesgol": [chutes_gol_home, chutes_gol_visitante]
                                  })
        return data_elements
    # União das estrategias de alerta e corpo do texto de alerta

    # Você pode personalizar as estrategias ao seu favor
    def gera_alerts(self):
        text__ = ""
        sair = 0
        while True:
            dict_elements = self.data_json_Api(25)
            for time_do_time in dict_elements:
                if time_do_time["Tempo_jogo"] < 70 and time_do_time["Tempo_jogo"] != 45:
                    # APPM1 (Ataques perigosos)
                    if (time_do_time["appm1"][0] + time_do_time["appm1"][1]) / 2 >= 1.8:
                        text__ = f"""""
                                                              Arquibancada teste 🏆⚽️💻
                                                              Casa X Visitante
                                                              times: {time_do_time["Dados_jogo"][0]}  🆚  {time_do_time["Dados_jogo"][1]}

                                                              liga: {time_do_time["Dados_jogo"][2]} 🚨

                                                              tempo de jogo: {time_do_time["Tempo_jogo"]} min ⏱

                                                              goals: {time_do_time["goals"][0]} X {time_do_time["goals"][1]} 🥅

                                                              Chutes ao gol: {time_do_time["chutes_gol"][0]} x {time_do_time["chutes_gol"][1]} ✅
                                                              Chutes fora: {time_do_time["chutes_gol"][2]} x {time_do_time["chutes_gol"][3]} ❌

                                                              cartões amarelos: {time_do_time["Cards_Y"][0]} x {time_do_time["Cards_Y"][0]} 🟨


                                                              ataques perigosos: {time_do_time["atkdg"][0]} x {time_do_time["atkdg"][1]} ⚠️

                                                              Probabilidade: 
                                                              __________________________________
                                                              Casa- {time_do_time["probb_jogo"][0]:.0f} % ⬆️ 

                                                              Empate- {time_do_time["probb_jogo"][2]:.0f} %  ⚪️

                                                              Visitante- {time_do_time["probb_jogo"][1]:.0f} % ⬇️
                                                              ____________________________________

                                                              escanteios: {time_do_time["Cantos_jogo"][0]} x {time_do_time["Cantos_jogo"][1]} 🚩

                                                              tipo: APPM1(Ataques por min maior que 5.5)
                                                          """""
                        if not text__:
                            continue
                        else:

                            url_base = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatid}&text={text__.replace('    ', '')}"
                            results = requests.get(url_base)
                            sair += 1
                            print(
                                f'{time_do_time["Dados_jogo"][0]} X {time_do_time["Dados_jogo"][1]} - minuto: {time_do_time["Tempo_jogo"]} alert:{sair}')
                    # mh1 (Chances de gol)

                    if 85 > time_do_time["Tempo_jogo"] > 5 and time_do_time["Tempo_jogo"] != 45:
                        if time_do_time["mh1"][0] >= 25 or time_do_time["mh1"][1] >= 25:
                            text__ = f"""""
                                                                                 Arquibancada teste 🏆⚽️💻
                                                                                 Casa X Visitante
                                                                                 times: {time_do_time["Dados_jogo"][0]}  🆚  {time_do_time["Dados_jogo"][1]}

                                                                                 liga: {time_do_time["Dados_jogo"][2]} 🚨

                                                                                 tempo de jogo: {time_do_time["Tempo_jogo"]} min ⏱

                                                                                 goals: {time_do_time["goals"][0]} X {time_do_time["goals"][1]} 🥅

                                                                                 Chutes ao gol: {time_do_time["chutes_gol"][0]} x {time_do_time["chutes_gol"][1]} ✅
                                                                                 Chutes fora: {time_do_time["chutes_gol"][2]} x {time_do_time["chutes_gol"][3]} ❌

                                                                                 cartões amarelos: {time_do_time["Cards_Y"][0]} x {time_do_time["Cards_Y"][0]} 🟨


                                                                                 ataques perigosos: {time_do_time["atkdg"][0]} x {time_do_time["atkdg"][1]} ⚠️

                                                                                 Probabilidade: 
                                                                                 ________________________________
                                                                                 Casa- {time_do_time["probb_jogo"][0]:.0f} % ⬆️ 

                                                                                 Empate- {time_do_time["probb_jogo"][2]:.0f} %  ⚪️

                                                                                 Visitante- {time_do_time["probb_jogo"][1]:.0f} % ⬇️
                                                                                 __________________________________

                                                                                 escanteios: {time_do_time["Cantos_jogo"][0]} x {time_do_time["Cantos_jogo"][1]} 🚩

                                                                                 tipo: MH1(Chances de gol)
                                                                             """""
                            if not text__:
                                continue
                            else:
                                url_base = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatid}&text={text__.replace('    ', '')}"
                                results = requests.get(url_base)
                                sair += 1
                                print(
                                    f'{time_do_time["Dados_jogo"][0]} X {time_do_time["Dados_jogo"][1]} - minuto: {time_do_time["Tempo_jogo"]} alert:{sair}')

                # Cantos tempo 1 (Tiros de canto 1 tempo)
                if time_do_time["Tempo_jogo"] < 40:
                    if (time_do_time["Cantos_jogo"][0] + time_do_time["Cantos_jogo"][1]) / 2 >= 1.8:
                        text__ = f"""""
                                                               Arquibancada teste 🏆⚽️💻
                                                               Casa X Visitante
                                                               times: {time_do_time["Dados_jogo"][0]}  🆚  {time_do_time["Dados_jogo"][1]}

                                                               liga: {time_do_time["Dados_jogo"][2]} 🚨

                                                               tempo de jogo: {time_do_time["Tempo_jogo"]} min ⏱

                                                               goals: {time_do_time["goals"][0]} X {time_do_time["goals"][1]} 🥅

                                                               Chutes ao gol: {time_do_time["chutes_gol"][0]} x {time_do_time["chutes_gol"][1]} ✅
                                                               Chutes fora: {time_do_time["chutes_gol"][2]} x {time_do_time["chutes_gol"][3]} ❌

                                                               cartões amarelos: {time_do_time["Cards_Y"][0]} x {time_do_time["Cards_Y"][0]} 🟨


                                                               ataques perigosos: {time_do_time["atkdg"][0]} x {time_do_time["atkdg"][1]} ⚠️

                                                               Probabilidade: 
                                                               _______________________________
                                                               Casa- {time_do_time["probb_jogo"][0]:.0f} % ⬆️ 

                                                               Empate- {time_do_time["probb_jogo"][2]:.0f} %  ⚪️

                                                               Visitante- {time_do_time["probb_jogo"][1]:.0f} % ⬇️
                                                               __________________________________

                                                               escanteios: {time_do_time["Cantos_jogo"][0]} x {time_do_time["Cantos_jogo"][1]} 🚩

                                                               tipo: TC1(Tiros de canto 1° tempo)
                                                           """""
                        if not text__:
                            continue
                        else:
                            url_base = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatid}&text={text__.replace('    ', '')}"
                            results = requests.get(url_base)
                            sair += 1
                            print(
                                f'{time_do_time["Dados_jogo"][0]} X {time_do_time["Dados_jogo"][1]} - minuto: {time_do_time["Tempo_jogo"]} alert:{sair}')

                # Cantos tempo 1 and 2 (Tiros de canto mais de 65min)

                if 85 > time_do_time["Tempo_jogo"] >= 46:
                    if (time_do_time["Cantos_jogo"][0] + time_do_time["Cantos_jogo"][1]) / 2 >= 5:
                        text__ = f"""""
                                                               Arquibancada teste 🏆⚽️💻
                                                               Casa X Visitante
                                                               times: {time_do_time["Dados_jogo"][0]}  🆚  {time_do_time["Dados_jogo"][1]}

                                                               liga: {time_do_time["Dados_jogo"][2]} 🚨

                                                               tempo de jogo: {time_do_time["Tempo_jogo"]} min ⏱

                                                               goals: {time_do_time["goals"][0]} X {time_do_time["goals"][1]} 🥅

                                                               Chutes ao gol: {time_do_time["chutes_gol"][0]} x {time_do_time["chutes_gol"][1]} ✅
                                                               Chutes fora: {time_do_time["chutes_gol"][2]} x {time_do_time["chutes_gol"][3]} ❌

                                                               cartões amarelos: {time_do_time["Cards_Y"][0]} x {time_do_time["Cards_Y"][0]} 🟨


                                                               ataques perigosos: {time_do_time["atkdg"][0]} x {time_do_time["atkdg"][1]} ⚠️

                                                               Probabilidade: 
                                                               __________________________________
                                                               Casa- {time_do_time["probb_jogo"][0]:.0f} % ⬆️ 

                                                               Empate- {time_do_time["probb_jogo"][2]:.0f} %  ⚪️

                                                               Visitante- {time_do_time["probb_jogo"][1]:.0f} % ⬇️
                                                               ____________________________________

                                                               escanteios: {time_do_time["Cantos_jogo"][0]} x {time_do_time["Cantos_jogo"][1]} 🚩

                                                               tipo: TC12(Tiros de canto 2° tempo)
                                                           """""
                        if not text__:
                            continue
                        else:
                            url_base = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatid}&text={text__.replace('    ', '')}"
                            results = requests.get(url_base)
                            sair += 1
                            print(
                                f'{time_do_time["Dados_jogo"][0]} X {time_do_time["Dados_jogo"][1]} - minuto: {time_do_time["Tempo_jogo"]} alert:{sair}')

            time.sleep(60)
            # estrategias


if __name__ == "__main__":
    bot = Bot_telegram('5603315518:AAHDs2Z7Q9bWZPZmv3HZYKpHMvZ1iZf0nZ8', '-1001882777748')
    bot.gera_alerts()
