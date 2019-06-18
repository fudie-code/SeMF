layui.use(['admin', 'table', 'form', 'dropdown','index'], function () {
    var table = layui.table,
        form = layui.form,
        $ = layui.$,
        admin = layui.admin,
        dropdown = layui.dropdown
        index = layui.index;

    form.render();

    $('#jump').click(()=>{
        index.go('/assetmanage/detial');
    })
    //获取资产类型
    $.ajax({
        url: '/assetmanage/assettype/',
        type: 'GET',
        done: function (res) {
            let data = res.data;
            $.each(data, function (index, item) {
                $('#assettype').append(new Option(item.name, item.id));
            });
            form.render()
        }
    });

    table.render({
        elem: '#rootasset-list',
        url: '/assetmanage/assetlist/',
        toolbar: '#rootasset-toolbar',
        // headers: {
        // 	[layui.setter.request.tokenName]: 'JWT ' + layui.data(layui.setter.tableName)[layui.setter.request.tokenName]
        // },
        defaultToolbar: ['print', 'exports'],
        title: '资产列表',
        cols: [
            [{
                field: 'name',
                title: '资产名称',
                align: 'center',
                unresize: true
            }, {
                field: 'key',
                title: '访问地址',
                align: 'center',
                unresize: true
            }, {
                field: 'type',
                title: '类型',
                align: 'center',
                unresize: true
            }, {
                field: 'manage',
                title: '负责人',
                align: 'center',
                unresize: true
            }, {
                field: 'telephone',
                title: '联系电话',
                align: 'center',
                unresize: true
            }, {
                field: 'email',
                title: '邮箱',
                align: 'center',
                unresize: true
            }, {
                field: 'updatetime',
                title: '更新时间',
                align: 'center',
                unresize: true
            }, {
                field: 'description',
                title: '工程描述',
                hide: true,
                unresize: true
            }, {
                field: 'parent_check',
                title: 'parent',
                hide: true,
                unresize: true
            }, {
                field: 'id',
                title: 'ID',
                hide: true
            }, {
                fixed: 'right',
                title: '操作',
                toolbar: '#rootasset-bar',
                align: 'center',
                width: 150,
                unresize: true
            }]
        ],
        page: true
    });
    // 
    // 		//头工具栏事件
    table.on('toolbar(rootasset-list)', function (obj) {
        switch (obj.event) {
            case 'add':
                admin.open({
                    title: '资产录入',
                    area: ['500px', '660px'],
                    url: './views/assetmanage/assetcreate.html'
                });
            // admin.popup({
            // 	title: '资产录入',
            // 	area: ['500px', '660px'],
            // 	fixed: true,
            // 	maxmin: true,
            // 	success: function(layero, index) {
            // 		//将 views 目录下的某视图文件内容渲染给该面板
            // 		layui.view(this.id).render('assetmanage/create').done(function() {

            // 		});
            // 	},
            // 	end: function() {
            // 		table.reload('rootasset-list');
            // 	}
            // });
        };
    });
    // 
    // 		//监听行工具事件
    // 		table.on('tool(rootasset-list)', function(obj) {
    // 			var data = obj.data;
    // 			if (obj.event === 'del') {
    // 				layer.confirm('确定删除资产', function(index) {
    // 					admin.req({
    // 						url: '/assetmanage/assetdelete/' + data.id + "/" //实际使用请改成服务端真实接口
    // 							,
    // 						type: 'GET',
    // 						done: function(res) {
    // 							//成功的提示与跳转
    // 							layer.msg(res.msg, {
    // 								offset: '15px',
    // 								icon: 1,
    // 								time: 1000
    // 							}, function() {
    // 								layui.index.render();
    // 							});
    // 						}
    // 					});
    // 					obj.del();
    // 					layer.close(index);
    // 				});
    // 			} else if (obj.event === 'detial') {
    // 				location.hash = '/assetmanage/assetdetial/id=' + data.id;
    // 			} else if (obj.event === 'edit') {
    // 				admin.popup({
    // 					title: '修改资产信息',
    // 					area: ['500px', '660px'],
    // 					fixed: true,
    // 					maxmin: true,
    // 					success: function(layero, index) {
    // 						//将 views 目录下的某视图文件内容渲染给该面板
    // 						layui.view(this.id).render('assetmanage/create').done(function() {
    // 							$("#id").val(data.id);
    // 							$("#name").val(uncode(data.name));
    // 							$("#key").val(uncode(data.key));
    // 							$("#type").html(data.type);
    // 							$("#manage").val(uncode(data.manage));
    // 							$("#telephone").val(data.telephone);
    // 							$("#email").val(uncode(data.email));
    // 							$("#description").val(uncode(data.description));
    // 							$("#parent_name").val(uncode(data.parent_check.name)).attr("ts-selected", data.parent_check.id);
    // 							$("#parent").val(data.parent_check.id);
    // 						});
    // 					},
    // 					end: function() {
    // 						table.reload('rootasset-list');
    // 					}
    // 				});
    // 			} else if (obj.event == 'info') {
    // 				layer.tips(data.description, '.layui-table-hover', {
    // 					tips: 1,
    // 					time: 4000
    // 				});
    // 			};
    // 		});
    // 

    //查询并重载表格
    form.on('submit(query)', (d) => {
        table.reload('rootasset-list', {
            page: {
                curr: 1 //重新从第 1 页开始
            },
            where: {
                key: d.field.condition
            }
        });
    })

});