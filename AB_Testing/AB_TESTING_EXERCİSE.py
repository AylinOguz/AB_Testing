#####################################################
# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################

#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.




#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################



import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from pygments.lexers.macaulay2 import M2KEYWORDS
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.

df_control = pd.read_excel("datasets/ab_testing.xlsx",  sheet_name="Control Group")
df_test = pd.read_excel("datasets/ab_testing.xlsx",  sheet_name="Test Group")

df_test.columns = ["Impression_test", "Click_test", "Purchase_test","Earning_test"]
df_control.columns =  ["Impression_control", "Click_control", "Purchase_control","Earning_control"]

# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

df_control.describe().T
df_test.describe().T



# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.


df = pd.concat([df_control,df_test], axis=1)



#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.

# H0 : M1 = M2 ( maximumbidding"  teklif verme türüne  "average bidding"’i teklif verme türü arasında fark yoktur.)
# H1 : M1 != M2 ( .... vardır)


# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz

df["Purchase_control"].mean()
# 550.8940587702316
df["Purchase_test"].mean()
#  582.1060966484677


#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################


# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.


# Varsayım Kontrolleri

# Normallik varsayımı
# Varyans Homejenliği


# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz


# H0 : Normal dağılım varsayımı sağlanmaktadır.
# H1 : sağlanmamaktadır.

test_stat, pvalue = shapiro(df["Purchase_control"])
print("test_stat = %.4f, p-value = %.4f" %(test_stat,pvalue))

# test_stat = 0.9773, p-value = 0.5891


# p_value değeri 0.05 den büyük olduğu için H0 reddedilemez yani normallik dağılımı sağlanmaktadır


test_stat, pvalue = shapiro(df["Purchase_test"])
print("test_stat = %.4f, p-value = % .4f" %(test_stat,pvalue))

# test_stat = 0.9589, p-value =  0.1541

#  p_value değeri 0.05 den büyük olduğu için H0 reddedilemez yani normallik dağılımı sağlanmaktadır


test_stat, pvalue = levene(df["Purchase_control"],df["Purchase_test"])
print("test_stat = %.4f, p-value = % .4f" %(test_stat,pvalue))

# test_stat = 2.6393, p-value =  0.1083

# H0 reddedilemez yani varyans homojenliği sağlanmaktadır.


# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

#


test_stat,pvalue = ttest_ind(df["Purchase_control"],df["Purchase_test"], equal_var=True)
print("test_stat = %.4f, p-value = %.4f" % (test_stat,pvalue))

# test_stat = -0.9416, p-value = 0.3493



# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.


# p-value değeri 0.05 den büyük olduğu için H0 reddedilemez yani kontrol ve test grubu arasında satın alma
# ortalamaları açısından istatiksel bir fark yoktur.



##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

# test ve control gruplarının dağılımlarının homojen olmasından kaynaklı t_test kullandık ek olarak varyans
# homojenliği de sağlandığı için equal_var parametresine True değerini verdik



# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

# İstatiksel açıdan 2 teklif türünde satın alma ortalamaları açısından fark yoktur.Bu nedenle maliyeti daha
# az olan yöntemi tercih etmenizi öneririm







































# “İstatistiksel olarak fark bulunmayan bu iki strateji arasında seçim yaparken sadece performansa değil,
# maliyet ve yatırım getirisi (ROI) gibi faktörlere de dikkat edilmeli. Eğer Average Bidding daha az
# maliyetliyse ve aynı sonucu veriyorsa, bu strateji daha verimli olur. Ancak farklı kullanıcı segmentleri
# ya da kampanya türleri için özel stratejiler de değerlendirilebilir.”
