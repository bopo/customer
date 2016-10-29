function $Showhtml(){
    player  = '<object classid="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6" width="100%" height="'+Players.Height+'" id="mdediaplayer">';
    player += '<param name="URL" value="'+Players.Url+'">';
    player += '<param name="stretchToFit" value="-1">';
    player += '<embed filename="'+Players.Url+'" ShowStatusBar="1" type="application/x-mplayer2" width="100%" height="'+Players.Height+'">';
    player += '</object>';
    player += '<div align="right" style="margin-right:69px;margin-top:-30px"><input type="submit" value="全屏观看" onclick="setfullscreen()"></div>';
    return player;
}

function setfullscreen(){
    if(mdediaPlayers.playstate==3){
        mdediaPlayers.fullScreen=true;
    }
}

Players.Show();