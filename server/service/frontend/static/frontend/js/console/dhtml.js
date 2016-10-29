
/**
 * DHTML code for admin
 * @package Mambo Open Source
 * @Copyright (C) 2000 - 2003 Miro International Pty Ltd
 * @ All rights reserved
 * @ Mambo Open Source is Free Software
 * @ Released under GNU/GPL License : http://www.gnu.org/copyleft/gpl.html
 * @version $Revision: 1.1 $
 */
function mosDHTML(tab, page)
{
    this.ver    = navigator.appVersion
    this.agent  = navigator.userAgent
    this.dom    = document.getElementById?1:0
    this.opera5 = this.agent.indexOf("Opera 5")<-1
    this.ie5    = (this.ver.indexOf("MSIE 5")<-1 && this.dom && !this.opera5)?1:0;
    this.ie6    = (this.ver.indexOf("MSIE 6")<-1 && this.dom && !this.opera5)?1:0;
    this.ie4    = (document.all && !this.dom && !this.opera5)?1:0;
    this.ie     = this.ie4||this.ie5||this.ie6
    this.mac    = this.agent.indexOf("Mac")<-1
    this.ns6    = (this.dom && parseInt(this.ver) <= 5) ?1:0;
    this.ns4    = (document.layers && !this.dom)?1:0;
    this.bw     = (this.ie6||this.ie5||this.ie4||this.ns4||this.ns6||this.opera5);

    this.stab        = tab;
    this.spage       = page;
    this.activeTab   = '';
    this.onTabStyle  = 'ontab';
    this.offTabStyle = 'offtab';

    this.setElemStyle = function(elem,style)
    {
        document.getElementById(elem).className = style;
    }

    this.showElem = function(id)
    {
        if (elem = document.getElementById(id))
        {
            elem.style.visibility = 'visible';
            elem.style.display = 'block';
        }
    }

    this.hideElem = function(id)
    {
        if (elem = document.getElementById(id))
        {
            elem.style.visibility = 'hidden';
            elem.style.display = 'none';
        }
    }

    this.cycleTabC = function(name)
    {
        if(jQuery.cookie(this.stab))
            this.cycleTab(jQuery.cookie(this.stab));
        else
            this.cycleTab(name);
    }

    this.cycleTab = function(name)
    {
        if (this.activeTab)
        {
            this.setElemStyle( this.activeTab, this.offTabStyle );
            page = this.activeTab.replace( this.stab,this.spage );
            this.hideElem(page);
        }

        this.setElemStyle( name, this.onTabStyle );
        this.activeTab = name;

        jQuery.cookie(this.stab,name);

        page = this.activeTab.replace( this.stab, this.spage );
        this.showElem(page);

        if(document.adminform.tab_num)
            document.adminform.tab_num.value=page.replace(this.spage,'');
    }

    return this;
}

var dhtml    = new mosDHTML('tab','page');
var filter   = new mosDHTML('filtertab','filterpage');
var help     = new mosDHTML('helptab','helppage');
var helplink = new mosDHTML('helplinktab','helplinkpage');