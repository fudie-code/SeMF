layui.define(function (exports) {


    let uncode = (entity) => {
      var div = document.createElement('div');
      div.innerHTML = entity;
      var res = div.innerText || div.textContent;
      return res;
    }
  
    exports('uncode', uncode);
  });