/**
 * 选择列表
 */
function getSelectedValue( frmName, srcListName )
{
    var form    = eval( 'document.' + frmName );
    var srcList = eval( 'form.' + srcListName );

    i = srcList.selectedIndex;

    if (i != null && i > -1)
        return srcList.options[i].value;

    return null;
}

//These are date time functions
// JS Calendar
var calendar = null;

function selected(cal, date)
{
    cal.sel.value = date;
}

function closeHandler(cal)
{
    cal.hide();
    Calendar.removeEvent(document, "mousedown", checkCalendar);
}

function checkCalendar(ev)
{
    var el = Calendar.is_ie ? Calendar.getElement(ev) : Calendar.getTargetElement(ev);

    for (; el != null; el = el.parentNode)

    if (el == calendar.element || el.tagName == "A")
        break;

    if (el == null)
        calendar.callCloseHandler(); Calendar.stopEvent(ev);
}

function showCalendar(id)
{
    var el = document.getElementById(id);

    if (calendar != null)
    {
        calendar.hide();
        calendar.parseDate(el.value);
    }
    else
    {
        var cal = new Calendar(true, null, selected, closeHandler);
        calendar = cal;
        cal.setRange(1900, 2070);
        calendar.create();
    }

    calendar.sel = el;
    calendar.showAtElement(el);
    Calendar.addEvent(document, "mousedown", checkCalendar);

    return false;
}

var $urln=1;

function addurl(obj)
{
    var $play = jQuery('#addurl').parent().parent().prev().prev().html();
    var $playlist = jQuery('#addurl').parent().parent().prev().html();

    jQuery('#addurl').parent().parent().prev().after('<tr>'+$play+'</tr>');
    jQuery('#addurl').parent().parent().prev().after('<tr>'+$playlist+'</tr>');
    jQuery('#addurl').parent().parent().prev().find('textarea').val('');
    jQuery('#addurl').parent().parent().prev().prev().find('select').find('option:selected').attr('selected',false);
    jQuery('#addurl').parent().parent().prev().prev().find('td:first').text('播放类型 new');
    jQuery('#addurl').parent().parent().prev().find('td:first').text('播放地址 new');
}

function delurl(obj)
{

    if(jQuery('.delurl').length <= 1)
    {
        alert('播放地址必须至少一个!');
        return false;
    }    

    jQuery(obj).parent().parent().next().remove();
    jQuery(obj).parent().parent().remove();
}

function ordering (obj) {
    var text = $(obj).parent().parent().next().find('textarea');

    var aa = text.val();
    var tt = aa;
    var cc = tt.split("\n");
    var ee = "";

    for(var i=cc.length-1;i>=0;i--) {
        if(ee!="")
            ee+="\n";

        ee+=cc[i];
    }

    text.val(ee);    
}

function play_replace (obj) {
    var result  = $(obj).parent().parent().next().find('textarea');
    var search  = $(obj).prev().prev().val();
    var replace = $(obj).prev().val();
    
    if (search == '') {
        return false;
    };

    var text = result.val();
    var reg  = new RegExp(search, 'gi');
    result.val(text.replace(reg, replace));
}

function check_name (obj) {
    
}

function collect_url (url) {
    // body...
}