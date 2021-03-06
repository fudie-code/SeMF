/** EasyWeb spa v3.1.2 date:2019-06-05 License By http://easyweb.vip */

layui.config({
    version: Date.now(),   // 更新组件缓存，设为true不缓存，也可以设一个固定值
    base: 'assets/module/'
}).extend({
    formSelects: 'formSelects/formSelects-v4',
    treetable: 'treetable-lay/treetable',
    dropdown: 'dropdown/dropdown',
    notice: 'notice/notice',
    step: 'step-lay/step',
    dtree: 'dtree/dtree',
    citypicker: 'city-picker/city-picker',
    tableSelect: 'tableSelect/tableSelect',
    cropper: 'cropper/cropper',
    zTree: 'zTree/zTree',
    uncode:'uncode'
}).use(['config', 'layer', 'element', 'index', 'admin', 'laytpl','table'], function () {
    var $ = layui.jquery;
    var layer = layui.layer;
    var element = layui.element;
    var config = layui.config;
    var index = layui.index;
    var admin = layui.admin;
    var laytpl = layui.laytpl;
    var table = layui.table;

    table.set({headers:{['Authorization']:'JWT ' + config.getToken()}});
    

    // 检查是否登录
    if (!config.getToken()) {
        return location.replace('views/system/login.html');
    }

    //注册全局路由
    admin.ajax({
        url: 'json/router.json'
        , type: 'get'
        , dataType:'JSON'
        , success: (res) => {
            index.regRouter(res);  // 注册路由
        }
    })

    // 加载侧边栏
    admin.ajax({
        url: '/rbac/menu/'
        , type: 'get'
        , dataType:'JSON'
        , success: (res) => {
            laytpl(sideNav.innerHTML).render(res.data, function (html) {
                $('.layui-layout-admin .layui-side .layui-nav').html(html);
                element.render('nav');
            });
            index.regRouter(res.data);  // 注册路由
            index.loadHome({  // 加载主页
                url: '#/index',
                name: '<i class="layui-icon layui-icon-home"></i>'
            });
        }
    })

    // 移除loading动画
    // setTimeout(function () {
    //     admin.removeLoading();
    // }, 100); 
    admin.removeLoading();


});
