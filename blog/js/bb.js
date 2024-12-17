let currentIndex = 0; // 当前加载数据的起始索引
const loadCount = 10; // 每次加载的数据条数，方便后期修改
let allRants = []; // 保存所有的唠叨数据

// 假设你已经从后端或某个文件加载了所有的 rants 数据
async function fetchRants() {
  try {
    const response = await fetch('./1.json'); // 替换为你的数据路径
    if (!response.ok) {
      throw new Error(`HTTP 错误！状态码: ${response.status}`);
    }
    allRants = await response.json();
    renderRants(); // 页面加载完成后，自动加载初始的条数
  } catch (error) {
    console.error('加载数据失败:', error);
  }
}

// 渲染 rants 数据
function renderRants() {
  const rantList = document.getElementById('rant-list');
  const loadMoreButton = document.querySelector('.load-more');
  const noMoreText = document.querySelector('.no-more');
  const loadingSpinner = document.querySelector('.loading-spinner');

  // 获取当前需要加载的数据
  const newRants = allRants.slice(currentIndex, currentIndex + loadCount);

  // 如果没有更多数据，隐藏加载更多按钮并显示 "到底了"
  if (newRants.length === 0) {
    loadMoreButton.classList.add('hidden');
    noMoreText.classList.remove('hidden');
    loadingSpinner.classList.add('hidden');
    return;
  }

  // 渲染每一条 rant
  newRants.forEach(rant => {
    const rantCard = document.createElement('article');
    rantCard.classList.add('rant-card');

    rantCard.innerHTML = `
      <div class="rant-header">
        <image class="avatar" src="${rant.avatar}" alt="头像">
        <div class="user-info">
          <h3 class="username">${rant.username || '站长'}</h3>
          <span class="date">${rant.date || '未知日期'}</span>
        </div>
      </div>
      <div class="rant-content">
        <p>${rant.content || '这里是站长的唠叨内容。'}</p>
      </div>
      ${
        rant.images
          ? `<div class="flex_image">
               <a href="${rant.images}" data-fancybox="gallery">
                 <image src="${rant.images}" alt="图片" class="rant-image">
               </a>
             </div>`
          : ''
      }
      <div class="rant-footer">
        <span class="tag">日常唠叨 📝</span>
      </div>
    `;

    rantList.appendChild(rantCard);
  });

  // 更新当前索引
  currentIndex += loadCount;

  // 更新加载更多按钮状态
  updateLoadMoreButton();
}

// 更新 "加载更多" 按钮的状态
function updateLoadMoreButton() {
  const loadMoreButton = document.querySelector('.load-more');
  const noMoreText = document.querySelector('.no-more');
  const loadingSpinner = document.querySelector('.loading-spinner');

  // 如果没有更多数据，隐藏 "加载更多" 按钮并显示 "到底了"
  if (currentIndex >= allRants.length) {
    loadMoreButton.classList.add('hidden');
    noMoreText.classList.remove('hidden');
  } else {
    loadMoreButton.classList.remove('hidden');
    noMoreText.classList.add('hidden');
  }

  loadingSpinner.classList.add('hidden'); // 隐藏加载中动画
}

// "加载更多" 按钮的点击事件
window.loadMoreRants = async function () {
  const loadMoreButton = document.querySelector('.load-more');
  const loadMoreText = document.getElementById('loadMoreText');
  const loadingSpinner = document.querySelector('.loading-spinner');

  loadMoreText.textContent = '加载中...'; // 按钮文字变为“加载中...”
  loadingSpinner.classList.remove('hidden'); // 显示加载中动画

  // 模拟延迟加载
  setTimeout(() => {
    renderRants(); // 每次点击加载数据
    loadMoreButton.classList.remove('hidden'); // 显示加载更多按钮
    loadingSpinner.classList.add('hidden'); // 隐藏加载中动画
  }, 1000); // 假设延迟1秒
};

// 页面加载时自动加载初始的数据
(() => {
  fetchRants();
})()