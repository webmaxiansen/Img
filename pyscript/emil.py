import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import random

def send_email(subject, content, sender_email, sender_password, receiver_email):
    """
    使用QQ邮箱发送邮件
    :param subject: 邮件主题
    :param content: 邮件内容
    :param sender_email: 发件人邮箱（QQ邮箱地址）
    :param sender_password: 发件人邮箱的应用专用密码
    :param receiver_email: 收件人邮箱
    """
    try:
        # QQ邮箱的 SMTP 服务器地址和端口号
        smtp_server = "smtp.qq.com"
        smtp_port = 587  # 使用 STARTTLS
        message = MIMEMultipart()
        
        # 设置发件人和收件人
        message['From'] = sender_email  # 直接使用发件人邮箱
        message['To'] = receiver_email  # 直接使用收件人邮箱
        message['Subject'] = Header(subject, 'utf-8')  # 主题使用Header()进行编码

        # 添加邮件正文
        message.attach(MIMEText(content, 'html', 'utf-8'))

        # 使用 STARTTLS 连接 QQ 邮箱服务器并发送邮件
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 启用 TLS 加密
            server.login(sender_email, sender_password)  # 登录
            server.sendmail(sender_email, receiver_email, message.as_string())  # 发送邮件

            print("邮件发送成功！")

            # 使用 close() 而不是 quit()
            server.close()  # 如果quit()报错，尝试使用close()

    except Exception as e:
        print("邮件发送失败，错误信息：", e)

# 示例调用
if __name__ == "__main__":
    sender_email = "2398680927@qq.com"  # 替换为你的QQ邮箱
    sender_password = "aqudpcegsonvecbj"  # 替换为你的应用专用密码
    # receiver_email = "maxiansen2007@gmail.com"  # 替换为接收者邮箱 
    # receiver_email = "zxy_20001215@qq.com" 
    receiver_email = "2398680927@qq.com" 

    subject = "My Crush"
     # 添加HTML邮件正文
    # 动态内容
    name = '迎迎'
    background_image_url = 'https://maxiansen.top/Img/MyGirlFriend/1.jpg'
    content = '''
    tip-- 还记得你跟我说想要天上的星星嘛  虽然我无法做到  但给你另一种特殊的方式展现给你 手指连续点击屏幕会有声音
    '''
    quote = '你是我生命中的光，点亮了每一个平凡的日子。'
    sender = '凡凡——老公'
    link = 'https://maxiansen.top/Img/blog/public/startsky.html'
    themes = [{
        "header_color": "#ffd1dc",  # 柔和粉色
        "footer_color": "#ffe6e6",  # 淡粉色
        "button_color": "#ff80ab",  # 明亮的粉色
        "hover_color": "#ff5c8d",   # 略深的粉色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#555",  # 深灰色
        "text_footer_color": "#777", # 浅灰色
    }, {
        "header_color": "#d50000",  # 热情红色
        "footer_color": "#ff8a80",  # 粉红色
        "button_color": "#ff1744",  # 鲜艳的红色
        "hover_color": "#e55d5d",   # 略深的红色
        "text_theme_color": "#333", # 白色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#f8bbd0",  # 更浅的粉色（增加对比）
        "text_footer_color": "#f8bbd0", # 相同的浅粉色
    }, {
        "header_color": "#d1c4e9",  # 梦幻紫色
        "footer_color": "#b39ddb",  # 紫色系的渐变色
        "button_color": "#9c27b0",  # 紫色按钮
        "hover_color": "#7b1fa2",   # 深紫色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#b39ddb",  # 紫色引用
        "text_footer_color": "#b39ddb", # 页脚文字与引用一致
    }, {
        "header_color": "#ffd700",  # 金色
        "footer_color": "#ffecb3",  # 淡金色
        "button_color": "#ffc107",  # 明亮的金色
        "hover_color": "#e65100",   # 深金色
        "text_theme_color": "#4e342e", # 深咖啡色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#6d4c41",  # 棕色引用（调整为更深色）
        "text_footer_color": "#6d4c41", # 深棕色
    }, {
        "header_color": "#a5d6a7",  # 薄荷绿
        "footer_color": "#c8e6c9",  # 更淡的绿色
        "button_color": "#66bb6a",  # 活力绿
        "hover_color": "#388e3c",   # 稍深的绿
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#388e3c",  # 深绿引用
        "text_footer_color": "#777", # 浅灰色
    }, {
        "header_color": "#00bcd4",  # 天空蓝
        "footer_color": "#b2ebf2",  # 更淡的蓝色
        "button_color": "#00acc1",  # 深蓝绿色
        "hover_color": "#00838f",   # 深蓝色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#0288d1",  # 蓝色引用
        "text_footer_color": "#777", # 浅灰色
    }, {
        "header_color": "#ff5722",  # 辣椒橙色
        "footer_color": "#ffab91",  # 粉橙色
        "button_color": "#e64a19",  # 深橙色按钮
        "hover_color": "#d32f2f",   # 略深的红色
        "text_theme_color": "#333", # 白色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#f57c00",  # 橙色引用
        "text_footer_color": "#f57c00", # 更深的橙色
    }, {
        "header_color": "#8bc34a",  # 草绿色
        "footer_color": "#c5e1a5",  # 淡绿色
        "button_color": "#4caf50",  # 清新的绿色
        "hover_color": "#388e3c",   # 深绿色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#2e7d32",  # 深绿引用
        "text_footer_color": "#777", # 浅灰色
    }, {
        "header_color": "#9e9e9e",  # 灰色
        "footer_color": "#eeeeee",  # 浅灰色
        "button_color": "#607d8b",  # 深灰蓝色
        "hover_color": "#455a64",   # 深蓝灰色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#78909c",  # 淡灰蓝色引用
        "text_footer_color": "#777", # 浅灰色
    }, {
        "header_color": "#ff9800",  # 橙黄色
        "footer_color": "#ffe0b2",  # 淡黄色
        "button_color": "#ff5722",  # 明亮橙色
        "hover_color": "#d32f2f",   # 红色
        "text_theme_color": "#333", # 深灰色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#f57c00",  # 橙色引用
        "text_footer_color": "#f57c00", # 深橙色
    }, {
        "header_color": "#9c27b0",  # 紫红色
        "footer_color": "#f3e5f5",  # 浅紫色
        "button_color": "#8e24aa",  # 中紫红色
        "hover_color": "#6a1b9a",   # 深紫色
        "text_theme_color": "#333", # 白色
        "text_header_color": "#fff", # 白色
        "text_quote_color": "#ab47bc",  # 紫色引用
        "text_footer_color": "#ab47bc", # 紫色页脚
    },{
        "header_color": "#2a3d66",  # 深蓝色，象征星空
        "footer_color": "#4a6d8c",  # 深蓝灰色，增添深邃感
        "button_color": "#ffeb3b",  # 明亮的黄色，像星星的光辉
        "hover_color": "#fbc02d",   # 略深的黄色，使按钮更加生动
        "text_theme_color": "#333", # 白色，代表星星与光辉，确保文字清晰可见
        "text_header_color": "#ffffff", # 白色，保持一致的清晰度
        "text_quote_color": "#d1c4e9",  # 浅紫色，温柔的星空氛围
        "text_footer_color": "#b0bec5", # 浅灰蓝色，柔和且不抢眼
    }]

    # 用户是否选择特定主题
    choose_specific_theme = True  # 设置为True表示选择特定主题，False表示随机选择
    
    # 如果用户选择特定主题，可以通过下标指定主题，例如：主题1
    specific_theme_index = 11  # 自主选择主题
    
    # 随机选择或指定主题
    if choose_specific_theme:
        selected_theme = themes[specific_theme_index]
    else:
        selected_theme = random.choice(themes)
    
