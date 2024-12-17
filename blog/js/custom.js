// ****************** 樱花特效 ******************
// import "./mayang.js";
// ****************** 樱花特效 ******************

// ****************** 星空背景和流星特效 ******************
import "./universe.js";
// ****************** 星空背景和流星特效 ******************

// ****************** 动态标题 ******************
import "./title.js";
// ****************** 动态标题 ******************

// ****************** 背景更新 ******************
(() => {
  // fetch('http://101.200.151.47:8848/api/get_image_path', {
  //   method: 'Get',
  // }).then(response => {
  //   return response.json();
  // }).then(data => {
  //   console.log("data", data.data.image_path);
  // })

  let LOCAL_BG_URL = "https://images.maxiansen.top/blog/public/img/dm7.webp";

  let IS_OPEN_ONLINE_BG_CONFIG = true;

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



  if (IS_OPEN_ONLINE_BG_CONFIG) {
    // fetch('http://101.200.151.47/update_bg/data.json')
    //   .then((response) => response.json())
    //   .then((data) => LOCAL_BG_URL = data.image_path);

  } else {
    LOCAL_BG_URL = item.value;
  }

  document.getElementById("web_bg").style.background = `url(${LOCAL_BG_URL})`;
  document.getElementById("web_bg").style.backgroundSize = 'cover';
  document.getElementById("web_bg").style.backgroundPosition = 'center';

})();
// ****************** 背景更新 ******************