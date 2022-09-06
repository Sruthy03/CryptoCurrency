var values=[];
const getBtcData = async () => {

    var ele = document.getElementsByTagName('input');

 
              
            for(i = 0; i < ele.length; i++) {
                  
                if(ele[i].type="radio") {
                  
                    if(ele[i].checked)
                    values.push(ele[i].value)
                }
            }
            for(i = 0; i < values.length; i++) {
                console.log(values[i])
}
[1]; 
    fetch('https://min-api.cryptocompare.com/data/price?fsym='+values[0]+'&tsyms='+values[1])
   .then(response => response.json())
   .then(data => {
     console.log(data);
     document.getElementById("info").innerHTML = values[0] +'='+data[values[1]] +" "+values[1]
   });
 }
 getBtcData();
 tcount=setInterval(function(){
   tcount++
   if (tcount==5) {getBtcData(); tcount=0}
   document.getElementById("infotime").innerHTML = 'Next update in ' + (5-tcount) + ' seconds'
 },300);
 const getLatestData = async () => {
    const response = await fetch('https://min-api.cryptocompare.com/data/v2/histohour?fsym=' + values[0] +"&tsym="+ values[1]+"&limit=2000&aggregate=1&e=CCCAGG ");
    const json = await response.json();
    const data = json.Data.Data
    const times = data.map(obj => obj.time)
    const high = data.map(obj => obj.high)
    const low = data.map(obj => obj.low)
    const open = data.map(obj => obj.open)
    const close = data.map(obj => obj.close)
    var txt=""
    for (var i=0;i<times.length;i++)
    {
      txt = txt + "\t\t" + serialDateToNiceDate(times[i]) + "\t\t" + high[i]+"\t\t" + low[i] +"\t\t" + open[i]+"\t\t" + close[i]+ "\n"
    }
    document.getElementById("txtout").value = txt
   
getLatestData()
 }

  function serialDateToNiceDate(date) {
    // return new Date(Math.round((date)*86400*1000));
    var ts = new Date(date);
    timeStampCon = ts.toLocaleString()
    return timeStampCon;
  }
