$.fn.getFormValues = function(form) {
	var elements = {},
		element;
	var tagElements = form.getElementsByTagName('input');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		switch(element.type.toLowerCase()) {
			case 'checkbox':
			case 'radio':
				if(element.checked) {
					elements[element.name] = element.value;
				}
				break;
			default:
				elements[element.name] = element.value;
				break;
		}
	}
	tagElements = form.getElementsByTagName('select');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		elements[element.name] = element.value;
	}
	tagElements = form.getElementsByTagName('textarea');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		elements[element.name] = element.value;
	}
	return elements;
}
$.fn.setFormValues = function(form, values) {
	var elements = {},
		element;
	var tagElements = form.getElementsByTagName('input');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		switch(element.type.toLowerCase()) {
			case 'checkbox':
			case 'radio':
				if(values[element.name]) {
					element.checked = 'checked';
				}
				break;
			default:
				element.value = values[element.name];
				break;
		}
	}
	tagElements = form.getElementsByTagName('select');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		if(typeof values[element.name] != 'undefined') {
			element.value = values[element.name];
		}
	}
	tagElements = form.getElementsByTagName('textarea');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		if(typeof values[element.name] != 'undefined') {
			element.value = values[element.name];
		}
	}
}
$.fn.validateForm = function(form) {
	var flag = false,
		element, parentEl;
	var tagElements = form.getElementsByTagName('input');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		parentEl = $('input[name=' + element.name + ']').parent();
		if(element.required && /^\s*$/.test(element.value)) {
			if(parentEl.next('.icon_dnx_warn').length == 0) {
				parentEl.after('<div class="item-after icon icon_dnx_warn"></div>');
			}
			flag = true;
		} else {
			if(parentEl.next('.icon_dnx_warn').length > 0) {
				!parentEl.next('.icon_dnx_warn').remove();
			}
		}
	}
	tagElements = form.getElementsByTagName('select')
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		parentEl = $('select[name=' + element.name + ']').parent();
		if(element.required && /^\s*$/.test(element.value)) {
			if(parentEl.next('.icon_dnx_warn').length == 0) {
				parentEl.after('<div class="item-after icon icon_dnx_warn"></div>');
			}
			flag = true;
		} else {
			if(parentEl.next('.icon_dnx_warn').length > 0) {
				!parentEl.next('.icon_dnx_warn').remove();
			}
		}
	}
	tagElements = form.getElementsByTagName('textarea');
	for(var j = 0; j < tagElements.length; j++) {
		element = tagElements[j];
		parentEl = $('textarea[name=' + element.name + ']').parent();
		if(element.required && /^\s*$/.test(element.value)) {
			if(parentEl.next('.icon_dnx_warn').length == 0) {
				parentEl.after('<div class="item-after icon icon_dnx_warn"></div>');
			}
			flag = true;
		} else {
			if(parentEl.next('.icon_dnx_warn').length > 0) {
				!parentEl.next('.icon_dnx_warn').remove();
			}
		}
	}
	return flag;
}
$.fn.isNotBlank = function(str) {
	return(str) && (str != null) && (str != 'null') && (str != 'undefined') && (!/^\s*$/.test(str));
}
$.fn.isBlank = function(str) {
	return(/^\s*$/.test(str)) || (str == null) || (str === 'null') || (str === 'undefined');
}
$.fn.getUrlParam = function(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
	var r = window.location.search.substr(1).match(reg);
	if(r != null) {
		return unescape(r[2]);
	} else {
		return null;
	}
}
$.fn.getWeekStart = function(date) {
	var weekStartDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 1);
	return this.formatDate(weekStartDate);
}
$.fn.getWeekEnd = function(date) {
	var weekStartDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() + (7 - date.getDay()));
	return this.formatDate(weekStartDate);
}
$.fn.getMonthStart = function(date) {
	var monthStartDate = new Date(date.getFullYear(), date.getMonth(), 1);
	return this.formatDate(monthStartDate);
}
$.fn.getMonthEnd = function(date) {
	var monthEndDate = new Date(date.getFullYear(), date.getMonth(), this.getDayInMonth(date));
	return this.formatDate(monthEndDate);
}
$.fn.getQuarterStart = function(date) {
	var quarterStartDate = new Date(date.getFullYear(), this.getQuarterStartMonth(date), 1);
	return this.formatDate(quarterStartDate);
}
$.fn.getQuarterEnd = function(date) {
	var quarterEndMonth = this.getQuarterStartMonth(date) + 2;
	var quarterEndDate = new Date(date.getFullYear(), quarterEndMonth, 1);
	var quarterEndDay = this.getDayInMonth(quarterEndDate);
	quarterEndDate.setDate(quarterEndDay);
	return this.formatDate(quarterEndDate);
}
$.fn.getYearStart = function(date) {
	var yearStartDate = new Date(date.getFullYear(), 0, 1);
	return this.formatDate(yearStartDate);
}
$.fn.getYearEnd = function(date) {
	var yearEndDate = new Date(date.getFullYear(), 11, 1);
	var yearEndDay = this.getDayInMonth(yearEndDate);
	yearEndDate.setDate(yearEndDay);
	return this.formatDate(yearEndDate);
}
$.fn.getDayInMonth = function(date) {
	var monthStartDate = new Date(date.getFullYear(), date.getMonth(), 1);
	var monthEndDate = new Date(date.getFullYear(), date.getMonth() + 1, 1);
	var days = (monthEndDate - monthStartDate) / (1000 * 60 * 60 * 24);
	return days;
}
$.fn.getQuarterStartMonth = function(date) {
	var quarterStartMonth = 0;
	var nowMonth = date.getMonth();
	if(nowMonth < 3) {
		quarterStartMonth = 0;
	}
	if(2 < nowMonth && nowMonth < 6) {
		quarterStartMonth = 3;
	}
	if(5 < nowMonth && nowMonth < 9) {
		quarterStartMonth = 6;
	}
	if(nowMonth > 8) {
		quarterStartMonth = 9;
	}
	return quarterStartMonth;
}
$.fn.formatDate = function(date) {
	var myyear = date.getFullYear();
	var mymonth = date.getMonth() + 1;
	var mydate = date.getDate();
	if(mymonth < 10) {
		mymonth = "0" + mymonth;
	}
	if(mydate < 10) {
		mydate = "0" + mydate;
	}
	return(myyear + "-" + mymonth + "-" + mydate);
}
$.fn.compareDate = function(str1, str2) {
	var startDate = new Date(Date.parse(str1.replace(/-/g, '/')));
	var endDate = new Date(Date.parse(str2.replace(/-/g, '/')));
	if(startDate.getTime() == endDate.getTime()) {
		return 0;
	} else if(startDate.getTime() < endDate.getTime()) {
		return 1;
	} else {
		return -1;
	}
}