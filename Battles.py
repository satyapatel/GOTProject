from MySqlDbHandler import MySqlHandler

class Battles:

    @staticmethod
    def get_battle_map(row):
        battle = {}
        battle['id'] = row[0]
        battle['name']= row[1]
        battle['year'] = row[2]
        battle['battle_number'] = row[3]
        battle['attacker_king'] = row[4]
        battle['defender_king'] = row[5]
        battle['attacker_1'] = row[6]
        battle['attacker_2'] = row[7]
        battle['attacker_3'] = row[8]
        battle['attacker_4'] = row[9]
        battle['defender_1'] = row[10]
        battle['defender_2'] = row[11]
        battle['defender_3'] = row[12]
        battle['defender_4'] = row[13]
        battle['attacker_outcome'] = row[14]
        battle['battle_type'] = row[15]
        battle['major_death'] = row[16]
        battle['major_capture'] = row[17]
        battle['attacker_size'] = row[18]
        battle['defender_size'] = row[19]
        battle['attacker_commander'] = row[20]
        battle['defender_commander'] = row[21]
        battle['summer'] = row[22]
        battle['location'] = row[23]
        battle['region'] = row[24]
        battle['note'] = row[25]
        return battle

    @staticmethod
    def get_all_battles():
        db_client = MySqlHandler()
        sql = "SELECT * FROM battles"
        results = db_client.execute_query(sql)
        all_battles = []
        for row in results:
            all_battles.append(Battles.get_battle_map(row))
        db_client.close()
        return all_battles


    @staticmethod
    def get_number_of_batles():
        sql = "SELECT count(*) FROM battles"
        db_client = MySqlHandler()
        results = db_client.execute_query(sql)
        count = 0
        for row in results:
            count = row[0]
        db_client.close()
        return count

    @staticmethod
    def get_battles_stats():
        sqlAttackerKing = "select attacker_king from (select attacker_king , count(*) as count from battles group by attacker_king) as temp where count = (select max(count) from (select attacker_king , count(*) as count from battles group by attacker_king) as temp)"
        sqlDefenderKing = "select defender_king from (select defender_king , count(*) as count from battles group by defender_king) as temp where count = (select max(count) from (select defender_king , count(*) as count from battles group by defender_king) as temp)"
        sqlRegion = "select region from (select region , count(*) as count from battles group by region) as temp where count = (select max(count) from (select region , count(*) as count from battles group by region) as temp)"
        sqlAttackerOutcom = "select attacker_outcome , count(*) from battles where  attacker_outcome in('win','loss')  group by attacker_outcome order by 1"
        sqlDefenderSize = "select avg(defender_size), max(defender_size) , min(defender_size) from battles where defender_size!=' '"
        sqlBattleTypes = "select distinct(battle_type) from battles where battle_type!=' '"
        db_client = MySqlHandler()

        most_active = {}
        attacker_outcome = {}
        defender_size = {}
        battle_type = []


        results = db_client.execute_query(sqlAttackerKing)
        for row in results:
            most_active["attacker_king"] = row[0]

        results = db_client.execute_query(sqlDefenderKing)
        for row in results:
            most_active["defender_king"] = row[0]

        results = db_client.execute_query(sqlRegion)
        for row in results:
            most_active["region"] = row[0]

        results = db_client.execute_query(sqlAttackerOutcom)
        for row in results:
            attacker_outcome[row[0]] = row[1]

        results = db_client.execute_query(sqlDefenderSize)
        for row in results:
            defender_size["average"] = row[0]
            defender_size["max"] = row[1]
            defender_size["min"] = row[2]

        results = db_client.execute_query(sqlBattleTypes)
        for row in results:
            battle_type.append(row[0])

        db_client.close()



        result_map = {}
        result_map["most_active"] = most_active
        result_map["attacker_outcome"] = attacker_outcome
        result_map["defender_size"] = defender_size
        result_map["battle_type"] = battle_type
        return result_map

    @staticmethod
    def search_battles(colum_map):
        str = " 1 = 1 "
        for key, value in colum_map.iteritems():
            if value and value != 'undefined':
                str = str + " and " + key + " = '" + value +"'"

        sql = "SELECT * FROM battles WHERE" + str
        db_client = MySqlHandler()
        results = db_client.execute_query(sql)
        all_battles = []
        for row in results:
            all_battles.append(Battles.get_battle_map(row))
        db_client.close()
        return all_battles






