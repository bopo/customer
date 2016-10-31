var startDate, endDate;
// 初始化界面
$(document).on("pageInit", ".page", function(e, pageId, $page) {
	initPage();
});

$(document).on("click", '.pull-left', function() {
	window.sessionStorage.setItem('checkOutDateType', 'w');
	document.location.href = 'report.html';
});

$(document).on('click', '.pull-right', function() {
	var popupHTML = document.getElementById('tpl_datePopup').innerHTML;
	$.popup(popupHTML);
	var dateType = window.sessionStorage.getItem('checkOutDateType')||'w';
	$('#report_date_list input[name=dateRadio]').each(function(index, item) {
		if(item.value === dateType) {
			$(item).attr('checked', 'checked');
			if(dateType === 'c') {
				$('#customDate').show();
				$('#startDate').val(startDate);
				$('#endDate').val(endDate);
			}
		} else {
			$(item).removeAttr('checked');
		}
	});
	$('#startDate').calendar();
	$('#endDate').calendar();
});

$(document).on('change', '#report_date_list input[name=dateRadio]', function() {
	var dateType = $(this).val();
	window.sessionStorage.setItem('checkOutDateType', dateType);
	if(dateType === 'c') {
		$('#customDate').show();
	} else {
		$('#customDate').hide();
	}
});

$(document).on('click', '#report_in_query_btn', function() {
	initPage();
});

function initPage() {
	var userId = window.sessionStorage.getItem("userId");
	var dateType = window.sessionStorage.getItem('checkOutDateType');
	var now = new Date();
	if($.fn.isBlank(dateType)) {
		dateType = 'w';
	}
	switch(dateType) {
		case 'w':
			startDate = $.fn.getWeekStart(now);
			endDate = $.fn.getWeekEnd(now);
			$('.open-popup').text('本周');
			break;
		case 'm':
			startDate = $.fn.getMonthStart(now);
			endDate = $.fn.getMonthEnd(now);
			$('.open-popup').text('本月');
			break;
		case 'q':
			startDate = $.fn.getQuarterStart(now);
			endDate = $.fn.getQuarterEnd(now);
			$('.open-popup').text('本季');
			break;
		case 'y':
			startDate = $.fn.getYearStart(now);
			endDate = $.fn.getYearEnd(now);
			$('.open-popup').text('本年');
			break;
		default:
			startDate = $('#startDate').val();
			endDate = $('#endDate').val();
			$('.open-popup').text('定义');
	}
	if($.fn.isBlank(startDate)) {
		$.toast('开始时间不能为空');
		return false;
	} else if($.fn.isBlank(endDate)) {
		$.toast('结束时间不能为空');
		return false;
	} else if($.fn.compareDate(startDate, endDate) == -1) {
		$.toast('开始日期不能大于结束日期');
		return false;
	} else {
		$.closeModal('.popup-date');
		$.ajax({
			url: '../servlet/ReportServlet',
			dataType: 'json',
			type: 'get',
			data: {
				action: 'report4Out',
				userId: userId,
				startDate: startDate,
				endDate: endDate
			},
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			success: function(data, status) {
				if(data.success == 1) {
					$('.content-block-title').text('总出货：' + data.totalMoney);
					data.sd = startDate;
					data.ed = endDate;
					renderLineChart(data);
				} else {
					$.toast(data.msg);
				}
			}
		});
	}
}

function renderLineChart(data) {
	var tpl = document.getElementById('tpl_report4Out').innerHTML;
	laytpl(tpl).render(data, function(render) {
		$('#report_out_list').html(render);
	});
}