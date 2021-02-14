import numpy as np
import pandas as pd

class GDF:

    def gen_position(self, train_df):

        position_list=train_df['position'] 
        output_coder = np.zeros(len(position_list))
        output_engineer = np.zeros(len(position_list))
        output_manager = np.zeros(len(position_list))
        output_programer = np.zeros(len(position_list))
        output_productowner = np.zeros(len(position_list))
        output_cto = np.zeros(len(position_list))
        output_scrummaster = np.zeros(len(position_list))
        output_datascientist = np.zeros(len(position_list))
        output_ai = np.zeros(len(position_list))
        output_architect = np.zeros(len(position_list))
        output_infra = np.zeros(len(position_list))
        output_sp = np.zeros(len(position_list))
        
        for ind,val in enumerate(position_list):
            if 'エンジニア' in str(val):
                output_engineer[ind]=1
            if 'SE' in str(val):
                output_engineer[ind]=1
            if 'PM' in str(val):
                output_manager[ind]=1
            if 'PL' in str(val):
                output_manager[ind]=1
            if 'リーダ' in str(val):
                output_manager[ind]=1
            if 'マネジャ' in str(val):
                output_manager[ind]=1
            if 'マネージャ' in str(val):
                output_manager[ind]=1
            if 'PG' in str(val):
                output_programer[ind]=1
            if 'プログラマ' in str(val):
                output_programer[ind]=1
            if 'コーダ' in str(val):
                output_coder[ind]=1
            if 'プロダクトオーナ' in str(val):
                output_productowner[ind]=1
            if 'CTO' in str(val):
                output_cto[ind]=1
            if 'スクラム' in str(val):
                output_scrummaster[ind]=1
            if 'データ サイエンティスト' in str(val):
                output_datascientist[ind]=1
            if 'AI' in str(val):
                output_ai[ind]=1
            if 'リード' in str(val):
                output_architect[ind]=1
            if 'アーキテクト' in str(val):
                output_architect[ind]=1
            if 'インフラ' in str(val):
                output_infra[ind]=1
            if 'Android' in str(val):
                output_sp[ind]=1
            if 'iOS' in str(val):
                output_sp[ind]=1
            if 'ディレクター' in str(val):
                output_manager[ind]=1
            if '開発' in str(val):
                output_sp[ind]=1
            if 'engineering' in str(val):
                output_engineer[ind]=1
            if 'データ' in str(val):
                output_datascientist[ind]=1
            if 'Unity' in str(val):
                output_engineer[ind]=1
            if 'データ' in str(val):
                output_datascientist[ind]=1
            if '責任者' in str(val):
                output_manager[ind]=1
            if '組み込み' in str(val):
                output_engineer[ind]=1
            if '責任者' in str(val):
                output_manager[ind]=1
            if '技師' in str(val):
                output_engineer[ind]=1
            if '構築' in str(val):
                output_engineer[ind]=1
            if '講師' in str(val):
                output_engineer[ind]=1
            if 'Engineering' in str(val):
                output_engineer[ind]=1
            if '3DCG' in str(val):
                output_engineer[ind]=1
            if 'プロダクトオーナー' in str(val):
                output_scrummaster[ind]=1
                
        train_df['エンジニア']=output_engineer
        train_df['マネージャ']=output_manager
        train_df['コーダー']=output_coder
        train_df['プログラマー']=output_programer
        train_df['プロダクトオーナー']=output_productowner
        train_df['AI']=output_ai
        train_df['CTO']=output_cto
        train_df['スクラムマスタ']=output_scrummaster
        train_df['データサイエンティスト']=output_datascientist
        train_df['アーキテクト']=output_architect
        train_df['インフラ']=output_infra
        train_df['SP']=output_sp

    def gen_locale(self, train_df):
        location_list = train_df['location']
        
        output_hokkaido = np.zeros(len(location_list))
        output_tohoku = np.zeros(len(location_list))
        output_kanto = np.zeros(len(location_list))
        output_chubu = np.zeros(len(location_list))
        output_kinki = np.zeros(len(location_list))
        output_chugoku = np.zeros(len(location_list))
        output_shikoku = np.zeros(len(location_list))
        output_kyushu = np.zeros(len(location_list))
        output_okinawa = np.zeros(len(location_list))
        output_oversea = np.zeros(len(location_list))
        
        for idx,v in enumerate(location_list):
            if '北海道' in v:
                output_hokkaido[idx]=1
            elif '青森県' in v:
                output_tohoku[idx]=1
            elif '岩手県' in v:
                output_tohoku[idx]=1
            elif '宮城県' in v:
                output_tohoku[idx]=1
            elif '秋田県' in v:
                output_tohoku[idx]=1
            elif '山形県' in v:
                output_tohoku[idx]=1
            elif '福島県' in v:
                output_tohoku[idx]=1
            elif '茨城県' in v:
                output_kanto[idx]=1
            elif '栃木県' in v:
                output_kanto[idx]=1
            elif '群馬県' in v:
                output_kanto[idx]=1
            elif '埼玉県' in v:
                output_kanto[idx]=1
            elif '千葉県' in v:
                output_kanto[idx]=1
            elif '東京都' in v:
                output_kanto[idx]=1
            elif '神奈川県' in v:
                output_kanto[idx]=1
            elif '新潟県' in v:
                output_chubu[idx]=1
            elif '富山県' in v:
                output_chubu[idx]=1
            elif '石川県' in v:
                output_chubu[idx]=1
            elif '福井県' in v:
                output_chubu[idx]=1
            elif '山梨県' in v:
                output_chubu[idx]=1
            elif '長野県' in v:
                output_chubu[idx]=1
            elif '岐阜県' in v:
                output_chubu[idx]=1
            elif '静岡県' in v:
                output_chubu[idx]=1
            elif '愛知県' in v:
                output_chubu[idx]=1
            elif '三重県' in v:
                output_kinki[idx]=1
            elif '滋賀県' in v:
                output_kinki[idx]=1
            elif '京都府' in v:
                output_kinki[idx]=1
            elif '大阪府' in v:
                output_kinki[idx]=1
            elif '兵庫県' in v:
                output_kinki[idx]=1
            elif '奈良県' in v:
                output_kinki[idx]=1
            elif '和歌山県' in v:
                output_kinki[idx]=1
            elif '鳥取県' in v:
                output_chugoku[idx]=1
            elif '島根県' in v:
                output_chugoku[idx]=1
            elif '岡山県' in v:
                output_chugoku[idx]=1
            elif '広島県' in v:
                output_chugoku[idx]=1
            elif '山口県' in v:
                output_chugoku[idx]=1
            elif '徳島県' in v:
                output_shikoku[idx]=1
            elif '香川県' in v:
                output_shikoku[idx]=1
            elif '愛媛県' in v:
                output_shikoku[idx]=1
            elif '高知県' in v:
                output_shikoku[idx]=1
            elif '福岡県' in v:
                output_kyushu[idx]=1
            elif '佐賀県' in v:
                output_kyushu[idx]=1
            elif '長崎県' in v:
                output_kyushu[idx]=1
            elif '熊本県' in v:
                output_kyushu[idx]=1
            elif '大分県' in v:
                output_kyushu[idx]=1
            elif '宮崎県' in v:
                output_kyushu[idx]=1
            elif '鹿児島県' in v:
                output_kyushu[idx]=1
            elif '沖縄県' in v:
                output_okinawa[idx]=1
            elif '海外' in v:
                output_oversea[idx]=1
        
        train_df['北海道']=output_hokkaido
        train_df['東北']=output_tohoku
        train_df['関東']=output_kanto
        train_df['中部']=output_chubu
        train_df['近畿']=output_kinki
        train_df['中国']=output_chugoku
        train_df['四国']=output_shikoku
        train_df['九州']=output_kyushu
        train_df['沖縄県']=output_okinawa
        train_df['海外']=output_oversea
        return train_df

    def gen_language(self, train_df):

        language_list=train_df['language_skillset'] 

        ## 次元をなるべく丸める
        output_fe = np.zeros(len(language_list))
        output_be = np.zeros(len(language_list))
        output_serversides = np.zeros(len(language_list))
        output_scala = np.zeros(len(language_list))
        output_ai = np.zeros(len(language_list))
        output_buildsin = np.zeros(len(language_list))
        output_androids = np.zeros(len(language_list))
        output_ios = np.zeros(len(language_list))
        output_others = np.zeros(len(language_list))
        output_r = np.zeros(len(language_list))
        
        for ind,val in enumerate(language_list):
            print(str(val))
            if 'JavaScript'in str(val):
                output_be[ind]=1
            if 'Java'in str(val):
                output_be[ind]=1
            if 'PHP'in str(val):
                output_be[ind]=1
            if 'Ruby'in str(val):
                output_be[ind]=1
            if 'HTML'in str(val):
                output_fe[ind]=1
            if 'CSS'in str(val):
                output_fe[ind]=1
            if 'Python'in str(val):
                output_ai[ind]=1
            if 'Objective-C'in str(val):
                output_buildsin[ind]=1
            if 'C++'in str(val):
                output_buildsin[ind]=1
            if 'Kotlin'in str(val):
                output_androids[ind]=1
            if 'C＃'in str(val):
                output_buildsin[ind]=1
            if 'CoffeeScript'in str(val):
                output_be[ind]=1
            if 'PL'in str(val):
                output_others[ind]=1
            if 'Scala'in str(val):
                output_scala[ind]=1
            if 'Swift'in str(val):
                output_ios[ind]=1
            if 'Perl'in str(val):
                output_be[ind]=1
            if 'TypeScript'in str(val):
                output_fe[ind]=1
            if 'Go'in str(val):
                output_be[ind]=1
            if 'Kotlin'in str(val):
                output_androids[ind]=1
            if 'Bash'in str(val):
                output_serversides[ind]=1
            if 'R言語'in str(val):
                output_r[ind]=1
            if 'Clojure'in str(val):
                output_others[ind]=1
            if 'PL'in str(val):
                output_others[ind]=1
            if 'Node.js'in str(val):
                output_be[ind]=1
            if 'Vue.js'in str(val):
                output_fe[ind]=1
            if 'SQL'in str(val):
                output_serversides[ind]=1
                
        train_df['FrontEnd']=output_fe
        train_df['BackEnd']=output_be
        train_df['ServerSide']=output_serversides
        train_df['AI']=output_ai
        train_df['Build-in']=output_buildsin
        train_df['android']=output_androids
        train_df['scala']=output_androids
        train_df['R言語']=output_r
        train_df['ios']=output_ios
        train_df['others']=output_others
        return train_df

    def exclude_clm(self, train_df, exclude_cols):
        feature_cols = []
        for col in train_df.columns:
            if col not in exclude_cols:
                feature_cols.append(col)

        return feature_cols

    def gen_test_position(self, test_df):

        location_list = test_df['location']
        output_hokkaido = np.zeros(len(location_list))
        output_tohoku = np.zeros(len(location_list))
        output_kanto = np.zeros(len(location_list))
        output_chubu = np.zeros(len(location_list))
        output_kinki = np.zeros(len(location_list))
        output_chugoku = np.zeros(len(location_list))
        output_shikoku = np.zeros(len(location_list))
        output_kyushu = np.zeros(len(location_list))
        output_okinawa = np.zeros(len(location_list))
        output_oversea = np.zeros(len(location_list))
        
        for ind,val in enumerate(location_list):
            if '北海道' in val:
                output_hokkaido[ind]=1
            elif '青森県' in val:
                output_tohoku[ind]=1
            elif '岩手県' in val:
                output_tohoku[ind]=1
            elif '宮城県' in val:
                output_tohoku[ind]=1
            elif '秋田県' in val:
                output_tohoku[ind]=1
            elif '山形県' in val:
                output_tohoku[ind]=1
            elif '福島県' in val:
                output_tohoku[ind]=1
            elif '茨城県' in val:
                output_kanto[ind]=1
            elif '栃木県' in val:
                output_kanto[ind]=1
            elif '群馬県' in val:
                output_kanto[ind]=1
            elif '埼玉県' in val:
                output_kanto[ind]=1
            elif '千葉県' in val:
                output_kanto[ind]=1
            elif '東京都' in val:
                output_kanto[ind]=1
            elif '神奈川県' in val:
                output_kanto[ind]=1
            elif '新潟県' in val:
                output_chubu[ind]=1
            elif '富山県' in val:
                output_chubu[ind]=1
            elif '石川県' in val:
                output_chubu[ind]=1
            elif '福井県' in val:
                output_chubu[ind]=1
            elif '山梨県' in val:
                output_chubu[ind]=1
            elif '長野県' in val:
                output_chubu[ind]=1
            elif '岐阜県' in val:
                output_chubu[ind]=1
            elif '静岡県' in val:
                output_chubu[ind]=1
            elif '愛知県' in val:
                output_chubu[ind]=1
            elif '三重県' in val:
                output_kinki[ind]=1
            elif '滋賀県' in val:
                output_kinki[ind]=1
            elif '京都府' in val:
                output_kinki[ind]=1
            elif '大阪府' in val:
                output_kinki[ind]=1
            elif '兵庫県' in val:
                output_kinki[ind]=1
            elif '奈良県' in val:
                output_kinki[ind]=1
            elif '和歌山県' in val:
                output_kinki[ind]=1
            elif '鳥取県' in val:
                output_chugoku[ind]=1
            elif '島根県' in val:
                output_chugoku[ind]=1
            elif '岡山県' in val:
                output_chugoku[ind]=1
            elif '広島県' in val:
                output_chugoku[ind]=1
            elif '山口県' in val:
                output_chugoku[ind]=1
            elif '徳島県' in val:
                output_shikoku[ind]=1
            elif '香川県' in val:
                output_shikoku[ind]=1
            elif '愛媛県' in val:
                output_shikoku[ind]=1
            elif '高知県' in val:
                output_shikoku[ind]=1
            elif '福岡県' in val:
                output_kyushu[ind]=1
            elif '佐賀県' in val:
                output_kyushu[ind]=1
            elif '長崎県' in val:
                output_kyushu[ind]=1
            elif '熊本県' in val:
                output_kyushu[ind]=1
            elif '大分県' in val:
                output_kyushu[ind]=1
            elif '宮崎県' in val:
                output_kyushu[ind]=1
            elif '鹿児島県' in val:
                output_kyushu[ind]=1
            elif '沖縄県' in val:
                output_okinawa[ind]=1
            elif '海外' in val:
                output_oversea[ind]=1
        
        test_df['北海道']=output_hokkaido
        test_df['東北']=output_tohoku
        test_df['関東']=output_kanto
        test_df['中部']=output_chubu
        test_df['近畿']=output_kinki
        test_df['中国']=output_chugoku
        test_df['四国']=output_shikoku
        test_df['九州']=output_kyushu
        test_df['沖縄県']=output_okinawa
        test_df['海外']=output_oversea
        return test_df

    def gen_test_position(self, test_df):
        
        position_list=test_df['position_tokenized'] 
        output_coder = np.zeros(len(position_list))
        output_engineer = np.zeros(len(position_list))
        output_manager = np.zeros(len(position_list))
        output_programer = np.zeros(len(position_list))
        output_productowner = np.zeros(len(position_list))
        output_cto = np.zeros(len(position_list))
        output_scrummaster = np.zeros(len(position_list))
        output_datascientist = np.zeros(len(position_list))
        output_ai = np.zeros(len(position_list))
        output_architect = np.zeros(len(position_list))
        output_infra = np.zeros(len(position_list))
        output_sp = np.zeros(len(position_list))
        
        for ind,val in enumerate(position_list):
            if 'エンジニア' in str(val):
                output_engineer[ind]=1
            if 'SE' in str(val):
                output_engineer[ind]=1
            if 'PM' in str(val):
                output_manager[ind]=1
            if 'PL' in str(val):
                output_manager[ind]=1
            if 'リーダ' in str(val):
                output_manager[ind]=1
            if 'マネジャ' in str(val):
                output_manager[ind]=1
            if 'マネージャ' in str(val):
                output_manager[ind]=1
            if 'PG' in str(val):
                output_programer[ind]=1
            if 'プログラマ' in str(val):
                output_programer[ind]=1
            if 'コーダ' in str(val):
                output_coder[ind]=1
            if 'プロダクトオーナ' in str(val):
                output_productowner[ind]=1
            if 'CTO' in str(val):
                output_cto[ind]=1
            if 'スクラム' in str(val):
                output_scrummaster[ind]=1
            if 'データ サイエンティスト' in str(val):
                output_datascientist[ind]=1
            if 'AI' in str(val):
                output_ai[ind]=1
            if 'リード' in str(val):
                output_architect[ind]=1
            if 'アーキテクト' in str(val):
                output_architect[ind]=1
            if 'インフラ' in str(val):
                output_infra[ind]=1
            if 'Android' in str(val):
                output_sp[ind]=1
            if 'iOS' in str(val):
                output_sp[ind]=1
            if 'ディレクター' in str(val):
                output_manager[ind]=1
            if '開発' in str(val):
                output_sp[ind]=1
            if 'engineering' in str(val):
                output_engineer[ind]=1
            if 'データ' in str(val):
                output_datascientist[ind]=1
            if 'Unity' in str(val):
                output_engineer[ind]=1
            if 'データ' in str(val):
                output_datascientist[ind]=1
            if '責任者' in str(val):
                output_manager[ind]=1
            if '組み込み' in str(val):
                output_engineer[ind]=1
            if '責任者' in str(val):
                output_manager[ind]=1
            if '技師' in str(val):
                output_engineer[ind]=1
            if '構築' in str(val):
                output_engineer[ind]=1
            if '講師' in str(val):
                output_engineer[ind]=1
            if 'Engineering' in str(val):
                output_engineer[ind]=1
            if '3DCG' in str(val):
                output_engineer[ind]=1
            if 'プロダクトオーナー' in str(val):
                output_scrummaster[ind]=1
                
        test_df['エンジニア']=output_engineer
        test_df['マネージャ']=output_manager
        test_df['コーダー']=output_coder
        test_df['プログラマー']=output_programer
        test_df['プロダクトオーナー']=output_productowner
        test_df['AI']=output_ai
        test_df['CTO']=output_cto
        test_df['スクラムマスタ']=output_scrummaster
        test_df['データサイエンティスト']=output_datascientist
        test_df['アーキテクト']=output_architect
        test_df['インフラ']=output_infra
        test_df['SP']=output_sp
        return test_df

    def gen_test_language(self, test_df):

        language_list=test_df['language_skillset'] 
        
        ## 次元削減
        output_fe = np.zeros(len(language_list))
        output_be = np.zeros(len(language_list))
        output_serversides = np.zeros(len(language_list))
        output_scala = np.zeros(len(language_list))
        output_ai = np.zeros(len(language_list))
        output_buildsin = np.zeros(len(language_list))
        output_androids = np.zeros(len(language_list))
        output_ios = np.zeros(len(language_list))
        output_others = np.zeros(len(language_list))
        output_r = np.zeros(len(language_list))
        
        for ind,val in enumerate(language_list):
            print(str(val))
            if 'JavaScript'in str(val):
                output_be[ind]=1
            if 'Java'in str(val):
                output_be[ind]=1
            if 'PHP'in str(val):
                output_be[ind]=1
            if 'Ruby'in str(val):
                output_be[ind]=1
            if 'HTML'in str(val):
                output_fe[ind]=1
            if 'CSS'in str(val):
                output_fe[ind]=1
            if 'Python'in str(val):
                output_ai[ind]=1
            if 'Objective-C'in str(val):
                output_buildsin[ind]=1
            if 'C++'in str(val):
                output_buildsin[ind]=1
            if 'Kotlin'in str(val):
                output_androids[ind]=1
            if 'C＃'in str(val):
                output_buildsin[ind]=1
            if 'CoffeeScript'in str(val):
                output_be[ind]=1
            if 'PL'in str(val):
                output_others[ind]=1
            if 'Scala'in str(val):
                output_scala[ind]=1
            if 'Swift'in str(val):
                output_ios[ind]=1
            if 'Perl'in str(val):
                output_be[ind]=1
            if 'TypeScript'in str(val):
                output_fe[ind]=1
            if 'Go'in str(val):
                output_be[ind]=1
            if 'Kotlin'in str(val):
                output_androids[ind]=1
            if 'Bash'in str(val):
                output_serversides[ind]=1
            if 'R言語'in str(val):
                output_r[ind]=1
            if 'Clojure'in str(val):
                output_others[ind]=1
            if 'PL'in str(val):
                output_others[ind]=1
            if 'Node.js'in str(val):
                output_be[ind]=1
            if 'Vue.js'in str(val):
                output_fe[ind]=1
            if 'SQL'in str(val):
                output_serversides[ind]=1
                
        test_df['FrontEnd']=output_fe
        test_df['BackEnd']=output_be
        test_df['ServerSide']=output_serversides
        test_df['AI']=output_ai
        test_df['Build-in']=output_buildsin
        test_df['android']=output_androids
        test_df['scala']=output_androids
        test_df['R言語']=output_r
        test_df['ios']=output_ios
        test_df['others']=output_others


if __name__ == '__main__':
    gdf=GDF()
