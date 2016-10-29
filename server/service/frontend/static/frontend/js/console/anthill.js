
/* Submit button */
function submitbutton(pressbutton){
    submitform(pressbutton);
}

/* Submit tha main form */
function submitform(pressbutton){
    jQuery('form[name=adminform] input[name=task]').val(pressbutton);

    try {
        jQuery('.xheditor').val(jQuery('.xheditor').val());
    }catch(e){}

    if(pressbutton == 'filter'){
        jQuery("form[name=adminform]").attr('method','get');
    }

    jQuery("form[name=adminform]").submit();
}

/* check if something is selected */
function isChecked(isitchecked)
{
    if (isitchecked == true)
        document.adminform.boxchecked.value++;
    else
        document.adminform.boxchecked.value--;
}

/* orering of things */
function listItemTask(id, task){
    var f = document.adminform;
    cb = eval('f.' + id);

    if (cb){
        cb.checked = true;
        submitbutton(task);
    }

    return false;
}

function listItemCheck(id){
    var f = document.adminform;
    cb = eval( 'f.' + id );

    if (cb){
        cb.checked = true;
        Highlight(cb);
        document.adminform.boxchecked.value++;
    }

    return false;
}

function Toggle(e)
{
    if (e.checked)
        Highlight(e);
    else
        Unhighlight(e);
}

function ToggleAll(e)
{
    if (e.checked)
        CheckAll();
    else
        ClearAll();
}

function Check(e)
{
    e.checked = true;
    isChecked(e.checked);
}

function Clear(e)
{
    e.checked = false;
    isChecked(e.checked);
}

function CheckAll()
{
    var ml  = document.adminform;
    var len = ml.elements.length;

    for (var i = 0; i < len; i++)
    {
        var e = ml.elements[i];

        if (e.name == "_id_[]")
        {
            Check(e);
            Highlight(e);
        }
    }
}

function ClearAll()
{
    //jQuery("from[name=adminform]");
    var ml  = document.adminform;
    var len = ml.elements.length;

    for (var i = 0; i < len; i++)
    {
        var e = ml.elements[i];
        if (e.name == "_id_[]" )
        {
            Clear(e);
            Unhighlight(e);
        }
    }
}

function Highlight(e)
{
    var r = null;

    if (e.parentNode && e.parentNode.parentNode)
        r = e.parentNode.parentNode;
    else if (e.parentElement && e.parentElement.parentElement)
        r = e.parentElement.parentElement;

    if (r)
    {
        if (r.className == "wbg")
            r.className = "wbgs";

        if (r.className == "gbg")
            r.className = "wgbg";
    }
}

function Unhighlight(e)
{
    var r = null;

    if (e.parentNode && e.parentNode.parentNode)
        r = e.parentNode.parentNode;
    else if (e.parentElement && e.parentElement.parentElement)
        r = e.parentElement.parentElement;

    if (r)
    {
        if (r.className == "wbgs")
            r.className = "wbg";

        if (r.className == "wgbg")
            r.className = "gbg";
    }
}

function changeImage(srcObj,srcListName,dir)
{
    var image = eval ( 'document.image_' + srcListName );

    if(srcObj.value == '' || srcObj.value == null)
        image.src = '/assets/images/console/common/noimage.gif';
    else
        image.src = dir + srcObj.value;
}

//获取QueryString的数组

function getQueryString() {
     var result = location.search.match(new RegExp("[\?\&][^\?\&]+=[^\?\&]+","g")); 

     if(result == null)
         return "";

     for(var i = 0; i < result.length; i++)
         result[i] = result[i].substring(1);

     return result;
}

//根据QueryString参数名称获取值
function getQueryStringByName(name) {
     var result = location.search.match(new RegExp("[\?\&]" + name+ "=([^\&]+)","i"));
     
     if(result == null || result.length < 1)
         return "";

     return result[1];
}

//根据QueryString参数索引获取值
function getQueryStringByIndex(index) {
     if(index == null)
         return "";

     var queryStringList = getQueryString();

     if (index >= queryStringList.length)
         return "";

     var result     = queryStringList[index];
     var startIndex = result.indexOf("=") + 1;
     result         = result.substring(startIndex);

     return result;
}