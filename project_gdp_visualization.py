#coding:gbk
"""
���ߣ�����
����Ŀ�꣺��scv�ļ��еĸ���gdp���ݿ��ӻ������ݵķ���
"""
import csv
import math
import pygal
import pygal_maps_world  #������Ҫʹ�õĿ�


def read_csv_as_nested_dict(filename, keyfield, separator, quote): #��ȡԭʼcsv�ļ������ݣ���ʽΪǶ���ֵ�
    """
    �������:
      filename:csv�ļ���
      keyfield:����
      separator:�ָ���
      quote:���÷�
    ���:
      ��ȡcsv�ļ����ݣ�����Ƕ���ֵ��ʽ����������ֵ�ļ���Ӧ����keyfiled���ڲ��ֵ��Ӧÿ���ڸ�������Ӧ�ľ���ֵ
    """
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result

pygal_countries = pygal.maps.world.COUNTRIES #��ȡpygal.maps.world�й��Ҵ�����Ϣ��Ϊ�ֵ��ʽ�������м�Ϊpygal�и������룬ֵΪ��Ӧ�ľ������(���齫����ʾ����Ļ���˽�����ʽ���������ݣ�

def reconcile_countries_by_name(plot_countries, gdp_countries): #������������GDP���ݵĻ�ͼ����Ҵ����ֵ䣬�Լ�û������GDP���ݵĹ��Ҵ��뼯��
    """
    �������:
    plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
    gdp_countries:���и������ݣ�Ƕ���ֵ��ʽ�������ⲿ�ֵ�ļ�Ϊ���й��Ҵ��룬ֵΪ�ù��������ļ��е������ݣ��ֵ��ʽ)
    �����
    ����Ԫ���ʽ������һ���ֵ��һ�����ϡ������ֵ�����Ϊ��������GDP���ݵĻ�ͼ�������Ϣ����Ϊ��ͼ������Ҵ��룬ֵΪ��Ӧ�ľ������),
    ��������Ϊ��������GDP���ݵĻ�ͼ����Ҵ���
    """
    set_1=set()
    dict_1={}
    for k,v in gdp_countries.items():
        lst_1=set(v.values())
        if len(lst_1)==5:
            set_1.add(from_value_to_key(k))
    for k,v in plot_countries.items():
        if v not in set_1:
            dict_1[k]=v
    tuple_1=(dict_1,set_1)
    return tuple_1



def from_key_to_value(key):
    for key_1,values in pygal_countries.items():
        if key_1 == key:
            return values
            
def from_value_to_key(value):     
    for key,values in pygal_countries.items():
        if values == value:
            return key


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    �������:
    gdpinfo:
    plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
    year: �������ֵ
    �����
    �������һ���ֵ�Ͷ������ϵ�Ԫ�����ݡ������ֵ�����Ϊ��ͼ������Ҵ��뼰��Ӧ����ĳ�������GDP��ֵ����Ϊ��ͼ���и����Ҵ��룬ֵΪ�ھ�����ݣ���year����ȷ��������Ӧ������GDP����ֵ��Ϊ
    ������ʾ���㣬GDP�����ת��Ϊ��10Ϊ�����Ķ�����ʽ����GDPԭʼֵΪ2500����ӦΪlog2500��ps:����math.log()���)
    2������һ��Ϊ������GDP��������ȫû�м�¼�Ļ�ͼ����Ҵ��룬��һ������Ϊֻ��û��ĳ�ض��꣨��year����ȷ��������GDP���ݵĻ�ͼ����Ҵ���
   """
    set_1=set()
    dict_1={}
    for key,value in gdpinfo.items():
        if from_value_to_key(key) in plot_countries[0]:        #�����жϡ������ݵĹ�����Ϣ���Ĺ�����ļ���������һ���ж�
            if value[year] != "":
                num_1 = float(value[year])
                dict_1[from_value_to_key(key)] = math.log(num_1)
            else:
                set_1.add(from_value_to_key(key))
    tuple_1=(dict_1,set_1,plot_countries[1])
    return tuple_1
    
def render_world_map(gdpinfo, plot_countries, year, map_file): #������ĳ�����������GDP����(����ȱ��GDP�����Լ�ֻ���ڸ���ȱ��GDP���ݵĹ���)�Ե�ͼ��ʽ���ӻ�
    """
    Inputs:
      gdpinfo:gdp��Ϣ�ֵ�
      plot_countires:��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
      year:����������ݣ����ַ�����ʽ������"1970"
      map_file:�����ͼƬ�ļ���
    Ŀ�꣺��ָ��ĳ����������GDP�����������ͼ����ʾ������������Ϊ����ĵ�ͼƬ�ļ�
    ��ʾ�����������ӻ���Ҫ����pygal.maps.world.World()����
    """
    
    list_1=list(gdpinfo[1])               #������˳��������Ϊ�б���б����������ֵ��в���ֵ��1��
    list_2=list(gdpinfo[2])
    dict_1={}
    dict_2={}
    for values_1 in list_1:
        dict_1[values_1] = "1"
    for values_2 in list_2:
        if values_2 != None:                                 #ɾ���ڶ��������еĿ�ֵ
            dict_2[values_2] = "1"
    worldmap_chart=pygal.maps.world.World()
    worldmap_chart.title = 'ȫ��GDP�ֲ�ͼ'                   #���ݿ��ӻ����
    worldmap_chart.add('%s'%year,gdpinfo[0])
    worldmap_chart.add('missing from world bank',dict_1)
    worldmap_chart.add('no data at this year',dict_2)
    worldmap_chart.render_to_file(map_file)

# def test_render_world_map(year):  #���Ժ���
    # """
    # �Ը����ܺ������в���
    # """
    # gdpinfo = {
        # "gdpfile": "isp_gdp.csv",
        # "separator": ",",
        # "quote": '"',
        # "min_year": 1960,
        # "max_year": 2015,
        # "country_name": "Country Name",
        # "country_code": "Country Code"
    # } #���������ֵ�


    # pygal_countries = pygal.maps.world.COUNTRIES   # ��û�ͼ��pygal���Ҵ����ֵ�

    # # ����ʱ����1970��Ϊ�����Ժ����������ԣ������н�����ṩ��svg���жԱȣ�������ݿɽ��ļ���������
    # render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_1970.svg")








#������Ժ�����
print("��ӭʹ������GDP���ݿ��ӻ���ѯ")
print("----------------------")
year=input("���������ѯ�ľ������:")
result1=read_csv_as_nested_dict("isp_gdp.csv","Country Name",",",'"')   #���ú���
result2=reconcile_countries_by_name(pygal_countries,result1)         #���õڶ�������
beta=build_map_dict_by_name(result1,result2,year)                #���õ���������
render_world_map(beta,pygal_countries,year,"isp_gdp_world_name_%s.svg"%year)
