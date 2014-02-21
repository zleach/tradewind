$( document ).ready(function() {
  $('#myAffix').affix({
    offset: {
      top: 0
    , bottom: function () {
        return (this.bottom = $('.bs-footer').outerHeight(true))
      }
    }
  })    

  // Range Sliders
  
  $("#genderMix").bind("change", function(event){
    var mix = $("#genderMix").val();
    var display = $("#genderMixDisplay")
    
    var text = (mix)+"% M"+" / "+Math.abs(mix-100) + "% F";
    display.html(text);
  }).change();

  $("#crewSize").bind("change", function(event){
    var size = $("#crewSize").val();
    var display = $("#crewSizeDisplay")    
    var text = size/10+"x";
    display.html(text);
  }).change();
});

var aVocab = new Array();

var intIncr
var intCat

intCat =0
intIncr=0

//The data stored is pretty simple.  It works like this:
//
// The aVocab array has sub arrays that are named lists of data.
//
//aVocab[intCat]= new Array(); - The aVocab Array actually holds other arrays.
//aVocab[intCat][0]="FIRST" - This is the name of the list of data in this sub array.  The name helps the program find the data.
//aVocab[intCat][1] = new Array() - Yep, ANOTHER array - this is the array that holds the actual data.
//aVocab[intCat][1][intIncr++]="First thing <SECOND>" // See that <SECOND> tag?  Anything in brackets references another list.
//aVocab[intCat][1][intIncr++]="First thing <THIRD>"
//
// Unless it's the last entry, don't forget to increment and reset the counters!
//
//intCat++
//intIncr=0


aVocab[intCat]= new Array();
aVocab[intCat][0]="FIRST"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="This <personality> <age>-year-old boy has <eyecolor> eyes, a<skincolor> complexion, and <hairtype> <haircolor> hair <hairstyle>.  He is <height>, <weight>, and <fashion>.  He <trivstuff>."
aVocab[intCat][1][intIncr++]="This <personality> <age>-year-old girl has <eyecolor> eyes, a<skincolor> complexion, and <hairtype> <haircolor> hair <hairstyle>.  She is <height>, <weight>, and <fashion>.  She <trivstuff>."


intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="personality"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="ambitious"
aVocab[intCat][1][intIncr++]="arrogant"
aVocab[intCat][1][intIncr++]="energetic"
aVocab[intCat][1][intIncr++]="gentle"
aVocab[intCat][1][intIncr++]="kind-hearted"
aVocab[intCat][1][intIncr++]="moody"
aVocab[intCat][1][intIncr++]="outgoing"
aVocab[intCat][1][intIncr++]="outspoken"
aVocab[intCat][1][intIncr++]="playful"
aVocab[intCat][1][intIncr++]="rambunctious"
aVocab[intCat][1][intIncr++]="rebellious"
aVocab[intCat][1][intIncr++]="serious"
aVocab[intCat][1][intIncr++]="short-tempered"
aVocab[intCat][1][intIncr++]="shy"
aVocab[intCat][1][intIncr++]="spiteful"
aVocab[intCat][1][intIncr++]="quiet"
aVocab[intCat][1][intIncr++]="wacky"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="haircolor"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="auburn"
aVocab[intCat][1][intIncr++]="black"
aVocab[intCat][1][intIncr++]="blond"
aVocab[intCat][1][intIncr++]="brown"
aVocab[intCat][1][intIncr++]="dark brown"
aVocab[intCat][1][intIncr++]="dull blond"
aVocab[intCat][1][intIncr++]="golden-blond"
aVocab[intCat][1][intIncr++]="light brown"
aVocab[intCat][1][intIncr++]="platinum blond"
aVocab[intCat][1][intIncr++]="red"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="eyecolor"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="blue"
aVocab[intCat][1][intIncr++]="brown"
aVocab[intCat][1][intIncr++]="dark brown"
aVocab[intCat][1][intIncr++]="gray"
aVocab[intCat][1][intIncr++]="green"
aVocab[intCat][1][intIncr++]="hazel"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="skincolor"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]=" dark"
aVocab[intCat][1][intIncr++]=" fair"
aVocab[intCat][1][intIncr++]=" pale"
aVocab[intCat][1][intIncr++]="n olive"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="hairtype"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="straight"
aVocab[intCat][1][intIncr++]="wavy"
aVocab[intCat][1][intIncr++]="curly"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="hairstyle"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="neatly braided"
aVocab[intCat][1][intIncr++]="cut short"
aVocab[intCat][1][intIncr++]="in a <length> braid"
aVocab[intCat][1][intIncr++]="in a <length> ponytail"
aVocab[intCat][1][intIncr++]="left uncut"
aVocab[intCat][1][intIncr++]="pinned neatly back"
aVocab[intCat][1][intIncr++]="worn <length>"
aVocab[intCat][1][intIncr++]="worn loose about the shoulders"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="length"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="long"
aVocab[intCat][1][intIncr++]="mid-length"
aVocab[intCat][1][intIncr++]="short"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="age"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="13"
aVocab[intCat][1][intIncr++]="14"
aVocab[intCat][1][intIncr++]="15"
aVocab[intCat][1][intIncr++]="16"
aVocab[intCat][1][intIncr++]="17"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="weight"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="quite thin"
aVocab[intCat][1][intIncr++]="somewhat thin"
aVocab[intCat][1][intIncr++]="of average weight"
aVocab[intCat][1][intIncr++]="a bit pudgy"
aVocab[intCat][1][intIncr++]="quite heavy"
aVocab[intCat][1][intIncr++]="fairly muscular"
aVocab[intCat][1][intIncr++]="quite muscular"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="height"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="of average height"
aVocab[intCat][1][intIncr++]="tall"
aVocab[intCat][1][intIncr++]="a little tall"
aVocab[intCat][1][intIncr++]="very tall"
aVocab[intCat][1][intIncr++]="short"
aVocab[intCat][1][intIncr++]="a little short"
aVocab[intCat][1][intIncr++]="very short"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="fashion"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="dresses very modestly"
aVocab[intCat][1][intIncr++]="wears a lot of black"
aVocab[intCat][1][intIncr++]="wears very colorful clothing"
aVocab[intCat][1][intIncr++]="likes slogan shirts"
aVocab[intCat][1][intIncr++]="likes wearing old-fashioned clothing"
aVocab[intCat][1][intIncr++]="likes wearing outrageous clothing"
aVocab[intCat][1][intIncr++]="wears a lot of 'nerdy' clothing"
aVocab[intCat][1][intIncr++]="likes to flash some skin"
aVocab[intCat][1][intIncr++]="dresses quite conservatively"
aVocab[intCat][1][intIncr++]="can't be bothered with fashion"


intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="trivstuff"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="<flaw>, <trivia>, and <skill>"
aVocab[intCat][1][intIncr++]="<flaw> and <trivia>"
aVocab[intCat][1][intIncr++]="<flaw> and <skill>"
aVocab[intCat][1][intIncr++]="<trivia> and <skill>"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="flaw"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="is afraid of water"
aVocab[intCat][1][intIncr++]="is a really picky eater"
aVocab[intCat][1][intIncr++]="is easily confused"
aVocab[intCat][1][intIncr++]="has a learning disorder"
aVocab[intCat][1][intIncr++]="gets lost easily"
aVocab[intCat][1][intIncr++]="is terrible at keeping secrets"
aVocab[intCat][1][intIncr++]="tends to be forgetful"
aVocab[intCat][1][intIncr++]="tends to gossip too much"
aVocab[intCat][1][intIncr++]="had a disabling accident"
aVocab[intCat][1][intIncr++]="has a speech impediment"
aVocab[intCat][1][intIncr++]="speaks with a stutter"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="trivia"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="has a morbid sense of humor"
aVocab[intCat][1][intIncr++]="volunteers for charity"
aVocab[intCat][1][intIncr++]="looks deceptively innocent"
aVocab[intCat][1][intIncr++]="<likelevel> playing video games"
aVocab[intCat][1][intIncr++]="is known for playing pranks"
aVocab[intCat][1][intIncr++]="has a great sense of humor"
aVocab[intCat][1][intIncr++]="<likelevel> listening to <musictype>"
aVocab[intCat][1][intIncr++]="<likelevel> reading <booktype>"
aVocab[intCat][1][intIncr++]="<likelevel> watching <movietype>"
aVocab[intCat][1][intIncr++]="always has some piece of trivia to share"
aVocab[intCat][1][intIncr++]="is quite naive"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="booktype"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="fantasy literature"
aVocab[intCat][1][intIncr++]="historical fiction"
aVocab[intCat][1][intIncr++]="horror literature"
aVocab[intCat][1][intIncr++]="mystery literature"
aVocab[intCat][1][intIncr++]="romance literature"
aVocab[intCat][1][intIncr++]="comics"
aVocab[intCat][1][intIncr++]="manga"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="movietype"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="fantasy movies"
aVocab[intCat][1][intIncr++]="historical movies"
aVocab[intCat][1][intIncr++]="horror movies"
aVocab[intCat][1][intIncr++]="mystery movies"
aVocab[intCat][1][intIncr++]="romance movies"
aVocab[intCat][1][intIncr++]="musicals"
aVocab[intCat][1][intIncr++]="anime"
aVocab[intCat][1][intIncr++]="cartoons"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="likelevel"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="enjoys"
aVocab[intCat][1][intIncr++]="loves"
aVocab[intCat][1][intIncr++]="likes"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="musictype"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="music"
aVocab[intCat][1][intIncr++]="J-Pop"
aVocab[intCat][1][intIncr++]="classical music"
aVocab[intCat][1][intIncr++]="metal"
aVocab[intCat][1][intIncr++]="death metal"
aVocab[intCat][1][intIncr++]="country music"
aVocab[intCat][1][intIncr++]="pop music"
aVocab[intCat][1][intIncr++]="rap"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="skillorambition"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="<skill>"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="ambition"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]=""


intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="skill"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="<skillambrate> artist"
aVocab[intCat][1][intIncr++]="<skillambrate> dancer"
aVocab[intCat][1][intIncr++]="<skillambrate> guitar player"
aVocab[intCat][1][intIncr++]="<skillambrate> leader"
aVocab[intCat][1][intIncr++]="<skillambrate> poet"
aVocab[intCat][1][intIncr++]="<skillambrate> pianist"
aVocab[intCat][1][intIncr++]="<skillambrate> singer"
aVocab[intCat][1][intIncr++]="<skillrate> student"
aVocab[intCat][1][intIncr++]="<skillambrate> writer"

aVocab[intCat][1][intIncr++]="<career>n architect"
aVocab[intCat][1][intIncr++]="<career>n athlete"
aVocab[intCat][1][intIncr++]="<career>n engineer"
aVocab[intCat][1][intIncr++]="<career> mechanic"
aVocab[intCat][1][intIncr++]="<career> programmer"
aVocab[intCat][1][intIncr++]="<career> lawyer"
aVocab[intCat][1][intIncr++]="<career> scientist"
aVocab[intCat][1][intIncr++]="<career> veterinarian"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="career"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="is studying to be a"
aVocab[intCat][1][intIncr++]="wants to be a"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="skillrate"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="is a decent"
aVocab[intCat][1][intIncr++]="is an excellent"
aVocab[intCat][1][intIncr++]="is a horrible"
aVocab[intCat][1][intIncr++]="is a rather poor"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="skillambrate"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="is an aspiring"
aVocab[intCat][1][intIncr++]="wants to be a"
aVocab[intCat][1][intIncr++]="is a decent"
aVocab[intCat][1][intIncr++]="is an excellent"
aVocab[intCat][1][intIncr++]="is a horrible"
aVocab[intCat][1][intIncr++]="is a rather poor"

intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="number"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]="several"
aVocab[intCat][1][intIncr++]="a few"
aVocab[intCat][1][intIncr++]="a couple of"
aVocab[intCat][1][intIncr++]="many"
aVocab[intCat][1][intIncr++]="numerous"

//Leave to Copy!
intCat++
intIncr=0
aVocab[intCat]= new Array();
aVocab[intCat][0]="THIRD"
aVocab[intCat][1] = new Array()
aVocab[intCat][1][intIncr++]=""



	function GenNumber(nRange)
	{
                var iNumGen
		iNumGen = Math.round((Math.random() * nRange));

                return iNumGen;
	}

        function GetFrom(aArray)
	{
		var undefined
		var sReturn
		sReturn = aArray[GenNumber(aArray.length)];
		if (sReturn == undefined)
		{
			sReturn = GetFrom(aArray)
		}
		return sReturn
	}


	function GetArray(sArrayName)
	{
		for (var intLooper=0;intLooper <aVocab.length;intLooper++)
		{
			if (aVocab[intLooper][0]==sArrayName)
			{
				return aVocab[intLooper][1];
				break;
			}
		}
	}

	function ScanLine(sLine)
	{
		var iTagStart, iTagEnd
		var sKey

		if (sLine.indexOf("<") > -1)
		{
			iTagStart = sLine.indexOf("<");
			iTagEnd = sLine.indexOf(">");
			
			sKey = sLine.substr(iTagStart+1, iTagEnd-(iTagStart+1));

			sKey = GetFrom(GetArray(sKey))
			sLine = sLine.substr(0, iTagStart) + sKey + sLine.substr(iTagEnd+1, (sLine.length - iTagEnd))

		}
		

		if (sLine.indexOf("<") > - 1)
		{
			sLine = ScanLine(sLine)
		}

		return sLine;
	}


	function GenPlot()
	{
		sLine = GetFrom(GetArray("FIRST"));

		sLine = ScanLine(sLine)

		return sLine;
	}