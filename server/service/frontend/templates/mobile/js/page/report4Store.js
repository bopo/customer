// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	initPage();
});

function initPage() {
	var userId = window.sessionStorage.getItem("userId");
	$.ajax({
		url: '../servlet/ReportServlet',
		dataType: 'json',
		type: 'get',
		data: {
			action: 'report4Store',
			userId: userId
		},
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		success: function(data, status) {
			if(data.success == 1) {
				var names = [];
				for(var i = 0; i < data.values.length; i++) {
					names.push(data.values[i].name);
				}
				data.names = names;
				renderBarChart(data);
			} else {
				$.toast(data.msg);
			}
		}
	});
}

function renderBarChart(data) {
	var myChart = echarts.init(document.getElementById('report_store'));
	var option = {
		tooltip: {
			trigger: 'item',
			formatter: "{b}: {d}%"
		},
		legend: {
			orient: 'horizontal',
			x: 'center',
			y: '10px',
			data: data.names,
			textStyle: {
				fontSize: '11'
			}
		},
		calculable: false,
		series: [{
			name: '库存状况',
			type: 'pie',
			radius: '95%',
			itemStyle: {
				normal: {
					label: {
						position: 'inner',
						formatter: function(params) {
							return params.name + '\n' + params.value + params.data.unit
						}
					},
					labelLine: {
						show: false
					}
				},
				emphasis: {
					label: {
						show: true,
						formatter: function(params) {
							return params.name + '\n' + params.value + params.data.unit
						}
					}
				}

			},
			data: data.values
		}]
	};
	myChart.setOption(option);
	window.onresize = function() {
		myChart.resize();
	}
}