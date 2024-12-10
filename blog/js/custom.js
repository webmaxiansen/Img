// ****************** 樱花特效 ******************
// import "./mayang.js";
// ****************** 樱花特效 ******************

// ****************** 星空背景和流星特效 ******************
import "./universe.js";
// ****************** 星空背景和流星特效 ******************

// ****************** 背景更新 ******************
(() => {
  // fetch('http://101.200.151.47:8848/api/get_image_path', {
  //   method: 'Get',
  // }).then(response => {
  //   return response.json();
  // }).then(data => {
  //   document.getElementById("#web_bg").style.background = data.data.image_path;
  // })
  const itemStr = localStorage.getItem("image_path");

  // 如果没有找到数据，则返回 null
  if (!itemStr) {
    return;
  }

  const item = JSON.parse(itemStr);
  const now = new Date();

  // 如果数据过期了，清除并返回 null
  if (now.getTime() > item.expiry) {
    localStorage.removeItem(key);
    return;
  }

  document.getElementById("web_bg").style.background = item.value;
})();
// ****************** 背景更新 ******************
