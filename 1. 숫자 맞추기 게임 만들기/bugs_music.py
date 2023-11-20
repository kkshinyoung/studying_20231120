import pandas as pd
from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text
        print('Url 입력이 되었습니다.')

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs=({"class":self.class_name[1]}))
        ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        for i in ls2:
            self.artist_ls.append(i.find("a").text)
        print('데이터가 수집 되었습니다.')

    def insert_dict(self):

        # 방법 1. range
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        # 방법 2. zip
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        # 방법 3. enumerate
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]
        print('데이터가 딕셔너리에 추가 되었습니다.')
        print('딕셔너리에 저장된 데이터는 다음과 같습니다')
        print(dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print('딕셔너리 데이터를 데이터프레임에 이전 했습니다.')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print('데이터가 CSV 파일에 저장되었습니다.')



    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-프로그램종료\n'
                         '1-url 입력\n'
                         '2-데이터 수집\n'
                         '3-데이터를 딕셔너리에 추가\n'
                         '4-딕셔너리를 데이터프레임에 이전\n'
                         '5-csv 로 저장\n')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('https://music.bugs.co.kr/chart/track/day/total')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_dict()
            elif menu == '4':
                bugs.dict_to_dataframe()
            elif menu == '5':
                bugs.df_to_csv()
            else:
                print('Wrong Number')
                continue

if __name__ == '__main__':
    BugsMusic.main()