
import time

def check_strategy(stock_code, name, support, resistance_list, price):
    message = f"【{name}({stock_code})】現價：{price}"
    if price <= support:
        message += f" ▶️ 跌破支撐({support})，可留意反彈"
    elif any(price >= res for res in resistance_list):
        hit = [res for res in resistance_list if price >= res][0]
        message += f" ▶️ 突破壓力({hit})，可觀察追價機會"
    else:
        return None
    return message

# 股票資料
stocks = [
    {"code": "3583", "name": "辛耘", "support": 335, "resistance": [355.5]},
    {"code": "3167", "name": "大量", "support": 167, "resistance": [174.5, 178]},
    {"code": "6215", "name": "和椿", "support": 108.5, "resistance": [118.5]}
]

def get_mock_price(stock_code):
    # 假設函數，實際可接 API
    mock_prices = {
        "3583": 340.7,
        "3167": 174.32,
        "6215": 115.67
    }
    return mock_prices.get(stock_code, 0)

# 執行策略
for stock in stocks:
    price = get_mock_price(stock["code"])
    result = check_strategy(stock["code"], stock["name"], stock["support"], stock["resistance"], price)
    if result:
        print(result)

# 防止 Render 自動關閉
while True:
    time.sleep(60)