# 处理内容中的换行符
content_with_line_breaks = '<br>'.join([f'&nbsp;&nbsp;{line.strip()}' for line in content.splitlines()])  # 将 \n 替换为 <br>

# 使用 f-string 构建 HTML 模板
html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
            <title>To My Dearest {name}</title>
            <style>
                body {{
                    font-family: 'Courier New', Courier, monospace;
                    margin: 0;
                    padding: 0;
                    color: {selected_theme["text_theme_color"]};
                    background: url('{background_image_url}') no-repeat center center fixed;
                    background-size: cover;
                    position: relative;
                    overflow: auto;
                }}
                .container {{
                    max-width: 600px;
                    margin: 50px auto;
                    background: rgba(255, 255, 255, 0.85);
                    border-radius: 15px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
                    overflow: hidden;
                    position: relative;
                    z-index: 2;
                }}
                .header {{
                    background-color: { selected_theme["header_color"] };
                    padding: 20px;
                    text-align: center;
                    color: {selected_theme["text_header_color"]};
                    border-bottom: 5px solid { selected_theme["header_color"] };
                }}
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                }}
                .content {{
                    padding: 20px 30px;
                    line-height: 1.8;
                }}
                .content p {{
                    margin: 0 0 15px;
                }}
                .quote {{
                    margin: 20px 0;
                    font-style: italic;
                    text-align: center;
                    color: {selected_theme["text_quote_color"]};
                }}
                .footer {{
                    background-color: { selected_theme["footer_color"] };
                    text-align: center;
                    padding: 15px;
                    font-size: 14px;
                    color: {selected_theme["text_footer_color"]};
                }}
                .btn {{
                    display: inline-block;
                    margin: 20px 0;
                    padding: 10px 20px;
                    background-color: { selected_theme["button_color"] };
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                }}
                .btn:hover {{
                    background-color: { selected_theme["hover_color"] };
                }}
                .kiss {{
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: 1;
                    font-size: 25px;
                }}
                .kiss span {{
                    position: absolute;
                    top: -50px;
                    animation: fall 5s linear infinite;
                }}
                @keyframes fall {{
                    0% {{
                        transform: translateY(0) rotate(0deg);
                        opacity: 1;
                    }}
                    100% {{
                        transform: translateY(100vh) rotate(360deg);
                        opacity: 0;
                    }}
                }}
                .kiss span:nth-child(1) {{
                    left: 10%;
                    animation-delay: 0s;
                }}
                .kiss span:nth-child(2) {{
                    left: 25%;
                    animation-delay: 2s;
                }}
                .kiss span:nth-child(3) {{
                    left: 50%;
                    animation-delay: 4s;
                }}
                .kiss span:nth-child(4) {{
                    left: 70%;
                    animation-delay: 1s;
                }}
                .kiss span:nth-child(5) {{
                    left: 90%;
                    animation-delay: 3s;
                }}
            </style>
        </head>
        <body>
            <div class="kiss">
                <span>💋</span>
                <span>💋</span>
                <span>💋</span>
                <span>💋</span>
                <span>💋</span>
            </div>
            <div class="container">
                <div class="header">
                    <h1>给我最爱的 {name} 💖</h1>
                </div>
                <div class="content">
                    <p>亲爱的 {name}：</p>
                    <p>{content_with_line_breaks}</p>
                    <div class="quote">
                        “{quote}”
                    </div>
                    <p>永远爱你的，<br>{sender}</p>
                    <a href="{link}" class="btn">宝宝拆拆看</a>
                </div>
                <div class="footer">
                    <p>💌 写给最特别的你 | 未来的每一天，我们一起走过。</p>
                </div>
            </div>
        </body>
        </html>
    """

send_email(subject, html_template, sender_email, sender_password, receiver_email)

