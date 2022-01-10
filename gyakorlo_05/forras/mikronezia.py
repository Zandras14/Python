from country import Country
from typing import List



class Mikronezia:
    def __init__(self):
        self.countries: List[Country] = []
        self.sep = ':'
    def read_content(self):
        file_name = 'gyakorlo_05/forras/countries.txt'
        fp = open(file_name, 'r',encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()

    def convert_content(self):
        for line in self.lines[1::]:            
            (id, name, area, population) = line.split('#')
            country = Country(id, name, int(area), int(population))
            self.countries.append(country)

    # Legnépesebb ország
    def most_populated(self):
        max_pop = self.countries[0]
        for country in self.countries:
            if country.population > max_pop.population:
                max_pop = country
        print('A legnépesebb ország:',
                max_pop.name, 
                max_pop.population)
            

    # Legkisebb területű ország
    def smallest_area(self):
        min_area = self.countries[0]
        for country in self.countries:
            if country.area < min_area.area:
                min_area = country
        print('A legkisebb területű ország adatai:',
                min_area.id, 
                min_area.name, 
                min_area.area, 
                min_area.population)
            

    # 99 ezernél kisebb népesség
    def less_than_ninety_nine_thousand(self):
        pop_less = self.countries[0]
        for country in self.countries:
            if country.population < 99000:
                pop_less = country
                print('A 99 ezernél kisebb népességő országok',
                        pop_less.name,
                        pop_less.population)
                

    # Hány 500 négyeztkilométernél nagyobb területi ország van?
    def more_than_five_hunderd_area(self):
        more = 0
        for country in self.countries:
            if country.area > 500:
                more += 1
        print('Ennyi 500 négyeztkilométernél nagyobb területi ország van', more)
                

    # Hány ország nevében szerepel a "sziget" szó?
    def island_word_in_name(self):
        count = 0
        for country in self.countries:
            if country.name.find('sziget') != -1:
                count += 1
        print('A sziget szó ennyi ország nevében szerepel',count)
            

    # Az országok területe összesen
    def sum_areas(self):
        all_area = 0
        for country in self.countries:
            if country.area:
                all_area = all_area + country.area
        print('Az országok területe összesen %5d négyzetkilométer' % all_area)
            

    # Az országok népességének átlaga
    def population_average(self):
        average_pop = 0
        count = 0
        for country in self.countries:
            if country.population:
                count += 1
                average_pop = (average_pop + country.population)
        print('Az országok népességének átlaga %6d'% (average_pop/count))


    # Állapítsuk meg, hogy egyszavas, vagy nem, a név
    def is_one_word(self,country):
        return True

    def write_a_country(self, fp, country):
        fp.write(country.id)
        fp.write(self.sep)
        fp.write(country.name)
        fp.write(self.sep)
        fp.write(str(country.area))
        fp.write(self.sep)
        fp.write(str(country.population))
        fp.write('\n')


    def write_one_word(self):
        fp = open('gyakorlo_05/forras/oneword.txt', 'w', encoding='utf-8')
        for country in self.countries:
            if self.is_one_word(country):
                self.write_a_country(fp, country)
        fp.close()


mikro = Mikronezia()
mikro.read_content()
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()
mikro.more_than_five_hunderd_area()
mikro.island_word_in_name()
mikro.sum_areas()
mikro.population_average()
#mikro.is_one_word()
mikro.write_one_word()
