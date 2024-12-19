(() => {
  let group = document.getElementsByClassName('links_group')[0];
  let data = [];

  async function rendertoolbox() {
    const response = await fetch('https://images.maxiansen.top/blog/data/toolbox.json'); // 替换为你的数据路径
    if (!response.ok) {
      throw new Error(`HTTP 错误！状态码: ${response.status}`);
    }
    data = await response.json();

    // 遍历数据并生成 HTML
    data.forEach(item => {
      let html = `
    <div class="toolboxs">
      <a href="${item.url}" class="toolbox_link">
        <div class="left_image">
          <image src="${item.image}" alt="icon">
        </div>
        <div class="content">
          <div class="text_title">${item.text}</div>
          <div class="text_title2">${item.url}</div>
        </div>
      </a>
    </div>
  `;

      // 将生成的 HTML 字符串转换为 DOM 元素并添加到 group
      let div = document.createElement('div');
      div.innerHTML = html.trim(); // 生成 DOM 元素
      group.appendChild(div.firstChild); // 只添加第一个子元素（即生成的 <div>）
    });
  }
  rendertoolbox();
})()