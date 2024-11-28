import json
import random
class QuoteReader:
    def __init__(self, quotes_filename, position_filename):
        # 读取情话文件
        with open(quotes_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.quotes = data['quotes']
        
        # 读取保存的当前索引
        with open(position_filename, 'r', encoding='utf-8') as f:
            position_data = json.load(f)
            self.index = position_data['current_index']

    def get_next_quote(self):
        # 如果还有情话可以读取
        if self.index < len(self.quotes):
            quote = self.quotes[self.index]
            self.index += 1
            
            # 更新索引到 position.json
            self._save_position()
            return quote
        else:
            return None  # 已经读完所有情话

    def _save_position(self):
        # 更新 position.json 文件
        with open('position.json', 'w', encoding='utf-8') as f:
            json.dump({'current_index': self.index}, f, ensure_ascii=False, indent=4)

def get_words():
    quote_reader = QuoteReader("./lovers_word.json" , "./position.json")  # 替换为你的 JSON 文件路径
    return quote_reader.get_next_quote()

def I_Want_To_Say():
    quote_reader = QuoteReader("./tell_you.json" , "./position.json")  # 替换为你的 JSON 文件路径
    return quote_reader.get_next_quote()

# print(f"句子：{get_words()}")
# print(f"想对你说的话：{I_Want_To_Say()}")

print(','.join(["2398680927@qq.com","maxiansen2007@gmail.com"]))