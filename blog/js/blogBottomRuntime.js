setInterval(() => {
    let create_time = Math.round(new Date('2021-07-03 00:00:00').getTime() / 1000); // 将建站时间转换为时间戳（单位：秒）
    let timestamp = Math.round((new Date().getTime()) / 1000); // 获取当前时间的时间戳（单位：秒）
    let second = timestamp - create_time; // 计算网站运行的总时间（单位：秒）
  
    let nol = function(h) {
      return h > 9 ? h : '0' + h; // 如果数字小于10，则在前面补零；否则直接返回数字
    }
  
    // 计算运行时间
    let days = parseInt(second / (24 * 3600)); // 总天数
    second %= 24 * 3600; // 剩余秒数
    let hours = nol(parseInt(second / 3600)); // 小时数
    second %= 3600; // 剩余秒数
    let minutes = nol(parseInt(second / 60)); // 分钟数
    let seconds = nol(second % 60); // 秒数
  
    // 生成时间字符串加跳动的 SVG 爱心
    let currentTimeHtml = `本站运行了 ${days} 天 ${hours} 小时 ${minutes} 分 ${seconds} 秒 
      <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="red" viewBox="0 0 16 16" class="heartbeat">
        <path d="M8 15s-3.315-2.253-5.373-4.303C.67 8.393 0 6.627 0 5a4 4 0 0 1 8-1.268A4 4 0 0 1 16 5c0 1.627-.67 3.393-2.627 5.697C11.315 12.747 8 15 8 15z"/>
      </svg>`;
  
    document.getElementById("workboard").innerHTML = currentTimeHtml; // 将生成的 HTML 内容动态更新到页面的元素中
  }, 1000); // 每隔 1 秒钟重新计算并更新运行时间和状态
  
  // 添加 CSS 样式使 SVG 爱心跳动
  const style = document.createElement('style');
  style.innerHTML = `
    .heartbeat {
      animation: heartbeat 1s infinite;
      transform-origin: center;
    }
    @keyframes heartbeat {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.2); }
    }
  `;
  document.head.appendChild(style);
  
