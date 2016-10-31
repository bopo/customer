$(document).on('click', '#add_level', function() {
	$.prompt('请输入等级名称', function(value) {
		if(value != "") {
			var userId = window.sessionStorage.getItem("userId");
			if(userId == null) {
				userId = "73e62a2f4c0411e6bce900163e00209a";
			}
			$.ajax({
				type: "POST",
				url: "../servlet/UserServlet",
				data: {
					action: "saveLevelInfo",
					userId: userId,
					title: value
				},
				dataType: 'json',
				success: function(data, textStatus) {
					if(data.success == 1) {
						$.toast("保存成功");
						var levelnum = window.sessionStorage.getItem('levelnum') - 0;
						window.sessionStorage.setItem('levelnum', levelnum + 1);
						initList();
					} else
						$.toast("保存失败," + data.msg);
				}
			});
		} else {
			$.toast("名称不能为空");
		}
	});
});

function deleteLevel(levelId) {
	$.confirm('确定要删除吗？', function() {
		var userId = window.sessionStorage.getItem("userId");
		if($.fn.isNotBlank(userId)) {
			userId = "73e62a2f4c0411e6bce900163e00209a";
		}
		$.ajax({
			type: "POST",
			url: "../servlet/UserServlet",
			data: {
				action: "deleteLevelInfo",

				levelId: levelId
			},
			dataType: 'json',
			success: function(data, textStatus) {
				if(data.success == 1) {
					$.toast("删除成功");

					var levelnum = window.sessionStorage.getItem('levelnum') - 0;
					window.sessionStorage.setItem('levelnum', levelnum - 1);
					initList();
				} else
					$.toast("删除失败," + data.msg);
			}
		});
	});
}

$(document).on("pageInit", ".page", function(e, pageId, $page) {
	initList();
});

function initList() {
	var userId = window.sessionStorage.getItem("userId");
	if(userId == null) {
		userId = "73e62a2f4c0411e6bce900163e00209a";
	}
	//alert("测试信息:"+userId);
	$.ajax({
		type: "GET",
		url: "../servlet/UserServlet",
		data: {
			action: "getLevelList",
			userId: userId
		},
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		dataType: 'json',
		scriptCharset: 'utf-8',
		success: function(data, textStatus) {
			//var obj = eval('(' + data + ')');

			renderPage(data);

		}
	});
}
//渲染界面
function renderPage(data) {
	var tpl = document.getElementById('tpl_levels').innerHTML;
	laytpl(tpl).render(data, function(render) {
		$('#level_list').html(render);
	});
}