// ****************** 樱花特效 ******************
// import "./mayang.js";
// ****************** 樱花特效 ******************

// ****************** 星空背景和流星特效 ******************
import "./universe.js";
// ****************** 星空背景和流星特效 ******************

// ****************** 背景更新 ******************
(() => {
  fetch('http://101.200.151.47:8848/api/get_image_path', {
    method: 'Get',
  }).then(response => {
    return response.json();
  }).then(data => {
    document.getElementById("#web_bg").style.background = data.data.image_path;
  })
})();
// ****************** 背景更新 ******************