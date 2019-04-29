#Creating data in different languages

from faker import Faker
print('''Enter the laguage number in which you want to generate data:
0-->ar_EG - Arabic (Egypt)
1-->ar_PS - Arabic (Palestine)
2-->ar_SA - Arabic (Saudi Arabia)
3-->bg_BG - Bulgarian
4-->cs_CZ - Czech
5-->de_DE - German
6-->dk_DK - Danish
7-->el_GR - Greek
8-->en_AU - English (Australia)
9-->en_CA - English (Canada)
10-->en_GB - English (Great Britain)
11-->en_US - English (United States)
12-->es_ES - Spanish (Spain)
13-->es_MX - Spanish (Mexico)
14-->et_EE - Estonian
15-->fa_IR - Persian (Iran)
16-->fi_FI - Finnish
17-->fr_FR - French
18-->hi_IN - Hindi
19-->hr_HR - Croatian
20-->hu_HU - Hungarian
21-->it_IT - Italian
22-->ja_JP - Japanese
23-->ko_KR - Korean
24-->lt_LT - Lithuanian
25-->lv_LV - Latvian
26-->ne_NP - Nepali
27-->nl_NL - Dutch (Netherlands)
28-->no_NO - Norwegian
29-->pl_PL - Polish
30-->pt_BR - Portuguese (Brazil)
31-->pt_PT - Portuguese (Portugal)
32-->ro_RO - Romanian
33-->ru_RU - Russian
34-->sl_SI - Slovene
35-->sv_SE - Swedish
36-->tr_TR - Turkish
37-->uk_UA - Ukrainian
38-->zh_CN - Chinese (China)
39-->zh_TW - Chinese (Taiwan)
40-->ka_GE - Georgian (Georgia)''')


lang_list=['ar_EG','ar_PS','ar_SA','bg_BG','cs_CZ','de_DE','dk_DK','el_GR','en_AU','en_CA','en_GB','en_US','es_ES','es_MX','et_EE','fa_IR','fi_FI','fr_FR','hi_IN',
           'hr_HR','hu_HU','it_IT','ja_JP','ko_KR','lt_LT','lv_LV','ne_NP','nl_NL','no_NO','pl_PL','pt_BR','pt_PT','ro_RO','ru_RU','sl_SI',
           'sv_SE','tr_TR','uk_UA','zh_CN','zh_TW','ka_GE']
language_number=input()
#converting the input type to integer
language_number=int(language_number,10)
fake=Faker(lang_list[language_number])

for i in range(0,10):
    print('1.Name--->', fake.name(), '2.Country-->', fake.country())

