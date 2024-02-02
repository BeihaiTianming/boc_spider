from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time

# 货币代号对照
currency_map = {
    'USD': '美元',
    'EUR': '欧元',
    'JPY': '日元',
    'HKD': '港币',
    'GBP': '英镑',
    'KRW': '韩元',
    'SUR': '卢布',
    'THB': '泰国铢',
    'MOP': '澳门元',
    'NLG': '荷兰盾',
    'FRF': '法国法郎',   
    'CAD': '加拿大元',
    'SGD': '新加坡元',
    'CHF': '瑞士法郎',
    'MYR': '马来西亚林吉特',
    'NZD': '新西兰元',
    'AUD': '澳大利亚元',
    'PHP': '菲律宾比索',
    'IDR': '印度尼西亚卢比',
    'DEM': '德国马克',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'TWD': '新台币',
    'ESP': '西班牙比塞塔',
    'ITL': '意大利里拉',
    'BEF': '比利时法郎',
    'FIM': '芬兰马克',
    'INR': '印度卢比',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉',
}

try:
    # 获取命令行参数
    date = sys.argv[1]
    currency_code = sys.argv[2]
    currency_name = currency_map.get(currency_code.upper())

    # 使用selenium打开中国银行外汇牌价网站
    driver = webdriver.Chrome()
    driver.get('https://www.boc.cn/sourcedb/whpj/')

    # 定位日期输入框，并输入指定的日期
    date_input1 = driver.find_element(by=By.NAME, value='erectDate')
    date_input1.clear()
    date_input1.send_keys(date)

    data_input2 = driver.find_element(by=By.NAME, value='nothing')
    data_input2.clear()
    data_input2.send_keys(date)

    # 定位货币选择下拉框，并选择美元
    currency_select = Select(driver.find_element(by=By.NAME, value='pjname'))
    currency_select.select_by_visible_text(currency_name)

    # 点击查询按钮
    search_buttons = driver.find_elements(by=By.CLASS_NAME, value='search_btn')
    search_buttons[1].click()

    # 等待新页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))

    # 找到所有的tr元素
    rows = driver.find_elements(By.TAG_NAME, 'tr')

    with open('result.txt', 'w') as f:
        # 遍历tr元素
        for row in rows:
            # 找到当前行的所有td元素
            cols = row.find_elements(By.TAG_NAME, 'td')
            # 打印第四列的文本并将其保存在result.txt文件中
            if len(cols) > 3:
                f.write(cols[3].text)
                f.write('\n')
                print(cols[3].text)

    time.sleep(30)
    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")